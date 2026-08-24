class quickshear_Quickshear:
    """
    Note:
        dependencies: Nipype,quickshear
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", mask_file="path", **options):
        from nipype.interfaces.quickshear import Quickshear
        at = Quickshear()
        at.inputs.in_file = in_file
        at.inputs.mask_file = mask_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


