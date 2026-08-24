class mixins_CopyHeaderInterface:
    """
    Note:
        dependencies: Nipype,mixins
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mixins.fixheader import CopyHeaderInterface
        at = CopyHeaderInterface()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class mixins_ReportCapableInterface:
    """
    Note:
        dependencies: Nipype,mixins
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mixins.reporting import ReportCapableInterface
        at = ReportCapableInterface()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


