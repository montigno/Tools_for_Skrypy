#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate a YAML description of all Nipype interfaces and their inputs.

Output:
    nipype_modules.yaml

The generated YAML is intended to be used by a GUI/workflow editor.

Example:

    ants_ANTS:
      module: nipype.interfaces.ants.registration
      class: ANTS
      inputs:
        dimension:
          type: str
          default: null
          mandatory: false
          usedefault: false
          description: "..."
          argstr: "-d %s"

Usage:

    python generate_nipype_yaml.py

Optional:

    python generate_nipype_yaml.py output.yaml
"""

from __future__ import annotations

import inspect
import importlib
import pkgutil
import sys
import traceback
from pathlib import Path
from typing import Any

import yaml

import nipype


# ============================================================================
# Configuration
# ============================================================================

DEFAULT_OUTPUT = "nipype_modules.yaml"


# ============================================================================
# Safe conversion functions
# ============================================================================

def safe_value(value: Any) -> Any:
    """
    Convert a Python / Traits value into something YAML can serialize.

    Nipype traits may contain objects which cannot be directly represented
    in YAML. In those cases we keep a readable string representation.
    """

    if value is None:
        return None

    # Basic YAML-compatible types
    if isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, Path):
        return str(value)

    if isinstance(value, (list, tuple)):
        return [safe_value(v) for v in value]

    if isinstance(value, dict):
        return {
            str(k): safe_value(v)
            for k, v in value.items()
        }

    # numpy scalar types
    try:
        import numpy as np

        if isinstance(value, np.generic):
            return value.item()
    except Exception:
        pass

    # Traits / Python objects
    try:
        return str(value)
    except Exception:
        return repr(value)


def safe_repr(value: Any) -> str | None:
    """
    Return a readable representation without raising exceptions.
    """

    if value is None:
        return None

    try:
        return repr(value)
    except Exception:
        try:
            return str(value)
        except Exception:
            return None


# ============================================================================
# Trait type identification
# ============================================================================

def trait_type_name(trait) -> str:
    """
    Determine a useful high-level type for a Traits trait.

    Examples:
        Int       -> int
        Float     -> float
        Bool      -> bool
        Enum      -> enum
        List      -> list
        File      -> file
        Directory -> directory
        Either    -> either
    """

    cls_name = trait.__class__.__name__

    # Nipype-specific classes
    if cls_name in ("File",):
        return "file"

    if cls_name in ("Directory",):
        return "directory"

    if cls_name in ("InputMultiPath",):
        return "input_multipath"

    if cls_name in ("InputMultiObject",):
        return "input_multiobject"

    # Traits standard classes
    mapping = {
        "Bool": "bool",
        "Int": "int",
        "CInt": "int",
        "Float": "float",
        "CFloat": "float",
        "Str": "str",
        "Unicode": "str",
        "Enum": "enum",
        "List": "list",
        "Tuple": "tuple",
        "Either": "either",
        "Range": "range",
        "Array": "array",
        "Dict": "dict",
        "Set": "set",
        "Complex": "complex",
        "Instance": "instance",
        "Any": "any",
        "Constant": "constant",
        "Expression": "expression",
    }

    if cls_name in mapping:
        return mapping[cls_name]

    return cls_name.lower()


# ============================================================================
# Trait metadata
# ============================================================================

def get_trait_metadata(trait) -> dict:
    """
    Extract metadata attached to a Nipype trait.
    """

    result = {}

    # ------------------------------------------------------------------------
    # Main trait information
    # ------------------------------------------------------------------------

    result["type"] = trait_type_name(trait)

    # ------------------------------------------------------------------------
    # Default value
    # ------------------------------------------------------------------------

    try:
        default = trait.default_value()

        # default_value() may return:
        # (index, value)
        if isinstance(default, tuple) and len(default) == 2:
            default = default[1]

        result["default"] = safe_value(default)

    except Exception:
        result["default"] = None

    # ------------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------------

    metadata_names = [
        "mandatory",
        "usedefault",
        "argstr",
        "position",
        "desc",
        "requires",
        "xor",
        "copyfile",
        "exists",
        "genfile",
        "name_source",
        "name_template",
        "keep_extension",
        "hash_files",
        "nohash",
        "deprecated",
        "minlen",
        "maxlen",
        "min",
        "max",
    ]

    for name in metadata_names:

        try:
            value = getattr(trait, name)

        except Exception:
            continue

        if value is None:
            continue

        # Don't put empty values in YAML unless they are useful.
        if value == "":
            continue

        if value == []:
            continue

        result[name] = safe_value(value)

    # ------------------------------------------------------------------------
    # Enum choices
    # ------------------------------------------------------------------------

    if result["type"] == "enum":

        choices = None

        # Traits Enum normally stores values in .values
        try:
            choices = trait.values
        except Exception:
            pass

        # Some versions / situations may expose values differently
        if choices is None:
            try:
                choices = trait._values
            except Exception:
                pass

        if choices is not None:
            result["choices"] = safe_value(list(choices))

    # ------------------------------------------------------------------------
    # Range
    # ------------------------------------------------------------------------

    if result["type"] == "range":

        for attr in ("low", "high"):

            try:
                value = getattr(trait, attr)

                if value is not None:
                    result[attr] = safe_value(value)

            except Exception:
                pass

    # ------------------------------------------------------------------------
    # List / Tuple element information
    # ------------------------------------------------------------------------

    if result["type"] in ("list", "tuple"):

        try:
            inner = trait.inner_traits

            if inner:

                result["element_traits"] = []

                for inner_trait in inner:

                    result["element_traits"].append(
                        get_trait_metadata(inner_trait)
                    )

        except Exception:
            pass

    # ------------------------------------------------------------------------
    # Either
    # ------------------------------------------------------------------------

    if result["type"] == "either":

        try:
            handlers = trait.handlers

            if handlers:

                result["options"] = [
                    get_trait_metadata(t)
                    for t in handlers
                ]

        except Exception:
            pass

    return result


# ============================================================================
# InputSpec extraction
# ============================================================================

def get_inputs_from_spec(interface_class) -> dict:
    """
    Extract all inputs from an interface's InputSpec.
    """

    inputs = {}

    try:
        input_spec_class = interface_class.input_spec
    except Exception:
        return inputs

    if input_spec_class is None:
        return inputs

    try:
        spec = input_spec_class()

    except Exception:
        return inputs

    # Traits API
    try:
        traits_dict = spec.traits()

    except Exception:
        return inputs

    for name, trait in sorted(traits_dict.items()):

        # Internal / private traits
        if name.startswith("_"):
            continue

        try:
            inputs[name] = get_trait_metadata(trait)

        except Exception as exc:

            inputs[name] = {
                "type": "unknown",
                "error": str(exc),
            }

    return inputs


# ============================================================================
# Interface detection
# ============================================================================

def is_nipype_interface_class(obj) -> bool:
    """
    Determine whether an object is a Nipype interface class.
    """

    if not inspect.isclass(obj):
        return False

    try:
        from nipype.interfaces.base import BaseInterface

        if obj is BaseInterface:
            return False

        return issubclass(obj, BaseInterface)

    except Exception:
        return False


# ============================================================================
# Module scanning
# ============================================================================

def get_all_nipype_modules():
    """
    Recursively find all modules below nipype.interfaces.
    """

    import nipype.interfaces

    modules = []

    for module_info in pkgutil.walk_packages(
        nipype.interfaces.__path__,
        prefix=nipype.interfaces.__name__ + ".",
    ):

        name = module_info.name

        # Skip private modules
        if any(
            part.startswith("_")
            for part in name.split(".")
        ):
            continue

        modules.append(name)

    return sorted(set(modules))


# ============================================================================
# Scan one module
# ============================================================================

def scan_module(module_name: str):
    """
    Import one Nipype module and extract its interfaces.
    """

    try:
        module = importlib.import_module(module_name)

    except Exception as exc:

        return None, {
            "module": module_name,
            "error": str(exc),
        }

    interfaces = {}

    for name, obj in inspect.getmembers(module, inspect.isclass):

        if name.startswith("_"):
            continue

        # Only classes actually defined in this module.
        #
        # This avoids duplicating inherited/imported interfaces.
        try:
            if obj.__module__ != module_name:
                continue
        except Exception:
            continue

        if not is_nipype_interface_class(obj):
            continue

        try:
            inputs = get_inputs_from_spec(obj)

            # Some classes don't define inputs.
            if not inputs:
                inputs = {}

            interface_data = {
                "module": module_name,
                "class": name,
                "description": inspect.getdoc(obj) or "",
                "inputs": inputs,
            }

            interfaces[name] = interface_data

        except Exception as exc:

            interfaces[name] = {
                "module": module_name,
                "class": name,
                "description": inspect.getdoc(obj) or "",
                "inputs": {},
                "error": str(exc),
            }

    return interfaces, None


# ============================================================================
# Generate complete database
# ============================================================================

def generate_database():

    print()
    print("=" * 80)
    print("Nipype interface scanner")
    print("=" * 80)

    print(f"Nipype version : {getattr(nipype, '__version__', 'unknown')}")
    print(f"Python version : {sys.version.split()[0]}")
    print()

    modules = get_all_nipype_modules()

    print(f"Modules found: {len(modules)}")
    print()

    database = {}

    errors = []

    interface_count = 0

    for index, module_name in enumerate(modules, start=1):

        print(
            f"[{index:4d}/{len(modules):4d}] "
            f"{module_name}"
        )

        interfaces, error = scan_module(module_name)

        if error:
            errors.append(error)
            continue

        if not interfaces:
            continue

        for class_name, interface_data in interfaces.items():

            # ---------------------------------------------------------------
            # YAML key
            #
            # Example:
            #
            # ants_ANTS
            # fsl_BET
            # spm_SPM
            #
            # This makes it convenient for your GUI.
            # ---------------------------------------------------------------

            short_module = module_name.replace(
                "nipype.interfaces.",
                "",
            )

            # First component is normally the package
            package = short_module.split(".")[0]

            key = f"{package}_{class_name}"

            # Avoid accidental duplicate keys
            original_key = key
            counter = 2

            while key in database:

                key = f"{original_key}_{counter}"
                counter += 1

            database[key] = interface_data

            interface_count += 1

    # =========================================================================
    # Build final YAML structure
    # =========================================================================

    result = {
        "_metadata": {
            "generator": "generate_nipype_yaml.py",
            "nipype_version": getattr(
                nipype,
                "__version__",
                "unknown",
            ),
            "python_version": sys.version.split()[0],
            "interface_count": interface_count,
            "module_count": len(modules),
            "error_count": len(errors),
        },

        "interfaces": database,
    }

    if errors:

        result["_errors"] = errors

    return result


# ============================================================================
# YAML output
# ============================================================================

def write_yaml(data, output_file):

    output_path = Path(output_file)

    with output_path.open(
        "w",
        encoding="utf-8",
    ) as f:

        yaml.safe_dump(
            data,
            f,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
            width=160,
        )

    print()
    print("=" * 80)
    print("Generation finished")
    print("=" * 80)
    print()
    print(f"Output file : {output_path.resolve()}")

    metadata = data.get("_metadata", {})

    print(
        f"Interfaces  : "
        f"{metadata.get('interface_count', 0)}"
    )

    print(
        f"Modules     : "
        f"{metadata.get('module_count', 0)}"
    )

    print(
        f"Errors      : "
        f"{metadata.get('error_count', 0)}"
    )


# ============================================================================
# Main
# ============================================================================

def main():

    output_file = (
        sys.argv[1]
        if len(sys.argv) > 1
        else DEFAULT_OUTPUT
    )

    try:

        import yaml  # noqa: F401

    except ImportError:

        print(
            "ERROR: PyYAML is not installed."
        )

        print()
        print(
            "Install it with:"
        )

        print(
            "    pip install pyyaml"
        )

        sys.exit(1)

    data = generate_database()

    write_yaml(
        data,
        output_file,
    )


if __name__ == "__main__":
    main()