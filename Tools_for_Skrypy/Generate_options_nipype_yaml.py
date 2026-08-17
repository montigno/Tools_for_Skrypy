import inspect
import sys
import re


# interf = "slicer.registration"
# interf = "fsl"
interf = "mipav"
comment = False

try:
    if sys.argv[1]:
        interf = str(sys.argv[1])
except Exception as err:
    pass


def sort_yaml(data):
    if isinstance(data, dict):
        return {
            key: sort_yaml(data[key])
            for key in sorted(data)
        }

    elif isinstance(data, list):
        return [
            sort_yaml(item)
            for item in data
        ]

    return data

def detectMutuallyExclusive(docstr):
    if 'mutually_exclusive' in docstr:
        return True
    else:
        return False

def initial_values(line):
    br = line[line.index('(') + 1:line.index(')')]
    # print(br)
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
        value_init = 'enumerate((' + value_init + '))'
    elif 'list of items which are a list of items which are' in br:
        gv = get_value(br)
        value_init = "[[" + gv[0] + "]]"
        type_init = "array_" + gv[1]
    elif 'list of items which are' in br:
        gv = get_value(br)
        value_init = "[" + gv[0] + "]"
        type_init = "list_" + gv[1]
    else:
        gv = get_value(br)
        value_init = gv[0]
        type_init = gv[1]
    return value_init, type_init


if '.' in interf:
    print('from nipype.interfaces.{} import {}'.format(interf.split('.')[0], interf.split('.')[1]))
    exec('from nipype.interfaces.{} import {}'.format(interf.split('.')[0], interf.split('.')[1]))
    interf2 = interf.split('.')[1]
else:
    exec('from nipype.interfaces import ' + interf)
    interf2 = interf
lis = inspect.getmembers(eval(interf2), lambda a: not(inspect.isroutine(a)))
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

for elem in dict_cat_fct.keys():
    # print(elem, '#####################################################################')
    dataAll = {}
    doc = ''
    code = ''

    for elemVal in dict_cat_fct[elem]:
        TxtToImport = interf2
        TxtToExecute = elemVal[0:-1]
        if '.' in interf:
            tag = interf.split('.')[0] + "_" + TxtToExecute
        else:
            tag = TxtToImport + "_" + TxtToExecute
        # print(tag)

        try:
            if '.' in interf:
                TxtToImport += "." + elem
            print('try to execute', TxtToImport + "." + TxtToExecute + "().help(True)")
            doc = eval(TxtToImport + "." + TxtToExecute + "().help(True)")
            doc = doc[doc.index('[Optional]'):doc.index('Outputs')]
        except Exception as e:
            doc = ''
            
        if doc:
            code += tag + ':\n'
            descript = ''
            label, comments = None, ''
            list_opt = []

            for ele in doc.split('\n'):
                tmp = ele.strip()
                leading_spaces = len(ele) - len(ele.lstrip())
                # print(tmp, leading_spaces)
                if leading_spaces == 8:
                    key = tmp[:tmp.index(':')]
                    list_opt.append(key)

            for i, opt in enumerate(list_opt):
                try:
                    text = doc[doc.index(" " + list_opt[i]+": ") + len(opt) + 3: doc.index(" " + list_opt[i+1]+": ")].strip()
                    doc = doc[doc.index(" " + list_opt[i+1]+": "):]
                except:
                    text = doc[doc.index(" " + list_opt[i]+": ") + len(opt) + 3: ].strip()
                text = re.sub(r'\s+', ' ', text).strip()
                if text:
                    try:
                        # print(opt, ':', text)
                        # if detectMutuallyExclusive(text):
                        #     print(tag, opt, 'Mutual exclusive')
                        val_init = initial_values(text)
                        # print('values', val_init[0])
                        code += '  ' + opt + ': ' + val_init[0] + '\n'
                    except Exception as err:
                        print("error with", opt, 'in', tag, ":", err, ':', text)

        file = 'Interfaces_' + TxtToImport + '_' + elem + '.yml'
        f = open(file, 'w', encoding='utf8')
        f.write(code)
        f.close()
