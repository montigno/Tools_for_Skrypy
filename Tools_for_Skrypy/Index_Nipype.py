import importlib
import inspect
import pkgutil
import nipype.interfaces.fsl as fsl


def nipype_doc_url(cls):
    module = cls.__module__
    name = cls.__name__
    return (
        "https://nipype.readthedocs.io/en/latest/api/generated/"
        f"{module}.html#{module}.{name}"
    )


def build_fsl_index():
    index = {}

    # Parcours récursif de nipype.interfaces.fsl
    for _, modname, _ in pkgutil.walk_packages(
        fsl.__path__,
        fsl.__name__ + "."
    ):
        try:
            module = importlib.import_module(modname)
        except Exception:
            continue

        for attr_name in dir(module):
            obj = getattr(module, attr_name)

            # on garde uniquement les classes Nipype
            if inspect.isclass(obj) and obj.__module__.startswith("nipype.interfaces.fsl"):
                key = f"fsl_{obj.__name__}"
                index[key] = {
                    "class": obj,
                    "module": obj.__module__,
                    "url": nipype_doc_url(obj)
                }

    return index

index = build_fsl_index()

print(index["fsl_BinaryMaths"]["url"])

simple_index = {
    k: v["url"]
    for k, v in build_fsl_index().items()
}