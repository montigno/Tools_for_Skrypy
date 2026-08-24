class c3_C3d:
    """
    Note:
        dependencies: Nipype,c3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file=["path"], **options):
        from nipype.interfaces.c3 import C3d
        at = C3d()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_files(self) -> list[None]:
        return self.res.outputs.out_files

###############################################################################


class c3_C3dAffineTool:
    """
    Note:
        dependencies: Nipype,c3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.c3 import C3dAffineTool
        at = C3dAffineTool()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def itk_transform(self) -> None:
        return self.res.outputs.itk_transform

###############################################################################


