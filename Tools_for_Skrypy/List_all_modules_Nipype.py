import nipype.interfaces
import pkgutil
import inspect
import nipype.interfaces.slicer as slicer
from nipype.interfaces.ants import AI


for module in pkgutil.iter_modules(nipype.interfaces.__path__):
    print(module.name)

# i = 0
# for name, obj in inspect.getmembers(slicer, inspect.isclass):
#     print(i, name)
#     i += 1

# ai = AI()
# print(ai.inputs)

# for name, trait in ai.inputs.traits().items():
#
#     print("NAME :", name)
#     print("TYPE :", trait.trait_type)
#     print("DEFAULT :", trait.default_value)
#     print("DESC :", trait.desc)
#     print()
