class image_Reorient:
    """
    Note:
        dependencies: Nipype,image
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.image import Reorient
        at = Reorient()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def transform(self) -> None:
        return self.res.outputs.transform

###############################################################################


class image_Rescale:
    """
    Note:
        dependencies: Nipype,image
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", ref_file="path", **options):
        from nipype.interfaces.image import Rescale
        at = Rescale()
        at.inputs.in_file = in_file
        at.inputs.ref_file = ref_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class image_SimpleInterface:
    """
    Note:
        dependencies: Nipype,image
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


