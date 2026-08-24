class base_BaseInterface:
    """
    Note:
        dependencies: Nipype,base
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.base.core import BaseInterface
        at = BaseInterface()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class base_SimpleInterface:
    """
    Note:
        dependencies: Nipype,base
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.base.core import SimpleInterface
        at = SimpleInterface()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


