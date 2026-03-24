import inspect
import pandas as pd

from nipype.interfaces import fsl
from nipype.interfaces.base import BaseInterface, Undefined


def is_interface(obj):
    return inspect.isclass(obj) and issubclass(obj, BaseInterface)


def list_all_interfaces(module):
    return [
        obj for _, obj in inspect.getmembers(module)
        if is_interface(obj)
    ]


def get_enum_values(trait):
    """
    Récupère les valeurs possibles d'un Enum Nipype (si existant)
    """
    trait_type = trait.trait_type

    # cas standard (traits Enum)
    if hasattr(trait_type, "values") and trait_type.values:
        try:
            return list(trait_type.values)
        except Exception:
            pass

    return None


def extract_interface_data(interface):
    rows = []

    try:
        instance = interface()
        inputs = instance.inputs

        for name, trait in inputs.traits().items():
            if name.startswith("_"):
                continue

            # valeur par défaut (dans Nipype)
            value = getattr(inputs, name)
            default = None if value is Undefined else value

            # type
            trait_type_name = type(trait.trait_type).__name__

            # enum
            enum_values = get_enum_values(trait)

            rows.append({
                "interface": interface.__name__,
                "parameter": name,
                "mandatory": trait.mandatory,
                "default": default,
                "type": trait_type_name,
                "enum_values": enum_values,
                "description": trait.desc
            })

    except Exception as e:
        print(f"Skipping {interface.__name__}: {e}")

    return rows


def main():
    interfaces = list_all_interfaces(fsl)

    all_rows = []

    for iface in interfaces:
        all_rows.extend(extract_interface_data(iface))

    df = pd.DataFrame(all_rows)

    # tri lisible
    df = df.sort_values(by=["interface", "mandatory"], ascending=[True, False])

    # export
    output_file = "nipype_fsl_interfaces.csv"
    df.to_csv(output_file, index=False)

    print(f"Export terminé : {output_file}")
    print(df.head())


if __name__ == "__main__":
    main()