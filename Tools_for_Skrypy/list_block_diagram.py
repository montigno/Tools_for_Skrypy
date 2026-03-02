class GetValueInBrackets():

    def __init__(self, line, args):
        self.res = []
        line = line.rstrip()
        for i in range(len(args)-1):
            tmp = ''
            try:
                tmp = line[line.index(args[i]+'=') +
                           len(args[i])+1:line.index(args[i+1]+'=')-1][1:-1]
            except Exception as e:
                try:
                    tmp = line[line.index(args[i]+'=') +
                               len(args[i]) +
                               1:line.index(args[i+2]+'=')-1][1:-1]
                except Exception as e:
                    pass
            self.res.append(tmp)
        self.res.append(line[line.index(args[-1]+'=')+len(args[-1])+1:][1:-1])

    def getValues(self):
        return self.res


# diagram_file = "/home/montigon/Apps/mri_works_venv/main/NodeEditor/submodules/EL/EL_skull_stripping.mod"
diagram_file = '/home/olivier/Documents/skrypy_projects/IRMf_VCoizet/2c-EPI_registration.dgr'

with open(diagram_file) as f:
    txt = f.readlines()
    for line in txt:
        if line[0:5] == 'block' and 'RectF' in line:
            args = ["block", "category", "class", "valInputs", "RectF"]
            unit, cat, classs, Vinput, pos = GetValueInBrackets(line, args).getValues()
            print(cat, '-', classs, ':', Vinput)
