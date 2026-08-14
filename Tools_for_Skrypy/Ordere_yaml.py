import yaml


def sort_yaml(data):
    if isinstance(data, dict):
        return {
            key: sort_yaml(data[key])
            for key in sorted(data)
        }

    elif isinstance(data, list):
        return [
            sort_yaml(item)
            for item in data
        ]

    return data

with open("merged.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

data = sort_yaml(data)

with open("output.yaml", "w", encoding="utf-8") as f:
    yaml.dump(
        data,
        f,
        allow_unicode=True,
        sort_keys=False
    )