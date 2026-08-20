import inspect
import pkgutil
import nipype.interfaces
import importlib
import os
import yaml
import re


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

def detectMutuallyExclusive(docstr):
    if 'mutually_exclusive' in docstr:
        return True
    else:
        return False

def detectMutuallyExclusive2(docstr):
    if 'mutually_exclusive' in docstr:
        return docstr[docstr.index('mutually_exclusive') + 20:]
    return None
    
def initial_values(line, mut_exc):
    br = line[line.index('(') + 1:line.index(')')]
    value_init, type_init = '{}', '{}'

    def get_value(gv):
        value = "''"
        type = 'str'
        if '1 or 0' in br:
            value = '1'
            type = 'int'
        elif '0 or 1' in br:
            value = '0'
            type = 'int'
        elif 'tuple' in br:
            value = '(0,)'
            type = 'tuple'
        elif 'dictionary' in br:
            value = '{}'
            type = 'dict'
        elif 'pathlike' in br:
            value = 'path'
            type = 'None'
        elif 'boolean' in br:
            value = 'True'
            type = 'bool'
        elif 'unicode string' in br:
            value = "''"
            type = 'str'
        elif 'float' in br:
            value = '0.0'
            type = 'float'
        elif 'integer' in br:
            value = '0'
            type = 'int'
        return value, type

    if "’ or ‘" in br or "\' or \'" in  br:
        value_init_tmp = re.findall(r"""["']([^"']*)["']""", br)
        value_init = []
        for vi in value_init_tmp:
            if vi not in value_init:
                value_init.append(vi)
        value_init = "','".join(value_init)
        value_init = 'enumerate((\'' + value_init + '\'))'
    elif 'list of items which are a list of items which are' in br:
        gv = get_value(br)
        value_init = "[[" + gv[0]+ "]]"
        type_init = "list[list[{}]]".format(gv[1])
    elif 'list of items which are' in br:
        gv = get_value(br)
        value_init = "[" + gv[0]+ "]"
        type_init = "list[{}]".format(gv[1])
    else:
        gv = get_value(br)
        value_init = gv[0]
        type_init = gv[1]
    return value_init, type_init, mut_exc

def subtext(lab, src):
    lst = ['Example', 'Inputs::', '[Optional]', 'Outputs::', 'References']
    result = src
    if lab != '':
        lst.remove(lab)
    result = result[result.index(lab):]
    for i in lst:
        try:
            result = result[:result.index(i)]
        except:
            pass
    return result

def tag_values_comments_2(doc):
    # print("txt:", doc)
    list_opt = []
    port = {}

    for ele in doc.split('\n'):
        tmp = ele.strip()
        leading_spaces = len(ele) - len(ele.lstrip())
        if leading_spaces == 8:
            key = tmp[:tmp.index(':')]
            list_opt.append(key)
    # print("    list_opt:", list_opt)

    for i, opt in enumerate(list_opt):
        try:
            text = doc[doc.index(" " + list_opt[i]+": ") + len(opt) + 3: doc.index(" " + list_opt[i+1]+": ")].strip()
            doc = doc[doc.index(" " + list_opt[i+1]+": "):]
        except:
            text = doc[doc.index(" " + list_opt[i]+": ") + len(opt) + 3: ].strip()
        text = re.sub(r'\s+', ' ', text).strip()
        # print("        text:", opt, text)
        if text:
            try:
                val_init = initial_values(text, detectMutuallyExclusive2(text))
                port[opt] = val_init
            except Exception as err:
                print("error with", opt, ":", err, ':', text)

    # print("    port:", port)
    return port

def tag_values_comments(txt):
    descript = ''
    label, comments = None, ''
    port = {}

    for ele in txt.split('\n'):
        tmp = ele.strip()
        leading_spaces = len(ele) - len(ele.lstrip())
        if leading_spaces == 8:
            if label:
                val_init = initial_values(comments, detectMutuallyExclusive2(comments))
                port[label] = val_init
            if tmp:    
                label = tmp[0:tmp.index(':')]
                comments = ' #' + tmp[tmp.index(':') + 1:]
        elif leading_spaces != 0:
            comments += ' ' + tmp
    return port


for module in pkgutil.iter_modules(nipype.interfaces.__path__):
    print(module.name)

    module_nipype = module.name
    out_path = os.path.expanduser('Nipype')
    
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    module_name = "nipype.interfaces." + module_nipype
    module = importlib.import_module(module_name)

    codeMain = CodeGenerator()
    codeYaml = ''


    for name, obj in inspect.getmembers(module, inspect.isclass):
        # print(name, obj.__module__)
        list_mut_exc = {}
        name_class = module_nipype + "_" + name
        mod_class = obj.__module__
        # print(mod_class, ',', name, ",", name_class)
    
        try:
            exec('from {} import {}'.format(mod_class, name))
        except:
            print("error with exec")
        
        try:
            doc = eval(name + "().help(True)")
        except:
            doc = None
        if doc:
            codeMain += 'class ' + name_class + ":\n"
            codeMain.indent()
            codeMain += '\"\"\"\n'
            codeMain += 'Note:\n'
            codeMain.indent()
            codeMain += 'dependencies: Nipype,' + module_nipype + '\n'
            codeMain += 'GUI: no\n'
            codeMain += 'link_web: (click Ctrl + U)\n'
            codeMain.dedent()
            codeMain += '\"\"\"\n'

            try:
                mod_inputs = doc[doc.index('[Mandatory]'):doc.index('[Optional]')]
                mod_inputs = tag_values_comments(mod_inputs)
            except:
                mod_inputs = None
            text_inputs = "def __init__(self"
            if mod_inputs:
                for kin, vin in mod_inputs.items():
                    if not vin[2]: # mutually exclusive ?
                        text_inputs += ', ' + kin + '=' + vin[0]
                    else:
                        list_mut_exc[kin] = vin
                list_mut_exc = dict(sorted(list_mut_exc.items()))
            codeMain += text_inputs + ', **options):\n'
            codeMain.indent()
            codeMain += 'from {} import {}\n'.format(mod_class, name)
            codeMain += 'at = ' + name + '()\n'
            if mod_inputs:
                for kin, vin in mod_inputs.items():
                    if not vin[2]: # mutually exclusive ?
                        codeMain += 'at.inputs.{} = {}\n'.format(kin, kin)
            _opt = 'for ef in options:\n'
            codeMain += _opt
            codeMain.indent()
            _opt = 'setattr(at.inputs, ef, options[ef])\n'
            codeMain += _opt
            codeMain.dedent()
            _opt = 'self.res = at.run()\n'
            codeMain += _opt
            codeMain.dedent()
            codeMain.dedent()
            codeMain += '\n'
    
            try:
                mod_outputs = subtext('Outputs::', doc) + '\n' + ' ' * 8
                mod_outputs = mod_outputs[mod_outputs.index('\n')+1:]
                mod_outputs = tag_values_comments(mod_outputs)
            except:
                mod_outputs = None
            if mod_outputs:
                for kin, vin in mod_outputs.items():
                    codeMain.indent()
                    text_outputs = 'def {}(self) -> {}:\n'.format(kin, vin[1])
                    codeMain += text_outputs
                    codeMain.indent()
                    text_outputs = 'return self.res.outputs.{}\n\n'.format(kin)
                    codeMain += text_outputs
                    codeMain.dedent()
                    codeMain.dedent()
                    codeMain.dedent()
            codeMain += '#' * 79
            codeMain += '\n\n\n'
    
            try:
                mod_options = doc[doc.index('[Optional]'):doc.index('Outputs')]
                mod_options = tag_values_comments_2(mod_options)
            except Exception as e:
                mod_options = None
            if mod_options:
                codeYaml += name_class + ':\n'
                for kin, vin in list_mut_exc.items():
                    codeYaml += '  ' + kin + ': ' + vin[0] + ' # Mandatory Mutually exclusive with: ' + vin[2] + '\n'
                mod_options = dict(sorted(mod_options.items()))
                for kin, vin in mod_options.items():
                    if kin == 'output_file' or kin == 'output_image':
                        val = 'path'
                    else:
                        val = vin[0]

                    if vin[2]:
                        codeYaml += '  ' + kin + ': ' + val + ' # Optional Mutually exclusive with: ' + vin[2] + '\n'
                    else:
                        codeYaml += '  ' + kin + ': ' + val + '\n'

    if str(codeMain):
        file = os.path.join(out_path, 'Interfaces_' + module_nipype + '.py')
        f = open(file, 'w',  encoding='utf8')
        os.chmod(file, 0o777)
        f.write(str(codeMain))
        f.close()
        print(" " * 10 + "saved in", file)

    if codeYaml:
        file = os.path.join(out_path, 'Interfaces_' + module_nipype + '.yml')
        f = open(file, 'w',  encoding='utf8')
        os.chmod(file, 0o777)
        f.write(str(codeYaml))
        f.close()
        print(" " * 10 + "saved in", file)
