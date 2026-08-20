import inspect
import pkgutil
import importlib
import json
import nipype.interfaces
from traits.trait_handlers import TraitCompound, TraitEnum


def get_enum_values(handler):
    """Retourne les valeurs d'un Enum."""

    if isinstance(handler, TraitEnum):
        return list(handler.values)

    return None


def get_trait_structure(trait_or_handler):

    # --------------------------------------------------
    # Déterminer si on reçoit un Trait ou un TraitHandler
    # --------------------------------------------------

    if hasattr(trait_or_handler, "trait_type"):
        handler = trait_or_handler.trait_type
    else:
        handler = trait_or_handler

    type_name = type(handler).__name__

    result = {
        "type": type_name
    }

    # --------------------------------------------------
    # ENUM
    # --------------------------------------------------

    enum = get_enum_values(handler)

    if enum is not None:

        result["type"] = "Enum"
        result["values"] = enum

        return result

    # --------------------------------------------------
    # LIST
    # --------------------------------------------------

    if type_name == "List":

        item_trait = getattr(
            handler,
            "item_trait",
            None
        )

        if item_trait is not None:

            result["element"] = get_trait_structure(
                item_trait
            )

        return result

    # --------------------------------------------------
    # TRAIT COMPOUND
    # --------------------------------------------------

    if isinstance(handler, TraitCompound):

        result["types"] = []

        for subhandler in handler.handlers:

            result["types"].append(
                get_trait_structure(subhandler)
            )

        return result

    return result

def get_list_element_type(trait):

    trait_type = trait.trait_type

    if type(trait_type).__name__ != "List":
        return None

    item_trait = getattr(trait_type, "item_trait", None)

    if item_trait is None:
        return None

    return type(item_trait.trait_type).__name__

def trait_info(trait):

    structure = get_trait_structure(trait)

    info = {
        "type": structure["type"],
        "mandatory": getattr(trait, "mandatory", False),
        "usedefault": getattr(trait, "usedefault", False),
        "default": None,
        "description": getattr(trait, "desc", ""),
        "structure": structure,
    }

    # Valeur par défaut
    try:

        default = trait.default_value

        if default is not None:

            if isinstance(
                default,
                (str, int, float, bool, list, tuple)
            ):
                info["default"] = default

            else:
                info["default"] = str(default)

    except Exception:
        pass

    # Informations supplémentaires
    for attr in (
        "argstr",
        "position",
        "exists",
        "xor",
        "requires"
    ):

        try:

            value = getattr(trait, attr, None)

            if value is not None:
                info[attr] = value

        except Exception:
            pass

    return info


def get_interface_info(interface_class):
    """Retourne toutes les informations d'une interface Nipype."""

    info = {
        "name": interface_class.__name__,
        "module": interface_class.__module__,
        "inputs": {},
        "outputs": {}
    }

    # --------------------------------------------------
    # INPUTS
    # --------------------------------------------------

    input_spec = getattr(interface_class, "input_spec", None)

    if input_spec is not None:

        for name, trait in input_spec.class_traits().items():

            if name.startswith("_"):
                continue

            info["inputs"][name] = trait_info(trait)

    # --------------------------------------------------
    # OUTPUTS
    # --------------------------------------------------

    output_spec = getattr(interface_class, "output_spec", None)

    if output_spec is not None:

        for name, trait in output_spec.class_traits().items():

            if name.startswith("_"):
                continue

            info["outputs"][name] = trait_info(trait)

    return info


def scan_nipype_interfaces():
    """Parcourt automatiquement tous les modules Nipype."""

    result = {}

    package = nipype.interfaces

    # Modules à parcourir
    modules = [package]

    for module_info in pkgutil.walk_packages(
        package.__path__,
        package.__name__ + "."
    ):

        try:
            module = importlib.import_module(module_info.name)
            modules.append(module)

        except Exception as e:
            print(
                f"Impossible d'importer "
                f"{module_info.name}: {e}"
            )

    # --------------------------------------------------
    # Recherche des classes
    # --------------------------------------------------

    for module in modules:

        for name, obj in inspect.getmembers(module, inspect.isclass):

            # La classe doit être définie dans ce module
            if obj.__module__ != module.__name__:
                continue

            # Une interface Nipype possède généralement input_spec
            if not hasattr(obj, "input_spec"):
                continue

            try:

                info = get_interface_info(obj)

                result[name] = info

            except Exception as e:

                print(
                    f"Erreur avec "
                    f"{module.__name__}.{name}: {e}"
                )

    return result

interfaces = scan_nipype_interfaces()

print("Nombre d'interfaces :", len(interfaces))

info = interfaces["FNIRT"]

print(info["module"])

print("\nINPUTS")

for name, data in info["inputs"].items():

    print(
        f"{name:30} "
        f"type={data['type']:20} "
        f"mandatory={data['mandatory']} "
        f"default={data['default']}"
    )

    if data["type"] == "Enum":

        print(
            f"    valeurs : "
            f"{data['structure']['values']}"
        )

    elif data["type"] == "List":

        print(
            f"    élément : "
            f"{data['structure'].get('element')}"
        )

    elif data["type"] == "TraitCompound":

        print(
            f"    types : "
            f"{data['structure']['types']}"
        )


print("\nOUTPUTS")

for name, data in info["outputs"].items():

    print(
        f"{name:25} "
        f"type={data['type']}"
    )

with open("nipype_interfaces.json", "w", encoding="utf-8") as f:
    json.dump(
        interfaces,
        f,
        indent=4,
        ensure_ascii=False,
        default=str
    )
