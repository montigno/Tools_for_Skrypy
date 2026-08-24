import inspect
import pkgutil
import importlib
import json
import nipype.interfaces
from traits.trait_handlers import TraitCompound, TraitEnum
from traits.api import Undefined

from traits.api import Undefined


def get_inner_trait_structure(obj):
    """
    Recherche récursivement le trait interne d'un conteneur
    comme List ou InputMultiObject.
    """

    if obj is None:
        return {"type": "Any"}

    # Si c'est directement un CTrait ou un trait analysable
    structure = get_trait_structure(obj)

    if structure.get("type") != "NoneType":
        return structure

    return {"type": "Any"}


def get_handler_structure(handler):

    if handler is None:
        return {
            "type": "NoneType"
        }

    type_name = type(handler).__name__

    result = {
        "type": type_name
    }

    # ==================================================
    # ENUM
    # ==================================================

    values = get_enum_values(handler)

    if values is not None:

        result["type"] = "Enum"
        result["values"] = [
            get_default_python_value(v)
            for v in values
        ]

        return result

    # ==================================================
    # LIST
    # ==================================================

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

        else:

            result["element"] = {
                "type": "Any"
            }

        return result

    # ==================================================
    # TRAIT COMPOUND / EITHER
    # ==================================================
    
    
    # print("\n=== COMPOUND ===")
    #
    # for subhandler in handlers:
    #
    #     print("subhandler :", repr(subhandler))
    #     print("type :", type(subhandler))
    #     print("dict :", getattr(subhandler, "__dict__", None))
    #
    #     print("trait_type :",
    #           getattr(subhandler, "trait_type", "ABSENT"))
    #
    #     print("handlers :",
    #           getattr(subhandler, "handlers", "ABSENT"))
    #
    #     print("values :",
    #           getattr(subhandler, "values", "ABSENT"))
    #
    #     print("item_trait :",
    #           getattr(subhandler, "item_trait", "ABSENT"))
    #
    #     print("inner_traits :",
    #           getattr(subhandler, "inner_traits", "ABSENT"))
    #
    #     if isinstance(handler, TraitCompound):
    #
    #         result["types"] = []
    #
    #         handlers = getattr(
    #             handler,
    #             "handlers",
    #             ()
    #         )

        if callable(handlers):

            try:
                handlers = handlers()
            except Exception:
                handlers = ()

        for subhandler in handlers:

            if subhandler is None:
                continue

            result["types"].append(
                get_handler_structure(subhandler)
            )

        return result

    # ==================================================
    # INPUT MULTI OBJECT
    # ==================================================
    
    # print("\n=== InputMultiObject ===")
    # print("trait =", trait)
    # print("handler =", handler)
    # print("trait.inner_traits =", getattr(trait, "inner_traits", None))
    # print("trait.item_trait =", getattr(trait, "item_trait", None))
    # print("handler.trait =", getattr(handler, "trait", None))
    # print("handler.item_trait =", getattr(handler, "item_trait", None))
    # print("handler.inner_trait =", getattr(handler, "inner_trait", None))
    # print("handler.inner_traits =", getattr(handler, "inner_traits", None))
    
    if type_name == "InputMultiObject":
    
        result["type"] = "InputMultiObject"
    
        # Valeur par défaut éventuelle
        default = getattr(handler, "default_value", None)
    
        if default is not None:
    
            if callable(default):
                try:
                    default = default()
                except Exception:
                    default = None
    
            if default is not None:
                result["default"] = get_default_python_value(default)
    
        # Recherche du trait interne
        element_trait = None
    
        for attr in (
            "trait",
            "inner_trait",
            "item_trait",
        ):
    
            value = getattr(handler, attr, None)
    
            if value is not None:
                element_trait = value
                break
    
        # Certains objets stockent l'information
        # dans inner_traits
        if element_trait is None:
    
            inner_traits = getattr(
                obj if trait is not None else handler,
                "inner_traits",
                ()
            )
    
            if inner_traits:
                element_trait = inner_traits[0]
    
        if element_trait is not None:
    
            result["element"] = get_trait_structure(
                element_trait
            )
    
        else:
    
            result["element"] = {
                "type": "Any"
            }
    
        return result

    # ==================================================
    # AUTRES TYPES
    # ==================================================

    default = getattr(
        handler,
        "default_value",
        None
    )

    if default is not None:

        if callable(default):

            try:
                default = default()
            except Exception:
                default = None

        if default is not None:

            result["default"] = get_default_python_value(
                default
            )

    return result

def get_handler_info(handler):
    """
    Retourne les informations générales d'un Trait handler,
    y compris la structure interne des List, Tuple,
    TraitCompound, Enum, etc.
    """

    # Analyse complète de la structure
    result = get_trait_structure(handler)

    # --------------------------------------------------
    # Description
    # --------------------------------------------------

    desc = getattr(handler, "desc", None)

    if desc:
        result["description"] = desc

    # --------------------------------------------------
    # Valeur par défaut
    # --------------------------------------------------

    default = getattr(handler, "default_value", None)

    if default is not None:

        if callable(default):
            try:
                default = default()
            except Exception:
                default = None

        if default is not None:
            result["default"] = get_default_python_value(default)

    return result


def get_default_value(trait):

    try:
        default = trait.default_value()

        if default is Undefined:
            return None

        if isinstance(default, tuple):
            return [
                get_default_python_value(v)
                for v in default
            ]

        if isinstance(default, list):
            return [
                get_default_python_value(v)
                for v in default
            ]

        if isinstance(default, (str, int, float, bool)):
            return default

        return str(default)

    except Exception:
        return None


def get_default_python_value(value):

    if value is Undefined:
        return None

    if isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, (list, tuple)):
        return [
            get_default_python_value(v)
            for v in value
        ]

    return str(value)


def get_enum_values(handler):

    if handler is None:
        return None

    # --------------------------------------------------
    # TraitEnum
    # --------------------------------------------------

    if isinstance(handler, TraitEnum):

        for attr in (
            "values",
            "_values",
        ):

            values = getattr(
                handler,
                attr,
                None
            )

            if values is not None:

                try:
                    return list(values)
                except Exception:
                    pass

    # --------------------------------------------------
    # Enum générique
    # --------------------------------------------------

    for attr in (
        "values",
        "_values",
        "enum_values",
    ):

        values = getattr(
            handler,
            attr,
            None
        )

        if values is not None:

            try:
                return list(values)
            except Exception:
                pass

    return None


def get_trait_structure(obj):

    if obj is None:
        return {
            "type": "NoneType"
        }

    # --------------------------------------------------
    # CTrait avec un vrai trait_type
    # --------------------------------------------------

    trait_type = getattr(
        obj,
        "trait_type",
        None
    )

    if trait_type is not None:

        type_name = type(trait_type).__name__

        # Pour une List, les inner_traits sont
        # portés par le CTrait
        if type_name == "List":

            result = {
                "type": "List"
            }

            inner_traits = getattr(
                obj,
                "inner_traits",
                ()
            )

            if inner_traits:

                result["element"] = get_trait_structure(
                    inner_traits[0]
                )

            else:

                item_trait = getattr(
                    trait_type,
                    "item_trait",
                    None
                )

                if item_trait is not None:

                    result["element"] = get_trait_structure(
                        item_trait
                    )

                else:

                    result["element"] = {
                        "type": "Any"
                    }

            return result

        return get_handler_structure(trait_type)

    # --------------------------------------------------
    # Handler direct
    # --------------------------------------------------

    return get_handler_structure(obj)



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
        "type": structure.get(
            "type",
            type(trait.trait_type).__name__
        ),
        "mandatory": bool(
            getattr(trait, "mandatory", False)
        ),
        "usedefault": bool(
            getattr(trait, "usedefault", False)
        ),
        "default": get_default_value(trait),
        "description": getattr(
            trait,
            "desc",
            ""
        ),
        "structure": structure,
    }

    # ----------------------------------------------
    # Informations supplémentaires
    # ----------------------------------------------

    for attr in (
        "argstr",
        "position",
        "exists",
    ):
        try:
            value = getattr(
                trait,
                attr,
                None
            )
            if value is not None:
                info[attr] = value

        except Exception:
            pass

    # ----------------------------------------------
    # XOR
    # ----------------------------------------------

    xor = getattr(
        trait,
        "xor",
        None
    )

    if xor:
        info["xor"] = list(xor)

    # ----------------------------------------------
    # REQUIRES
    # ----------------------------------------------

    requires = getattr(
        trait,
        "requires",
        None
    )

    if requires:
        info["requires"] = list(requires)

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
        
            try:
        
                info["inputs"][name] = trait_info(trait)
        
            except Exception as e:
        
                print(
                    f"Erreur input "
                    f"{interface_class.__module__}."
                    f"{interface_class.__name__}."
                    f"{name}: {e}"
                )
        
                info["inputs"][name] = {
                    "type": type(
                        getattr(
                            trait,
                            "trait_type",
                            None
                        )
                    ).__name__,
                    "error": str(e)
                }

    # --------------------------------------------------
    # OUTPUTS
    # --------------------------------------------------

    output_spec = getattr(interface_class, "output_spec", None)

    if output_spec is not None:

        for name, trait in output_spec.class_traits().items():

            if name.startswith("_"):
                continue

            info["outputs"][name] = trait_info(trait)
    # print('        ', info["inputs"])
    # for inp, inv in info['inputs'].items():
    #     print('    ', inp, inv)

    return info


def scan_nipype_interfaces():
    """Parcourt automatiquement tous les modules Nipype
    et organise les interfaces hiérarchiquement.
    """

    result = {}

    package = nipype.interfaces
    modules = [package]

    # --------------------------------------------------
    # Recherche de tous les sous-modules
    # --------------------------------------------------

    for module_info in pkgutil.walk_packages(
        package.__path__,
        package.__name__ + "."
    ):

        try:
            module = importlib.import_module(module_info.name)

            print("Module :", module_info.name)

            modules.append(module)

        except Exception as e:

            print(
                f"Impossible d'importer "
                f"{module_info.name}: {e}"
            )

    # --------------------------------------------------
    # Recherche des classes / interfaces
    # --------------------------------------------------

    for module in modules:

        subresult = {}

        for name, obj in inspect.getmembers(
            module,
            inspect.isclass
        ):

            # La classe doit être définie directement
            # dans le module actuellement analysé
            if obj.__module__ != module.__name__:
                continue

            # Une interface Nipype possède un input_spec
            if not hasattr(obj, "input_spec"):
                continue

            try:
                info = get_interface_info(obj)
                subresult[name] = info
            except Exception as e:
                print(
                    f"Erreur avec "
                    f"{module.__name__}.{name}: {e}"
                )

        # Pas d'interface dans ce module
        if not subresult:
            continue

        # --------------------------------------------------
        # Création de la structure hiérarchique
        # --------------------------------------------------

        module_name = module.__name__

        # Exemple :
        #
        # nipype.interfaces.ants.registration
        #
        # devient :
        #
        # ["ants", "registration"]

        prefix = "nipype.interfaces."

        if module_name.startswith(prefix):
            parts = module_name[len(prefix):].split(".")
        else:
            parts = module_name.split(".")

        # --------------------------------------------------
        # Création automatique des dictionnaires imbriqués
        # --------------------------------------------------

        current = result

        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]

        # Ajout des interfaces dans ce module
        current["interfaces"] = subresult

    return result


interfaces = scan_nipype_interfaces()
print("Nombre d'interfaces :", len(interfaces))

with open("nipype_interfaces.json", "w", encoding="utf-8") as f:
    json.dump(
        interfaces,
        f,
        indent=4,
        ensure_ascii=False,
        default=str
    )
