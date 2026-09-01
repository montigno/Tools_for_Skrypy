import subprocess
import shutil
import re
import yaml
from pathlib import Path


def remove_backspaces(text: str) -> str:
    """Reconstruit correctement le texte contenant des backspaces."""
    result = []
    for char in text:
        if char == "\x08":  # backspace
            if result:
                result.pop()
        else:
            result.append(char)
    return "".join(result)


def get_arguments(text: str) -> str:

    arguments = {}

    if "DESCRIPTION" in text:
        end_field = "DESCRIPTION"
    elif "EXAMPLE USAGES" in text:
        end_field = "EXAMPLE USAGES"
    else:
        end_field = "OPTIONS"

    sub_text = text[text.find("USAGE"):text.find(end_field)]  
    text_tmp = repr(sub_text)
    list_args = text_tmp.split("\\n\\n     ")
    for ele in list_args[2:]:
        tmp = ele.strip()
        arg = tmp.split(" ")[0]
        tmp = tmp[tmp.find(" "):].strip()
        tmp = tmp.replace("\\n", "")
        com = re.sub(r'\s+', ' ', tmp)
        arguments[arg] = com

    print(f"Argument: {arguments}\n")

    return arguments


def get_options(text: str) -> str:

    options = {}
    comments = []
    
    sub_text = text[text.find("USAGE"):text.find("AUTHOR")]
    resultat = "\n".join(
        ligne for ligne in sub_text.splitlines()
            if ligne.startswith(" ")
)

    # Expression régulière pour capturer l'argument (qui commence par un '-')
    # et la description qui suit.
    pattern = re.compile(r'^\s*(-\S+.*?)\n\s*(.*?)(?=\n\s*-|\Z)', re.DOTALL | re.MULTILINE)
    
    # Recherche de toutes les correspondances dans le texte
    matches = pattern.findall(resultat)
    
    # Afficher les résultats
    for match in matches:
        opt = match[0].strip()
        opt = opt.split(" ")[0][1:]
        commentaire = match[1].strip()  # Supprimer les espaces avant/après le commentaire
        commentaire = re.sub(r'\n\s+', ' ', commentaire)  # Remplacer les retours à la ligne par un espace
        options[opt] = commentaire
        
    print(f"Options: {options}\n")
    
    return options


def get_command_help(command: str, help_flags=None) -> str:
    """
    Récupère le help d'une commande CLI et nettoie les artefacts de terminal.
    """
    if help_flags is None:
        help_flags = ["-help", "--help", "-h"]

    # Vérifie que la commande existe dans le PATH
    if shutil.which(command) is None:
        raise FileNotFoundError(f"Commande introuvable dans le PATH: {command}")

    for flag in help_flags:
        try:
            result = subprocess.run(
                [command, flag],
                capture_output=True,
                text=True,
                timeout=20
            )

            output = result.stdout or result.stderr
            if output:
                return remove_backspaces(output)

        except Exception:
            continue

    raise RuntimeError(f"Impossible de récupérer le help pour {command}")


def save_help(command: str):
    """
    Sauvegarde le help nettoyé dans un fichier texte.
    """

    help_text = get_command_help(command)
    
    print(command)
    get_arguments(help_text)
    option_list = get_options(help_text)

    return option_list


def main():

    list_mrtrix_command = "list_command_mrtrix3.txt"
    output_dir="options_output"
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    file_path = output_path / f"mrtrix_options.txt"


    with open(list_mrtrix_command, "r") as f:
        list_mrtrx = f.read()

    # file_path.write_text(help_text, encoding="utf-8")
    # print(f"Help sauvegardé dans : {file_path}")
    
        for ls in list_mrtrx.split():
            try:
                with open("mon_fichier.txt", "a", encoding="utf-8") as f:
                    data = save_help(ls)
                    f.write(f"{ls}:\n")
                    for cle, valeur in data.items():
                        f.write(f"  {cle}: '' # {valeur}\n")
            except Exception as e:
                print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
