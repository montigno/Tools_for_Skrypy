from os import listdir
from os.path import isfile, join


name_block = "Non_linear_registration_for_Atlases"

# dir_diagrams = "/home/olivier/Documents/skrypy_dvt"
# dir_diagrams = "/home/olivier/Documents/skrypy_projects/"
# dir_diagrams = "/home/olivier/Bureau/"
dir_diagrams = "/home/olivier/Applications/skrypy_venv_312/skrypy/NodeEditor/examples"

# dir_submodules = "/home/olivier/Documents/eclipse-workspace/skrypy/NodeEditor/submodules"
# dir_submodules = "/home/olivier/Applications/skrypy_venv_312/skrypy/NodeEditor/submodules"
dir_submodules = "/home/olivier/.skrypy/submodules"



def search_block(file_path, word):
    with open(file_path, 'r') as d:
        content = d.read()
        if word in content:
            print(word, "found in", file_path)


folders = [join(dir_diagrams, d) for d in listdir(dir_diagrams) if not isfile(join(dir_diagrams, d))]
folders.append(dir_diagrams)
print('folders', folders)
print()

for direct in folders:
    onlyfiles = [join(direct, f) for f in listdir(direct) if isfile(join(direct, f))]
    for files_d in onlyfiles:
        if files_d.endswith('.dgr'):
            # print(files_d)
            search_block(files_d, name_block)

print('\n' + '*'*20 + ' end ' + '*'*20 + "\n")

folders = [join(dir_submodules, d) for d in listdir(dir_submodules) if not isfile(join(dir_submodules, d))]

for direct in folders:
    onlyfiles = [join(direct, f) for f in listdir(direct) if isfile(join(direct, f))]
    for files_d in onlyfiles:
        if files_d.endswith('.mod'):
            # print(files_d)
            search_block(files_d, name_block)

print('\n' + '*'*20 + ' end ' + '*'*20 + "\n")
