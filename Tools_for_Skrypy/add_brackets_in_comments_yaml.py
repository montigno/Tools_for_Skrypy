import re

module = 'dipy'

input_file = "/home/olivier/Documents/eclipse-workspace-2026/skrypy-pyqt5/NodeEditor/modules/Nipype/Interfaces_{}.yml".format(module)
output_file = "nipype_modules_modified.yaml"


def convert_comment(line):
    """
    Transforme :

    # Optional Mutually exclusive with: a, b, c
    # Mandatory Mutually exclusive with: a, b, c

    en :

    # Optional Mutually exclusive with: [a, b, c]
    # Mandatory Mutually exclusive with: [a, b, c]
    """

    pattern = (
        r"(#\s*(?:Optional|Mandatory)\s+"
        r"Mutually exclusive with:\s*)"
        r"(.+?)"
        r"(\r?\n?)$"
    )

    match = re.search(pattern, line)

    if not match:
        return line

    prefix = match.group(1)
    values = match.group(2).strip()
    newline = match.group(3)

    # Ne rien faire si les crochets sont déjà présents
    if values.startswith("[") and values.endswith("]"):
        return line

    return line[:match.start()] + f"{prefix}[{values}]{newline}"


with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()


lines = [convert_comment(line) for line in lines]


with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(lines)


print(f"Fichier créé : {output_file}")