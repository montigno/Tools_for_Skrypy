class vista_Vnifti2Image:
    """
    Note:
        dependencies: Nipype,vista
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.vista.vista import Vnifti2Image
        at = Vnifti2Image()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class vista_VtoMat:
    """
    Note:
        dependencies: Nipype,vista
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.vista.vista import VtoMat
        at = VtoMat()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


