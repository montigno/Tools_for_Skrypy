import inspect
from nipype.interfaces import fsl
from nipype.interfaces.base import BaseInterface

def is_interface(obj):
    return inspect.isclass(obj) and issubclass(obj, BaseInterface)

def list_all_interfaces(module):
    return [obj for name, obj in inspect.getmembers(module) if is_interface(obj)]

def list_inputs(interface):
    inputs = interface().inputs
    mandatory = []
    optional = []

    for name, trait in inputs.traits().items():
        if name.startswith('_'):
            continue
        
        if trait.mandatory:
            mandatory.append(name)
        else:
            optional.append(name)

    return mandatory, optional


interfaces = list_all_interfaces(fsl)

for iface in interfaces:
    try:
        mand, opt = list_inputs(iface)
        print(f"\nInterface: {iface.__name__}")
        print(f"  Mandatory: {mand}")
        print(f"  Optional: {opt}")
    except Exception as e:
        print(f"Skipping {iface.__name__}: {e}")