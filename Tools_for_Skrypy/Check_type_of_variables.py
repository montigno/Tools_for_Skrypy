import yaml


pathYml = 'Check_type_of_variables.yml'

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

def regularPath(path):
    result = all(x == path[0] for x in path)
    return 'yes' if result else 'no'   


print('tag', ' '*(20 - 3), 'type', ' '*(20 - 4), 'regular ?', ' '*(15-9), 'size', ' '*(10-4), 'value')
print()

for lk, lv in val.items():
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

    print(lk, ' '*(20 - len(lk)), '{}{}'.format(type_list, type_var), ' '*(20 - len(type_list + type_var)), regular, ' '*(15-len(regular)), length, ' '*(10-len(str(length))), lv)
    print()