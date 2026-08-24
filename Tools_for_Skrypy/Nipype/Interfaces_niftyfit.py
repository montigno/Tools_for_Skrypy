class niftyfit_DwiTool:
    """
    Note:
        dependencies: Nipype,niftyfit
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source_file="path", bval_file="path", **options):
        from nipype.interfaces.niftyfit.dwi import DwiTool
        at = DwiTool()
        at.inputs.source_file = source_file
        at.inputs.bval_file = bval_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mcmap_file(self) -> None:
        return self.res.outputs.mcmap_file

    def syn_file(self) -> None:
        return self.res.outputs.syn_file

    def mdmap_file(self) -> None:
        return self.res.outputs.mdmap_file

    def famap_file(self) -> None:
        return self.res.outputs.famap_file

    def v1map_file(self) -> None:
        return self.res.outputs.v1map_file

    def rgbmap_file(self) -> None:
        return self.res.outputs.rgbmap_file

    def logdti_file(self) -> None:
        return self.res.outputs.logdti_file

###############################################################################


class niftyfit_FitAsl:
    """
    Note:
        dependencies: Nipype,niftyfit
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source_file="path", **options):
        from nipype.interfaces.niftyfit.asl import FitAsl
        at = FitAsl()
        at.inputs.source_file = source_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def cbf_file(self) -> None:
        return self.res.outputs.cbf_file

    def error_file(self) -> None:
        return self.res.outputs.error_file

    def syn_file(self) -> None:
        return self.res.outputs.syn_file

###############################################################################


class niftyfit_FitDwi:
    """
    Note:
        dependencies: Nipype,niftyfit
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source_file="path", bval_file="path", bvec_file="path", **options):
        from nipype.interfaces.niftyfit.dwi import FitDwi
        at = FitDwi()
        at.inputs.source_file = source_file
        at.inputs.bval_file = bval_file
        at.inputs.bvec_file = bvec_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def error_file(self) -> None:
        return self.res.outputs.error_file

    def res_file(self) -> None:
        return self.res.outputs.res_file

    def syn_file(self) -> None:
        return self.res.outputs.syn_file

    def nodiff_file(self) -> None:
        return self.res.outputs.nodiff_file

    def mdmap_file(self) -> None:
        return self.res.outputs.mdmap_file

    def famap_file(self) -> None:
        return self.res.outputs.famap_file

    def v1map_file(self) -> None:
        return self.res.outputs.v1map_file

    def rgbmap_file(self) -> None:
        return self.res.outputs.rgbmap_file

    def tenmap_file(self) -> None:
        return self.res.outputs.tenmap_file

    def tenmap2_file(self) -> None:
        return self.res.outputs.tenmap2_file

    def mcmap_file(self) -> None:
        return self.res.outputs.mcmap_file

    def mcout(self) -> None:
        return self.res.outputs.mcout

###############################################################################


class niftyfit_FitQt1:
    """
    Note:
        dependencies: Nipype,niftyfit
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source_file="path", **options):
        from nipype.interfaces.niftyfit.qt1 import FitQt1
        at = FitQt1()
        at.inputs.source_file = source_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def t1map_file(self) -> None:
        return self.res.outputs.t1map_file

    def m0map_file(self) -> None:
        return self.res.outputs.m0map_file

    def mcmap_file(self) -> None:
        return self.res.outputs.mcmap_file

    def comp_file(self) -> None:
        return self.res.outputs.comp_file

    def error_file(self) -> None:
        return self.res.outputs.error_file

    def syn_file(self) -> None:
        return self.res.outputs.syn_file

    def res_file(self) -> None:
        return self.res.outputs.res_file

###############################################################################


