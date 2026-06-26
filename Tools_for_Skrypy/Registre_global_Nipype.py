import importlib
import inspect
import pkgutil
from difflib import get_close_matches

import nipype.interfaces.fsl as fsl
import nipype.interfaces.spm as spm
import nipype.interfaces.ants as ants
import nipype.interfaces.afni as afni


def nipype_doc_url(cls):
    module = cls.__module__
    name = cls.__name__
    return (
        "https://nipype.readthedocs.io/en/latest/api/generated/"
        f"{module}.html#{module}.{name}"
    )


def build_index(package, prefix):
    index = {}

    for _, modname, _ in pkgutil.walk_packages(
        package.__path__,
        package.__name__ + "."
    ):
        try:
            module = importlib.import_module(modname)
        except Exception:
            continue

        for name, obj in vars(module).items():
            if inspect.isclass(obj) and obj.__module__.startswith(package.__name__):
                key = f"{prefix}_{obj.__name__}"

                index[key] = {
                    "class": obj,
                    "module": obj.__module__,
                    "url": nipype_doc_url(obj),
                    "name": obj.__name__.lower(),
                    "module_short": modname.split(".")[-1].lower()
                }

    return index

def build_global_index():
    return {
        **build_index(fsl, "fsl"),
        **build_index(spm, "spm"),
        **build_index(ants, "ants"),
        **build_index(afni, "afni"),
    }

def search(index, query, limit=5):
    query = query.lower()

    keys = list(index.keys())

    # 1) match exact
    exact = [k for k in keys if query in k.lower()]
    if exact:
        return exact[:limit]

    # 2) fuzzy match
    matches = get_close_matches(query, keys, n=limit, cutoff=0.3)
    return matches

def pretty_search(index, query):
    results = search(index, query)

    return [
        {
            "key": k,
            "class": index[k]["class"].__name__,
            "module": index[k]["module"],
            "url": index[k]["url"]
        }
        for k in results
    ]

index = build_global_index()

print(len(index))

print(pretty_search(index, "binary"))
