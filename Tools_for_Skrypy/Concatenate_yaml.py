from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True

files = ["Interfaces_mrtrix3_connectivity.yml",
            "Interfaces_mrtrix3_preprocess.yml",
            "Interfaces_mrtrix3_reconst.yml",
            "Interfaces_mrtrix3_tracking.yml",
            "Interfaces_mrtrix3_utils.yml"]

merged = {}

for file in files:
    with open(file, "r") as f:
        data = yaml.load(f)
        
        for key, value in data.items():
            if key not in merged:
                merged[key] = value
            else:
                # Si le tag parent existe déjà
                if isinstance(value, dict):
                    merged[key].update(value)
                elif isinstance(value, list):
                    merged[key].extend(value)
                else:
                    merged[key] = value  # écrase

# Réordonner les clés si nécessaire
ordered_keys = ["version", "services", "networks", "volumes"]

ordered = {k: merged[k] for k in ordered_keys if k in merged}

# Ajouter les autres clés non listées
for k in merged:
    if k not in ordered:
        ordered[k] = merged[k]

with open("merged.yml", "w") as f:
    yaml.dump(ordered, f)