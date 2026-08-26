import yaml

module = 'mipav'

fichier1_yaml = "/home/olivier/Documents/eclipse-workspace-2026/skrypy-pyqt5/NodeEditor/modules/Nipype/Interfaces_{}.yml".format(module)
fichier2_yaml = "data_v2.yml".format(module)

with open(fichier1_yaml, "r", encoding="utf-8") as f:
    yaml1 = yaml.safe_load(f)

with open(fichier2_yaml, "r", encoding="utf-8") as f:
    yaml2 = yaml.safe_load(f)


def compare(a, b, path=""):
    if isinstance(a, dict) and isinstance(b, dict):
        keys = sorted(set(a) | set(b))

        for key in keys:
            # print("key=", key)
            current_path = f"{path}.{key}" if path else str(key)

            if key not in a:
                print(f"+ {current_path} = {b[key]}")
            elif key not in b:
                print(f"- {current_path} = {a[key]}")
            else:
                compare(a[key], b[key], current_path)

    elif isinstance(a, list) and isinstance(b, list):
        if a != b:
            print(f"~ {path}")
            print(f"    fichier1 : {a}")
            print(f"    fichier2 : {b}")

    elif a != b:
        print(f"~ {path}")
        print(f"    fichier1 : {a}")
        print(f"    fichier2 : {b}")


compare(yaml1, yaml2)

print("end of comparaison")