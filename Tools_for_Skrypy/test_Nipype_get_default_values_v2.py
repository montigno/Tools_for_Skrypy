import inspect
import pkgutil
import importlib
import json

import nipype.interfaces

from traits.trait_handlers import TraitCompound, TraitEnum
from traits.api import Undefined


# ============================================================
# CONVERSION DES VALEURS EN TYPES JSON COMPATIBLES
# ============================================================

def get_default_python_value(value):
    """
    Convertit une valeur Traits/Python en une valeur
    compatible JSON.
    """

    if value is Undefined:
        return None

    if value is None:
        return None

    if isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, (list, tuple)):
        return [
            get_default_python_value(v)
            for v in value
        ]

    if isinstance(value, dict):
        return {
            str(k): get_default_python_value(v)
            for k, v in value.items()
        }

    return str(value)


# ============================================================
# RECUPERATION DE LA VALEUR PAR DEFAUT D'UN TRAIT
# ============================================================

def get_default_value(trait):
    """
    Récupère la valeur par défaut d'un CTrait.
    """

    if trait is None:
        return None

    try:

        default = trait.default_value()

        # default_value() peut retourner un tuple
        # du type (type_defaut, valeur)
        if isinstance(default, tuple) and len(default) == 2:

            # Dans certains cas Traits retourne :
            # (default_value_type, default_value)
            value = default[1]

            if value is Undefined:
                return None

            return get_default_python_value(value)

        if default is Undefined:
            return None

        return get_default_python_value(default)

    except Exception:

        pass

    return None


# ============================================================
# RECUPERATION DES VALEURS D'UN ENUM
# ============================================================

def get_enum_values(obj):
    """
    Essaie de récupérer les valeurs possibles d'un Enum.
    Fonction volontairement tolérante aux différentes
    versions de Traits.
    """

    if obj is None:
        return None

    # --------------------------------------------------------
    # Si c'est un CTrait, regarder son trait_type
    # --------------------------------------------------------

    trait_type = getattr(obj, "trait_type", None)

    if trait_type is not None and trait_type is not obj:

        values = get_enum_values(trait_type)

        if values is not None:
            return values

    # --------------------------------------------------------
    # TraitEnum explicite
    # --------------------------------------------------------

    if isinstance(obj, TraitEnum):

        for attr in (
            "values",
            "_values",
            "enum_values",
        ):

            values = getattr(obj, attr, None)

            if values is not None:

                try:
                    return [
                        get_default_python_value(v)
                        for v in list(values)
                    ]
                except Exception:
                    pass

    # --------------------------------------------------------
    # Recherche générique
    # --------------------------------------------------------

    for attr in (
        "values",
        "_values",
        "enum_values",
    ):

        values = getattr(obj, attr, None)

        if values is not None:

            try:

                return [
                    get_default_python_value(v)
                    for v in list(values)
                ]

            except Exception:
                pass

    return None


def resolve_trait_collection(value):
    """
    Transforme une collection Traits potentiellement exposée
    comme attribut ou comme méthode en liste Python.
    """

    if value is None:
        return None

    if callable(value):

        try:
            value = value()
        except Exception:
            return None

    try:
        return list(value)

    except (TypeError, ValueError):
        return None


# ============================================================
# RECUPERATION DU TRAIT INTERNE D'UN CONTENEUR
# ============================================================

def get_container_element(obj, handler=None):
    """
    Recherche le trait correspondant aux éléments internes
    d'un List ou d'un InputMultiObject.

    Recherche dans :
        - inner_traits
        - item_trait
        - inner_trait
        - trait

    en tenant compte du CTrait et du handler.
    """

    sources = []

    if obj is not None:
        sources.append(obj)

    if handler is not None and handler is not obj:
        sources.append(handler)

    for source in sources:

        if source is None:
            continue

        # ----------------------------------------------------
        # inner_traits
        # ----------------------------------------------------

        inner_traits = getattr(
            source,
            "inner_traits",
            None
        )

        if inner_traits:

            try:

                if isinstance(
                    inner_traits,
                    (list, tuple)
                ) and len(inner_traits) > 0:

                    return inner_traits[0]

            except Exception:
                pass

        # ----------------------------------------------------
        # item_trait
        # ----------------------------------------------------

        item_trait = getattr(
            source,
            "item_trait",
            None
        )

        if item_trait is not None:
            return item_trait

        # ----------------------------------------------------
        # inner_trait
        # ----------------------------------------------------

        inner_trait = getattr(
            source,
            "inner_trait",
            None
        )

        if inner_trait is not None:
            return inner_trait

        # ----------------------------------------------------
        # trait
        # ----------------------------------------------------

        inner_trait = getattr(
            source,
            "trait",
            None
        )

        if inner_trait is not None:
            return inner_trait

    return None


# ============================================================
# RECUPERATION DES HANDLERS D'UN TRAIT COMPOSE
# ============================================================

def get_compound_handlers(obj, handler=None):
    """
    Récupère les alternatives possibles d'un TraitCompound.
    """

    sources = []

    if obj is not None:
        sources.append(obj)

    if handler is not None and handler is not obj:
        sources.append(handler)

    for source in sources:

        if source is None:
            continue

        handlers = getattr(
            source,
            "handlers",
            None
        )

        if handlers is None:
            continue

        if callable(handlers):

            try:
                handlers = handlers()
            except Exception:
                handlers = None

        if handlers:

            try:
                return list(handlers)
            except Exception:
                pass

    return []


# ============================================================
# ANALYSE D'UN OBJET TRAITS
# ============================================================

def get_trait_structure(obj, _depth=0):
    """
    Analyse récursivement un objet Traits.

    Gère :
        - CTrait
        - Enum
        - List
        - InputMultiObject
        - Tuple
        - TraitCompound
        - types simples

    _depth évite une récursion infinie.
    """

    # Sécurité contre les structures circulaires
    if _depth > 20:

        return {
            "type": "MaxDepth"
        }

    if obj is None:

        return {
            "type": "NoneType"
        }

    # ========================================================
    # IDENTIFICATION CTrait / Handler
    # ========================================================

    trait = None
    handler = None

    # Un CTrait possède généralement trait_type
    if hasattr(obj, "trait_type"):

        trait = obj

        handler = getattr(
            obj,
            "trait_type",
            None
        )

        # Important :
        # certains CTrait ont trait_type == None
        # mais possèdent quand même inner_traits ou d'autres
        # informations utiles.
        if handler is None:

            # ------------------------------------------------
            # Essayer d'abord un TraitCompound
            # ------------------------------------------------

            compound_handlers = get_compound_handlers(
                trait,
                None
            )

            if compound_handlers:

                return {
                    "type": "TraitCompound",
                    "types": [
                        get_trait_structure(
                            subtrait,
                            _depth + 1
                        )
                        for subtrait in compound_handlers
                    ]
                }

            # ------------------------------------------------
            # Essayer les traits internes
            # ------------------------------------------------

            inner_traits = getattr(
                trait,
                "inner_traits",
                None
            )

            if inner_traits:

                try:

                    if len(inner_traits) == 1:

                        return get_trait_structure(
                            inner_traits[0],
                            _depth + 1
                        )

                except Exception:
                    pass

            # Aucun type détectable
            return {
                "type": "Unknown"
            }

    else:

        handler = obj

    # ========================================================
    # TYPE DU HANDLER
    # ========================================================

    if handler is None:

        return {
            "type": "NoneType"
        }

    type_name = type(handler).__name__

    result = {
        "type": type_name
    }

    # ========================================================
    # ENUM
    # ========================================================

    enum_values = get_enum_values(handler)

    if enum_values is not None:

        result["type"] = "Enum"
        result["values"] = enum_values

        return result

    # ========================================================
    # INPUT MULTI OBJECT
    # ========================================================

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

        element_trait = get_container_element(
            trait,
            handler
        )

        if element_trait is not None:

            result["element"] = get_trait_structure(
                element_trait,
                _depth + 1
            )

        else:

            result["element"] = {
                "type": "Any"
            }

        return result

    # ========================================================
    # LIST
    # ========================================================

    if type_name == "List":

        result["type"] = "List"

        element_trait = get_container_element(
            trait,
            handler
        )

        if element_trait is not None:

            result["element"] = get_trait_structure(
                element_trait,
                _depth + 1
            )

        else:

            result["element"] = {
                "type": "Any"
            }

        return result

    # ========================================================
    # TUPLE
    # ========================================================
    
    if type_name == "Tuple":
    
        result["type"] = "Tuple"
        result["elements"] = []
    
        sources = []
    
        if trait is not None:
            sources.append(trait)
    
        if handler is not None:
            sources.append(handler)
    
        tuple_traits = None
    
        for source in sources:
    
            if source is None:
                continue
    
            # inner_traits
            tuple_traits = resolve_trait_collection(
                getattr(
                    source,
                    "inner_traits",
                    None
                )
            )
    
            if tuple_traits:
                break
    
            # types
            tuple_traits = resolve_trait_collection(
                getattr(
                    source,
                    "types",
                    None
                )
            )
    
            if tuple_traits:
                break
    
        if tuple_traits:
    
            for subtrait in tuple_traits:
    
                if subtrait is None:
                    continue
    
                result["elements"].append(
                    get_trait_structure(
                        subtrait,
                        _depth + 1
                    )
                )
    
        return result



    # ========================================================
    # TRAIT COMPOUND / EITHER
    # ========================================================

    if isinstance(handler, TraitCompound):

        result["type"] = "TraitCompound"
        result["types"] = []

        compound_handlers = get_compound_handlers(
            trait,
            handler
        )

        for subhandler in compound_handlers:

            if subhandler is None:
                continue

            substructure = get_trait_structure(
                subhandler,
                _depth + 1
            )

            result["types"].append(
                substructure
            )

        return result

    # ========================================================
    # AUTRES TYPES SIMPLES
    # ========================================================

    return result


# ============================================================
# ANALYSE COMPLETE D'UN TRAIT
# ============================================================

def trait_info(trait):
    """
    Retourne toutes les informations d'un trait Nipype.
    """

    structure = get_trait_structure(trait)

    info = {

        "type": structure.get(
            "type",
            type(
                getattr(
                    trait,
                    "trait_type",
                    None
                )
            ).__name__
        ),

        "mandatory": bool(
            getattr(
                trait,
                "mandatory",
                False
            )
        ),

        "usedefault": bool(
            getattr(
                trait,
                "usedefault",
                False
            )
        ),

        "default": get_default_value(trait),

        "description": getattr(
            trait,
            "desc",
            None
        ),

        "structure": structure,
    }

    # ========================================================
    # INFORMATIONS SUPPLEMENTAIRES
    # ========================================================

    for attr in (
        "argstr",
        "position",
        "exists",
        "copyfile",
        "genfile",
        "hash_files",
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

    # ========================================================
    # XOR
    # ========================================================

    try:

        xor = getattr(
            trait,
            "xor",
            None
        )

        if xor:
            info["xor"] = list(xor)

    except Exception:
        pass

    # ========================================================
    # REQUIRES
    # ========================================================

    try:

        requires = getattr(
            trait,
            "requires",
            None
        )

        if requires:
            info["requires"] = list(requires)

    except Exception:
        pass

    return info


# ============================================================
# ANALYSE D'UNE INTERFACE NIPYPE
# ============================================================

def get_interface_info(interface_class):
    """
    Retourne toutes les informations d'une interface Nipype.
    """

    info = {

        "name": interface_class.__name__,

        "module": interface_class.__module__,

        "inputs": {},

        "outputs": {}
    }

    # ========================================================
    # INPUTS
    # ========================================================

    input_spec = getattr(
        interface_class,
        "input_spec",
        None
    )

    if input_spec is not None:

        for name, trait in input_spec.class_traits().items():

            if name.startswith("_"):
                continue

            try:

                info["inputs"][name] = trait_info(
                    trait
                )

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

    # ========================================================
    # OUTPUTS
    # ========================================================

    output_spec = getattr(
        interface_class,
        "output_spec",
        None
    )

    if output_spec is not None:

        for name, trait in output_spec.class_traits().items():

            if name.startswith("_"):
                continue

            try:

                info["outputs"][name] = trait_info(
                    trait
                )

            except Exception as e:

                print(
                    f"Erreur output "
                    f"{interface_class.__module__}."
                    f"{interface_class.__name__}."
                    f"{name}: {e}"
                )

                info["outputs"][name] = {

                    "type": type(
                        getattr(
                            trait,
                            "trait_type",
                            None
                        )
                    ).__name__,

                    "error": str(e)
                }

    return info


# ============================================================
# PARCOURS DE TOUTES LES INTERFACES NIPYPE
# ============================================================

def scan_nipype_interfaces():
    """
    Parcourt automatiquement tous les modules Nipype
    et organise les interfaces hiérarchiquement.
    """

    result = {}

    package = nipype.interfaces

    modules = [package]

    # ========================================================
    # RECHERCHE DES SOUS-MODULES
    # ========================================================

    print("Recherche des modules Nipype...")

    for module_info in pkgutil.walk_packages(
        package.__path__,
        package.__name__ + "."
    ):

        try:

            module = importlib.import_module(
                module_info.name
            )

            print(
                "Module :",
                module_info.name
            )

            modules.append(module)

        except Exception as e:

            print(
                f"Impossible d'importer "
                f"{module_info.name}: {e}"
            )

    # ========================================================
    # RECHERCHE DES INTERFACES
    # ========================================================

    interface_count = 0

    for module in modules:

        subresult = {}

        for name, obj in inspect.getmembers(
            module,
            inspect.isclass
        ):

            # La classe doit être définie directement
            # dans le module analysé
            if obj.__module__ != module.__name__:
                continue

            # Une interface Nipype possède un input_spec
            if not hasattr(obj, "input_spec"):
                continue

            try:

                info = get_interface_info(obj)

                subresult[name] = info

                interface_count += 1

            except Exception as e:

                print(
                    f"Erreur avec "
                    f"{module.__name__}.{name}: {e}"
                )

        # ====================================================
        # PAS D'INTERFACE
        # ====================================================

        if not subresult:
            continue

        # ====================================================
        # CREATION DE LA HIERARCHIE
        # ====================================================

        module_name = module.__name__

        prefix = "nipype.interfaces."

        if module_name.startswith(prefix):

            parts = module_name[
                len(prefix):
            ].split(".")

        else:

            parts = module_name.split(".")

        current = result

        for part in parts:

            if part not in current:
                current[part] = {}

            current = current[part]

        current["interfaces"] = subresult

    print()
    print(
        "Nombre total d'interfaces :",
        interface_count
    )

    return result


# ============================================================
# PROGRAMME PRINCIPAL
# ============================================================

if __name__ == "__main__":

    interfaces = scan_nipype_interfaces()

    output_file = "nipype_interfaces_v2.json"

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            interfaces,
            f,
            indent=4,
            ensure_ascii=False,
            default=str
        )

    print()
    print(
        "Fichier créé :",
        output_file
    )