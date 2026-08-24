class bru2nii_Bru2:
    """
    Note:
        dependencies: Nipype,bru2nii
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_dir="path", **options):
        from nipype.interfaces.bru2nii import Bru2
        at = Bru2()
        at.inputs.input_dir = input_dir
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def nii_file(self) -> None:
        return self.res.outputs.nii_file

###############################################################################


