import os
import yaml
import subprocess
import re

file_config = "../config.yml"

with open(file_config) as stream:
    data_loaded = yaml.safe_load(stream)
    
# print(data_loaded['packages'])

for ke, va in data_loaded['packages'].items():
    if '==' in va:
        pack = va[:va.index('==')]
    else:
        pack = va
    sp = subprocess.run(["pip3", "show", str(pack)], capture_output=True)
    ver = sp.stdout.decode('utf-8').strip().split('\n')
    if len(ver) == 1:
        version = 'unknow'
        summ = 'no comment'
    else:
        res = re.search('^Version:\ (.*)$', ver[1])
        # print(res)
        version = res.group(1)
        res = re.search('^Summary:\ (.*)$', ver[2])
        # print(res)
        summ = res.group(1)
    print('   "{}", {}, "{}"'.format(pack, version, summ))
