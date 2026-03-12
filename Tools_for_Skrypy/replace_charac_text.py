def remplacer_chaine_dans_fichier(fichier_path: str, ancienne_chaine: str, nouvelle_chaine: str, fichier_sortie: str = None):
    """
    Ouvre un fichier texte, remplace toutes les occurrences de 'ancienne_chaine' par 'nouvelle_chaine',
    puis enregistre les modifications dans un nouveau fichier (ou le même fichier).

    :param fichier_path: Le chemin du fichier à traiter
    :param ancienne_chaine: La chaîne à remplacer
    :param nouvelle_chaine: La chaîne de remplacement
    :param fichier_sortie: Le chemin du fichier où sauvegarder le texte modifié (par défaut, on remplace dans le fichier d'origine)
    """
    try:
        # Ouvrir le fichier en mode lecture
        with open(fichier_path, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()

        # Remplacer toutes les occurrences de l'ancienne chaîne par la nouvelle chaîne
        contenu_modifie = contenu.replace(ancienne_chaine, nouvelle_chaine)

        # Si aucun fichier de sortie n'est précisé, on remplace dans le même fichier
        if fichier_sortie is None:
            fichier_sortie = fichier_path

        # Ouvrir (ou créer) le fichier de sortie en mode écriture et y sauvegarder le contenu modifié
        with open(fichier_sortie, 'w', encoding='utf-8') as fichier:
            fichier.write(contenu_modifie)

        print(f"Les occurrences de '{ancienne_chaine}' ont été remplacées par '{nouvelle_chaine}' dans le fichier '{fichier_sortie}'.")

    except FileNotFoundError:
        print(f"Erreur : le fichier '{fichier_path}' n'a pas été trouvé.")
    except IOError as e:
        print(f"Erreur d'entrée/sortie : {e}")

# Exemple d'utilisation
fichier_path = '/home/honorom/Documents/eclipse-workspace/skrypy2/NodeEditor/modules/Demos/Models.py'  # Remplacez par le chemin réel de votre fichier

# remplacer_chaine_dans_fichier(fichier_path, old, new)
    
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

for old, new in list_chaine:
    print(old, new)
    remplacer_chaine_dans_fichier(fichier_path, old, new)



