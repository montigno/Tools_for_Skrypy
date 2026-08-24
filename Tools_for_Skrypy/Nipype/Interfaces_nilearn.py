class nilearn_NilearnBaseInterface:
    """
    Note:
        dependencies: Nipype,nilearn
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.nilearn import NilearnBaseInterface
        at = NilearnBaseInterface()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class nilearn_SignalExtraction:
    """
    Note:
        dependencies: Nipype,nilearn
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", label_files=["path"], class_labels=[''], **options):
        from nipype.interfaces.nilearn import SignalExtraction
        at = SignalExtraction()
        at.inputs.in_file = in_file
        at.inputs.label_files = label_files
        at.inputs.class_labels = class_labels
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class nilearn_SimpleInterface:
    """
    Note:
        dependencies: Nipype,nilearn
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


