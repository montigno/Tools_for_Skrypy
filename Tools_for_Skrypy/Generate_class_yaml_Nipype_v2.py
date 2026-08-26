import json
import yaml

# --------------------------------------------------
# Lecture du fichier JSON
# --------------------------------------------------

# yaml_file = "/home/honorom/eclipse-workspace/skrypy-pyqt5/NodeEditor/modules/Nipype/Interfaces_afni.yml"
# with open(yaml_file, "r", encoding="utf-8") as f:
#     yaml1 = yaml.safe_load(f)

with open("nipype_interfaces_v2.json", "r", encoding="utf-8") as f:
    data = json.load(f)

LIST_SIMPLE_TYPE = ['Int', 'Float', 'Str', 'Bool', 'File', 'Directory']
LIST_SIMPLE_VALUE = [0, 0.0, '', True, 'path', 'path']

class CodeGenerator:

    def __init__(self, indentation=' '*4):
        self.indentation = indentation
        self.level = 0
        self.code = ''

    def indent(self):
        self.level += 1

    def dedent(self):
        if self.level > 0:
            self.level -= 1

    def __add__(self, value):
        temp = CodeGenerator(indentation=self.indentation)
        temp.level = self.level
        temp.code = str(self) + ''.join([self.indentation for i in range(0, self.level)]) + str(value)
        return temp

    def __str__(self):
        return str(self.code)
    

class FlowStyleDumper(yaml.SafeDumper):
    pass


def represent_list(dumper, data):
    """Représente les listes au format [a, b, c]."""
    return dumper.represent_sequence(
        "tag:yaml.org,2002:seq",
        data,
        flow_style=True
    )


FlowStyleDumper.add_representer(list, represent_list)

def get_values_list(structure_info):
    element_type = structure_info['element']['type']
    if element_type in LIST_SIMPLE_TYPE:
        value_default = LIST_SIMPLE_VALUE[LIST_SIMPLE_TYPE.index(element_type)]
        return [value_default]
    elif element_type == 'Tuple':
        elements_type = structure_info['element']['elements']
        value_default = []
        for elem in elements_type:
            value_default.append(LIST_SIMPLE_VALUE[LIST_SIMPLE_TYPE.index(elem['type'])])
        return value_default
    elif element_type == 'Enum':
        value_default = structure_info['element']['values']
        return value_default
    elif element_type == 'List':
        value_default = structure_info['element']
        return value_default
    elif element_type == 'TraitCompound':
        elements_types = structure_info['element']['types']
        try:
            value_default = elements_types[0]['default']
        except:
            value_default = elements_types[0]['type']
        value_type = elements_types[0]['type']
        if not value_default:
            if value_type in LIST_SIMPLE_TYPE:
                value_default = [LIST_SIMPLE_VALUE[LIST_SIMPLE_TYPE.index(value_type)]]
        return value_default        

def get_values_MultiObject(structure_info):
    element_type = structure_info['element']['type']
    value_default = None
    if element_type == 'Enum':
        value_default = structure_info['element']['values']
        return value_default 
    elif element_type in LIST_SIMPLE_TYPE:
        value_default = LIST_SIMPLE_VALUE[LIST_SIMPLE_TYPE.index(element_type)]
        value_default = [value_default]
    elif element_type == 'TraitCompound':
        value_default = structure_info['element']['types'][0]
        # print('TraitCompound', value_default)

        if value_default['type'] in LIST_SIMPLE_TYPE:
            value_default = LIST_SIMPLE_VALUE[LIST_SIMPLE_TYPE.index(value_default['type'])]
            value_default = [value_default]
        elif value_default['type'] == "Enum":
            value_default = value_default['values']
        # elif value_default['type'] == "Tuple":
            
    return value_default

def get_values_TraitCompound(structure_info):
    value_default = structure_info['types'][0]
    if value_default['type'] == 'Enum':
        value_default = value_default['values']
    elif value_default['type'] in LIST_SIMPLE_TYPE:
        value_def = value_default['default']
        if not value_def:
            value_def = LIST_SIMPLE_VALUE[LIST_SIMPLE_TYPE.index(value_default['type'])]
        value_default = value_def
    return value_default
        
        
def get_default_value(value_type):
    # print("value_type=", value_type)
    if value_type['type'] == 'List':
        value_default = get_values_list(value_type['structure'])
    elif value_type['type'] in LIST_SIMPLE_TYPE:
        value_default = value_type['default']
        if not value_default:
            value_default = LIST_SIMPLE_VALUE[LIST_SIMPLE_TYPE.index(value_type['type'])]
    elif value_type['type'] == 'Enum':
        value_default = value_type['structure']['values']
    elif value_type['type'] == 'InputMultiObject':
        value_default = get_values_MultiObject(value_type['structure'])
    elif value_type['type'] == 'TraitCompound':
        value_default = get_values_TraitCompound(value_type['structure'])
    else:
        value_default = value_type['default']
    return value_default

def get_input_mandatory_no_exclusive(class_name, nom_info):
    set_inputs = {}
    interf_inputs = nom_info['inputs']
    for input_name, input_info in interf_inputs.items():
        # print(" " * 2, class_name, input_name)
        n1, n2 = ' '*4 , ' '*(40 - len(input_name))
        def_value = get_default_value(input_info)
        if input_info['type'] != 'Event':
            if "requires" in input_info:
                if input_info['mandatory']:
                    # print(" " * 4, "Mandatory")
                    if "xor" in input_info:
                        if "requires" in input_info:
                            print(class_name, n1, input_name, n2, f"Mandatory Mutually exclusive with: {input_info['xor']}; requires: {input_info['requires']}", n1, def_value)
                        else:
                            print(class_name, n1, input_name, n2, f"Mandatory Mutually exclusive with: {input_info['xor']}", n1, def_value)
                        set_inputs[input_name] = def_value
                elif "xor" in input_info:
                    print(class_name, n1, input_name, n2, f"Optional Mutually exclusive with: {input_info['xor']}", n1, def_value)
                    if "requires" in input_info:
                        print(class_name, n1, input_name, n2, f"Optional Mutually exclusive  with: {input_info['xor']}; requires: {input_info['requires']}", n1, def_value)
                    else:
                        print(class_name, n1, input_name, n2, f"Optional Mutually exclusive  with: {input_info['xor']}", n1, def_value)
                    set_inputs[input_name] = def_value
                else:
                    if "requires" in input_info:
                        print(class_name, n1, input_name, n2, f" # Optional requires: {input_info['requires']}", n1, def_value)
                    else:
                        print(class_name, n1, input_name, n2, f"Optional", n1, def_value)
                    set_inputs[input_name] = def_value

        # print(" " * 10, input_name, input_info['type'], def_value)
    return set_inputs

module = 'workbench'
codeMain = CodeGenerator()
pkg = data[module]
options_dict = {}


for pkg_name, pkg_info in pkg.items():
    print(pkg_name)
    interf = pkg_info['interfaces']
    for interf_name, interf_info in interf.items():
        class_name = module + '_' + interf_name
        options_mod = get_input_mandatory_no_exclusive(class_name, interf_info)
        options_dict[class_name] = options_mod

with open("data_v2.yml", "w", encoding="utf-8") as outfile:
    yaml.dump(
        options_dict,
        outfile,
        Dumper=FlowStyleDumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False
    )
