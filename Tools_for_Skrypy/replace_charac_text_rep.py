import os
from pathlib import Path

def remplacer_chaine_dans_fichiers_repertoire(repertoire_path: str, ancienne_chaine: str, nouvelle_chaine: str):
    """
    Ouvre tous les fichiers texte dans un répertoire donné, remplace toutes les occurrences de 'ancienne_chaine' 
    par 'nouvelle_chaine' dans chaque fichier, et sauvegarde les modifications dans les mêmes fichiers.

    :param repertoire_path: Le chemin du répertoire contenant les fichiers texte
    :param ancienne_chaine: La chaîne à remplacer
    :param nouvelle_chaine: La chaîne de remplacement
    """
    # Convertir le chemin du répertoire en objet Path
    repertoire = Path(repertoire_path)

    # Vérifier si le répertoire existe
    if not repertoire.exists() or not repertoire.is_dir():
        print(f"Erreur : le répertoire '{repertoire_path}' n'existe pas ou n'est pas un répertoire.")
        return

    # Parcourir tous les fichiers dans le répertoire
    for fichier in repertoire.glob('*.py'):  # Cherche tous les fichiers .txt
        try:
            # Ouvrir le fichier en mode lecture
            with open(fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()

            # Remplacer toutes les occurrences de l'ancienne chaîne par la nouvelle chaîne
            contenu_modifie = contenu.replace(ancienne_chaine, nouvelle_chaine)

            # Sauvegarder les modifications dans le même fichier
            with open(fichier, 'w', encoding='utf-8') as f:
                f.write(contenu_modifie)

            print(f"Les occurrences de '{ancienne_chaine}' ont été remplacées par '{nouvelle_chaine}' dans le fichier '{fichier}'.")

        except Exception as e:
            print(f"Erreur lors du traitement du fichier '{fichier}': {e}")


# Exemple d'utilisation
repertoire_path = '/home/olivier/Documents/eclipse-workspace/skrypy2-pyqt6/NodeEditor/modules'  # Remplacez par le chemin réel de votre répertoire

list_chaine = [[': \'int\')'        , ') -> int'],
               [': \'float\')'      , ') -> float'],
               [': \'str\')'        , ') -> str'],
               [': \'bool\')'       , ') -> bool'],
               [': \'path\')'       , ') -> None'],
               [': \'list_int\')'   , ') -> list[int]'],
               [': \'list_float\')' , ') -> list[float]'],
               [': \'list_str\')'   , ') -> list[str]'],
               [': \'list_bool\')'  , ') -> list[bool]'],
               [': \'list_path\')'  , ') -> list[None]'],
               [': \'array_int\')'  , ') -> list[list[int]]'],
               [': \'array_float\')', ') -> list[list[float]]'],
               [': \'array_str\')'  , ') -> list[list[str]]'],
               [': \'array_bool\')' , ') -> list[list[bool]]'],
               [': \'array_path\')' , ') -> list[list[None]]'],
               [': \'tuple_str\')'  , ') -> tuple(str)'],
               [': \'tuple_int\')'  , ') -> tuple(int)'],
               [': \'dict\')'       , ') -> dict']
               ]

chemin_repertoire = Path(repertoire_path)
repertoires = [dossier.name for dossier in chemin_repertoire.iterdir() if dossier.is_dir()]

print(repertoires)

for rep in repertoires:
    for old, new in list_chaine:
        rep_path = os.path.join(chemin_repertoire, rep)
        print(rep_path)
        remplacer_chaine_dans_fichiers_repertoire(rep_path, old, new)






