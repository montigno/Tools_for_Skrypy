import inspect
import sys


interf = 'fsl'
comment = False

try:
    if sys.argv[1]:
        interf = str(sys.argv[1])
except Exception as err:
    pass


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

for elem in dict_cat_fct.keys():
    # print(elem, '#####################################################################')
    dataAll = {}
    doc = ''
    code = ''

    for elemVal in dict_cat_fct[elem]:
        TxtToExecute = elemVal[0:-1]
        tag = TxtToImport + "_" + TxtToExecute

        try:
            doc = eval(TxtToImport + "." + TxtToExecute + "().help(True)")
            doc = doc[doc.index('[Optional]'):doc.index('Outputs')]
        except Exception as e:
            doc = ''

        if doc:
            code += tag + ':\n'
            descript = ''
            label, comments = None, ''

            for ele in doc.split('\n'):
                tmp = ele.strip()
                leading_spaces = len(ele) - len(ele.lstrip())
                if leading_spaces == 8:
                    # if TxtToExecute == 'BinaryMaths':
                    #     print(tmp,leading_spaces)
                    if label:
                        val_init = initial_values(comments)
                        if comment:
                            code += '  ' + label + ': ' + val_init[0] + comments + '\n'
                        else:
                            code += '  ' + label + ': ' + val_init[0] + '\n'
                        # print(label, comments)
                    label = tmp[0:tmp.index(':')]
                    comments = ' #' + tmp[tmp.index(':') + 1:]
                elif leading_spaces != 0:
                    comments += ' ' + tmp

        file = 'Interfaces_' + TxtToImport + '_' + elem + '.yml'
        f = open(file, 'w', encoding='utf8')
        f.write(code)
        f.close()
