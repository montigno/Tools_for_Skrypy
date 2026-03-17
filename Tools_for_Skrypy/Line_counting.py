from pathlib import Path

def count_lines_py(repertory):
    total1, total2, total3 = 0, 0, 0

    for file in Path(repertory).rglob("*.py"):
        with file.open("r", encoding="utf-8") as f:
            total1 += sum(1 for _ in f)
            # total2 += sum(1 for ligne in f if ligne.strip())
            # total3 += sum(1 for ligne in f if ligne.strip() and not ligne.strip().startswith("#"))

    return total1, total2, total3


rep = "/home/olivier/Documents/eclipse-workspace-2026/skrypy-pyqt5"
print(count_lines_py(rep))

rep = "/home/olivier/Applications/populse_mia/lib/python3.12/site-packages/populse_mia"
print(count_lines_py(rep))