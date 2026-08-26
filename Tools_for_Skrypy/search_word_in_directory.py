from pathlib import Path


def rechercher_mot(dossier, mot, file_ext):
    dossier = Path(dossier)

    if not dossier.is_dir():
        print(f"Erreur : le dossier n'existe pas : {dossier}")
        return

    print(f"Recherche de '{mot}' dans : {dossier}\n")

    nb_fichiers = 0
    nb_occurrences = 0

    # Parcours récursif de tous les fichiers .py
    for fichier in dossier.rglob(file_ext):
        try:
            with open(fichier, "r", encoding="utf-8") as f:
                for numero_ligne, ligne in enumerate(f, start=1):
                    if mot.lower() in ligne.lower():
                        print(f"{fichier} - ligne {numero_ligne}:")
                        print(f"    {ligne.strip()}\n")

                        nb_occurrences += 1

            nb_fichiers += 1

        except UnicodeDecodeError:
            print(f"Impossible de lire {fichier} avec UTF-8")

        except Exception as e:
            print(f"Erreur avec {fichier}: {e}")

    print("-" * 60)
    print(f"Fichiers Python analysés : {nb_fichiers}")
    print(f"Occurrences trouvées     : {nb_occurrences}")


if __name__ == "__main__":

    dossier = "/home/olivier/Documents/eclipse-workspace-2026/skrypy-pyqt5/NodeEditor/modules/Nipype"
    mot = "Mandatory"
    file_extension = "*.yml"

    rechercher_mot(dossier, mot, file_extension)