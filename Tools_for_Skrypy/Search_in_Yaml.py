from pathlib import Path
import yaml


def lire_valeur_yaml(fichier_yaml, chemin):
    """
    Charge un fichier YAML et retourne la valeur correspondant
    au chemin de clés fourni.

    Parameters
    ----------
    fichier_yaml : str ou Path
        Chemin vers le fichier YAML.

    chemin : list
        Liste des clés successives.

    Returns
    -------
    object
        Valeur trouvée dans le YAML.
    """

    fichier_yaml = Path(fichier_yaml)

    # Vérification du fichier
    if not fichier_yaml.exists():
        raise FileNotFoundError(
            f"Fichier YAML introuvable : {fichier_yaml}"
        )

    # Chargement du YAML
    with open(fichier_yaml, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Parcours des clés
    valeur = data

    for cle in chemin:

        if not isinstance(valeur, dict):
            raise TypeError(
                f"\nImpossible d'accéder à la clé '{cle}'.\n"
                f"L'objet actuel n'est pas un dictionnaire.\n"
                f"Valeur actuelle : {valeur}"
            )

        if cle not in valeur:
            raise KeyError(
                f"\nClé introuvable : '{cle}'"
            )

        valeur = valeur[cle]

    return valeur


# ============================================================
# PROGRAMME PRINCIPAL
# ============================================================

if __name__ == "__main__":

    fichier_yaml = "nipype_interfaces_v2.json"

    # Chemin sous forme de liste de clés
    chemin = [
        "afni",
        "model",
        "interfaces",
        "Deconvolve",
        "inputs",
        "in_files"
    ]

    try:

        valeur = lire_valeur_yaml(
            fichier_yaml,
            chemin
        )

        print("\n" + "=" * 80)
        print("CHEMIN :")
        print(" -> ".join(chemin))

        print("\nVALEUR :")
        print("=" * 80)

        # Affichage YAML propre si dict ou list
        if isinstance(valeur, (dict, list)):
            print(
                yaml.dump(
                    valeur,
                    allow_unicode=True,
                    default_flow_style=False,
                    sort_keys=False
                )
            )
        else:
            print(valeur)

    except (FileNotFoundError, KeyError, TypeError) as e:
        print(e)