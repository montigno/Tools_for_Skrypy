import ast
import yaml

with open("nipype_modules.yaml", "r", encoding="utf-8") as f:

    contenu = f.read()

print("CONTENU DU FICHIER :")
print(contenu)

data = yaml.safe_load(contenu)

print("\nVALEUR LUE :")
print(data["ants_Registration"]["transform_parameters"])

print("\nTYPE :")
print(type(data["ants_Registration"]["transform_parameters"]))


value = data["ants_Registration"]["transform_parameters"]

if "['(" in str(value) and (("'),") in str(value) or ")']" in str(value)):
    print('list of Tuple')
    imb = str(value).replace("'", "")
    print(imb, type(ast.literal_eval(imb)).__name__)
    imb = ast.literal_eval(imb)
    print(imb[0], type(imb[0]).__name__)