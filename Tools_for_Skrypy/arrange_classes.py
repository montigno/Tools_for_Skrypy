import ast
import os


# ============================================================
# Formatage de la signature __init__
# ============================================================

def format_init_signature(line, indent_spaces=17):

    result = []

    quote = None
    escape = False

    parentheses = 0
    brackets = 0
    braces = 0

    i = 0

    while i < len(line):

        char = line[i]

        # ----------------------------------------------------
        # Caractère échappé
        # ----------------------------------------------------

        if escape:
            result.append(char)
            escape = False
            i += 1
            continue

        if char == "\\" and quote is not None:
            result.append(char)
            escape = True
            i += 1
            continue

        # ----------------------------------------------------
        # Chaîne de caractères
        # ----------------------------------------------------

        if quote is not None:

            result.append(char)

            if char == quote:
                quote = None

            i += 1
            continue

        if char in ("'", '"'):
            quote = char
            result.append(char)
            i += 1
            continue

        # ----------------------------------------------------
        # Parenthèses
        # ----------------------------------------------------

        if char == "(":
            parentheses += 1
            result.append(char)
            i += 1
            continue

        if char == ")":

            parentheses -= 1
            result.append(char)

            # Fin de __init__(...)
            if parentheses == 0:

                if i + 1 < len(line) and line[i + 1] == ":":

                    result.append(":")
                    result.append("\n\n")

                    i += 2

                    # Supprime espaces et retours à la ligne
                    while i < len(line) and line[i] in " \t\n":
                        i += 1

                    continue

            i += 1
            continue

        # ----------------------------------------------------
        # Crochets
        # ----------------------------------------------------

        if char == "[":
            brackets += 1
            result.append(char)
            i += 1
            continue

        if char == "]":
            brackets -= 1
            result.append(char)
            i += 1
            continue

        # ----------------------------------------------------
        # Accolades
        # ----------------------------------------------------

        if char == "{":
            braces += 1
            result.append(char)
            i += 1
            continue

        if char == "}":
            braces -= 1
            result.append(char)
            i += 1
            continue

        # ----------------------------------------------------
        # Virgule séparant les arguments principaux
        # ----------------------------------------------------

        if (
            char == ","
            and parentheses == 1
            and brackets == 0
            and braces == 0
        ):

            result.append(",")
            result.append("\n")
            result.append(" " * indent_spaces)

            i += 1

            while i < len(line) and line[i] in (" ", "\t"):
                i += 1

            continue

        result.append(char)
        i += 1

    return "".join(result)


# ============================================================
# Lecture du fichier
# ============================================================


# list_files = ["drazft.py"]

list_files = ["Keras.py",
                "Monai.py",
                "RS2.py",
                "Tensorflow.py"]

rep = "/home/olivier/Documents/eclipse-workspace-2026/skrypy-pyqt5/NodeEditor/modules/DeepLearn/"


for fls in list_files:

    file_txt = os.path.join(rep, fls)
    with open(file_txt, "r", encoding="utf-8") as f:
        source = f.read()
    
    
    # ============================================================
    # Analyse avec AST
    # ============================================================
    
    tree = ast.parse(source)
    
    
    # ============================================================
    # Déterminer les classes sans docstring
    # ============================================================
    
    classes_without_docstring = []
    
    for node in ast.walk(tree):
    
        if isinstance(node, ast.ClassDef):
    
            has_docstring = (
                len(node.body) > 0
                and isinstance(node.body[0], ast.Expr)
                and isinstance(node.body[0].value, ast.Constant)
                and isinstance(node.body[0].value.value, str)
            )
    
            if not has_docstring:
                classes_without_docstring.append(node)
    
    
    # ============================================================
    # Modification du texte
    # ============================================================
    
    lines = source.splitlines(keepends=True)
    
    # ------------------------------------------------------------
    # Ajouter les docstrings manquantes
    # ------------------------------------------------------------
    
    # On travaille de bas en haut pour ne pas modifier
    # les numéros de lignes des classes suivantes.
    for node in sorted(
        classes_without_docstring,
        key=lambda x: x.lineno,
        reverse=True
    ):
    
        # Indentation de la classe
        class_line = lines[node.lineno - 1]
    
        indent = class_line[:len(class_line) - len(class_line.lstrip())]
    
        docstring = (
            indent
            + '    """\n'
            + indent
            + "    docstring to be completed\n"
            + indent
            + '    """\n'
        )
    
        # Insérer juste après la ligne "class ..."
        lines.insert(node.lineno, docstring)
    
    
    # Reconstituer le fichier
    source = "".join(lines)
    
    
    # ============================================================
    # Reformater les __init__
    # ============================================================
    
    lines = source.splitlines(keepends=True)
    
    new_lines = []
    
    for line in lines:
    
        if "__init__" in line and "def " in line and "):" in line:
    
            line = format_init_signature(
                line,
                indent_spaces=17
            )
    
        new_lines.append(line)
    
    
    # ============================================================
    # Écriture du fichier
    # ============================================================
    
    with open(file_txt, "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    
    
    print(f"Fichier modifié : {file_txt}")
