from pathlib import Path

def searching_string(dossier, mot):
    dossier_path = Path(dossier)
    for fichier in dossier_path.rglob('*'):
        if fichier.is_file():
            try:
                with fichier.open('r', encoding='utf-8') as f:
                    for num_ligne, ligne in enumerate(f, start=1):
                        if mot in ligne:
                            print(f"{fichier} (ligne {num_ligne}) : {ligne.strip()}")
            except (UnicodeDecodeError, PermissionError):
                continue

user_dir = "/home/olivier/Documents/eclipse-workspace/skrypy-pyqt6/"
searchstring = "/tmp"

searching_string(user_dir, searchstring)
