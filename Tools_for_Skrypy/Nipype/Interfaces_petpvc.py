class petpvc_PETPVC:
    """
    Note:
        dependencies: Nipype,petpvc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", mask_file="path", pvc="enumerate(('GTM','IY','IY+RL','IY+VC','LABBE','LABBE+MTC','LABBE+MTC+RL','LABBE+MTC+VC','LABBE+RBV','LABBE+RBV+RL','LABBE+RBV+VC','MG','MG+RL','MG+VC','MTC','MTC+RL','MTC+VC','RBV','RBV+RL','RBV+VC','RL','VC','STC'))", fwhm_x=0.0, fwhm_y=0.0, fwhm_z=0.0, **options):
        from nipype.interfaces.petpvc import PETPVC
        at = PETPVC()
        at.inputs.in_file = in_file
        at.inputs.mask_file = mask_file
        at.inputs.pvc = pvc
        at.inputs.fwhm_x = fwhm_x
        at.inputs.fwhm_y = fwhm_y
        at.inputs.fwhm_z = fwhm_z
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


