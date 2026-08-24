class dcm2nii_Dcm2nii:
    """
    Note:
        dependencies: Nipype,dcm2nii
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.dcm2nii import Dcm2nii
        at = Dcm2nii()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def converted_files(self) -> list[None]:
        return self.res.outputs.converted_files

    def reoriented_files(self) -> list[None]:
        return self.res.outputs.reoriented_files

    def reoriented_and_cropped_files(self) -> list[None]:
        return self.res.outputs.reoriented_and_cropped_files

    def bvecs(self) -> list[None]:
        return self.res.outputs.bvecs

    def bvals(self) -> list[None]:
        return self.res.outputs.bvals

###############################################################################


class dcm2nii_Dcm2niix:
    """
    Note:
        dependencies: Nipype,dcm2nii
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.dcm2nii import Dcm2niix
        at = Dcm2niix()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def converted_files(self) -> list[None]:
        return self.res.outputs.converted_files

    def bvecs(self) -> list[None]:
        return self.res.outputs.bvecs

    def mvecs(self) -> list[None]:
        return self.res.outputs.mvecs

    def bvals(self) -> list[None]:
        return self.res.outputs.bvals

    def bids(self) -> list[None]:
        return self.res.outputs.bids

###############################################################################


