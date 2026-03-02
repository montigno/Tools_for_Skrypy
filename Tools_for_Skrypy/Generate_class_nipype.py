import inspect
import os
import sys


interf = 'fsl'

try:
    if sys.argv[1]:
        interf = str(sys.argv[1])
except Exception as err:
    pass


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

def initial_values(line):
    br = line[line.index('(') + 1:line.index(')')]
    # print(br)
    value_init, type_init = '{}', '{}'

    def get_value(gv):
        value = "''"
        type = 'str'
        if 'tuple' in br:
            value = '(0,)'
            type = 'tuple'
        elif 'dictionary' in br:
            value = '{}'
            type = 'dict'
        elif 'pathlike object' in br:
            value = "'path'"
            type = 'path'
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

    if "\' or \'" in br:
        if ',' in br:
            # print('sub', br)
            # br = br[br.index(','):]
            br = br[0: br.index(',')]
        br = br[br.index("'"):]
        value_init = br.split(" or ")
        value_init = ','.join(value_init)
        value_init = '"enumerate((' + value_init + '))"'
    elif 'list of items which are a list of items which are' in br:
        gv = get_value(br)
        value_init = "[[" + gv[0]+ "]]"
        type_init = "array_" + gv[1]
    elif 'list of items which are' in br:
        gv = get_value(br)
        value_init = "[" + gv[0]+ "]"
        type_init = "list_" + gv[1]
    else:
        gv = get_value(br)
        value_init = gv[0]
        type_init = gv[1]
    return value_init, type_init

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

def tag_values_comments(txt, rep):
    descript = ''
    label, comments = None, ''
    port = {}
    # print(rep, txt)

    for ele in txt.split('\n'):
        tmp = ele.strip()
        leading_spaces = len(ele) - len(ele.lstrip())
        # print(rep, ele, leading_spaces)

        if leading_spaces == 8:
            # if TxtToExecute == 'BinaryMaths':
            # print(tmp,leading_spaces, rep)
            if label:
                val_init = initial_values(comments)
                # print(label, val_init)
                port[label] = val_init
                # print(rep, port)
            if tmp:    
                label = tmp[0:tmp.index(':')]
                comments = ' #' + tmp[tmp.index(':') + 1:]
                # print(rep, label)
        elif leading_spaces != 0:
            comments += ' ' + tmp
    
    return port

exec('from nipype.interfaces import ' + interf)
lis = inspect.getmembers(eval(interf), lambda a: not(inspect.isroutine(a)))
list_cat = []
list_fct = []
dict_cat_fct = {}
code = ''

for nameClass in lis:
    try:
        if '__' not in nameClass[0]:
            fct = nameClass[0]
            txt = str(nameClass[1])
            cat = 'type' in str(type(nameClass[1]))
            if cat:
                txt = txt[txt.index(interf) + len(interf) + 1:-1]
                txt1 = txt[0:txt.index('.')]
                txt2 = txt[txt.index('.'):]
                txt2 = txt2[txt2.index('.') + 1:]
                if txt1 in dict_cat_fct.keys():
                    list_fct = dict_cat_fct[txt1]
                else:
                    list_fct = []
                if txt2 not in list_fct:
                    list_fct.append(txt2)
                    dict_cat_fct[txt1] = list_fct
    except Exception as e:
        pass

TxtToImport = interf

codeMain = CodeGenerator()

for elem in dict_cat_fct.keys():
    # print(elem, '#####################################################################')
    dataAll = {}
    doc = ''
    code = ''

    for elemVal in dict_cat_fct[elem]:
        TxtToExecute = elemVal[0:-1]
        tag = TxtToImport + "_" + TxtToExecute
        # print('\n' + tag)
        codeMain += 'class ' + tag + ":\n"
        codeMain.indent()
        codeMain += '\"\"\"\n'
        codeMain += 'Note:\n'
        codeMain.indent()
        codeMain += 'dependencies: Nipype,' + TxtToImport + '\n'
        codeMain += 'GUI: no\n'
        codeMain += 'link_web: (click Ctrl + U)\n'
        codeMain.dedent()
        codeMain += '\"\"\"\n'
        # inputs = {}

        try:
            doc = eval(TxtToImport + "." + TxtToExecute + "().help(True)")
            clss = doc[doc.index('[Mandatory]'):doc.index('[Optional]')]
            # clss = subtext('[Mandatory]', doc)
            outp = subtext('Outputs::', doc) + '\n' + ' ' * 8
            # outp = outp[outp.index('\n')+1: ]
            outp = outp[outp.index('\n')+1:]
        except Exception as e:
            clss = ''


###############################################################################

        if clss:
            code += tag + ':\n'
            inputs = tag_values_comments(clss, 'inputs')

        text_inputs = "def __init__(self"
        for kin, vin in inputs.items():
            text_inputs += ', ' + kin + '=' + vin[0]
        codeMain += text_inputs + ', **options):\n'
        codeMain.indent()
        codeMain += 'from nipype.interfaces.{} import {}\n'.format(TxtToImport, TxtToExecute)
        codeMain += 'at = ' + TxtToExecute + '()\n'
        # codeMain.dedent()
        # codeMain.dedent()
        for kin in inputs.keys():
            codeMain += 'at.inputs.{} = {}\n'.format(kin, kin)
        # codeMain.indent()
        # codeMain.indent()
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

###############################################################################

        if outp:
            outputs = tag_values_comments(outp, 'outputs')

        for kin, vin in outputs.items():
            print(kin, vin)
            codeMain.indent()
            text_outputs = 'def {}(self: \"{}\"):\n'.format(kin, vin[1])
            codeMain += text_outputs
            codeMain.indent()
            text_outputs = 'return self.res.outputs.{}\n\n'.format(kin)
            codeMain += text_outputs
            codeMain.dedent()
            codeMain.dedent()
        codeMain += '\n'

###############################################################################


# print(codeMain)
file = TxtToImport + '.py'
f = open(file, 'w',  encoding='utf8')
os.chmod(file, 0o777)
f.write(str(codeMain))
f.close()
