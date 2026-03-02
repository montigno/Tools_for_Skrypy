import yaml
import typing
from pathlib import Path
import numpy as np

pathYml = 'example_Yaml_for_Skrypy.yml'

with open(pathYml, 'r', encoding='utf8') as stream:
    dicts = yaml.load(stream, yaml.FullLoader)

val = dicts['Module']

print(val)
print()

def regularList(lst):
    result = all(type(x).__name__ == type(lst[0]).__name__ for x in lst)
    return 'yes' if result else 'no'

def regularArray(arr):
    result = all(type(y).__name__ == type(arr[0][0]).__name__ and len(x) == len(arr[0]) for x in arr for y in x)
    return 'yes' if result else 'no'

def get_var_type(lv):

    regular = 'yes'
    element_var = lv
    type_list = ''
    length = 1
    if isinstance(lv, list):
        element_var = lv[0]
        type_list = 'list_'
        if isinstance(element_var, list):
            type_list = 'array_'
            element_var = element_var[0]
            regular = regularArray(lv)
            length = (len(lv), len(lv[0]))
        else:
            regular = regularList(lv)
            length = (len(lv),)
    type_var = type(element_var).__name__

    # print(lk, ' '*(20 - len(lk)), '{}{}'.format(type_list, type_var), ' '*(20 - len(type_list + type_var)), regular, ' '*(15-len(regular)), length, ' '*(10-len(str(length))), lv)

    if type_var == 'str':
        if  lv == 'path':
            type_var = 'path'
        elif 'list' in type_list:
            if lv[0] == 'path':
                type_var = 'path'
        elif 'array' in type_list:
            if lv[0][0] == 'path':
                type_var = 'path'
        else:
            try:
                type_var = type(eval(element_var)).__name__
            except Exception as err:
                pass
            if type_var == 'tuple':
                length = (len(lv),)
            if type_var not in ['tuple', 'enumerate']:
                type_var = 'str'
            if type_var == 'enumerate':
                type_list = 'enumerate_'
                lv = list(eval(lv))
                lv = [x[1] for x in lv]
                regular = regularList(lv)
                type_var = type(lv[0]).__name__
                length = (len(lv),)
            if regular == 'no':
                type_var = 'various'

    return type_list+type_var

def isPath(varble):
    if type(varble).__name__ == 'str':
        if 'path' in varble:
            return 'path'
        else:
            return type(varble).__name__
    else:
        return type(varble).__name__


for lk, lv in val.items():
    print('method1:', lk, get_var_type(lv))
    print()
