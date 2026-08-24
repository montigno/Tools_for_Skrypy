class meshfix_MeshFix:
    """
    Note:
        dependencies: Nipype,meshfix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file1="path", **options):
        from nipype.interfaces.meshfix import MeshFix
        at = MeshFix()
        at.inputs.in_file1 = in_file1
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mesh_file(self) -> None:
        return self.res.outputs.mesh_file

###############################################################################


