class nipy_ComputeMask:
    """
    Note:
        dependencies: Nipype,nipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, mean_volume="path", **options):
        from nipype.interfaces.nipy.preprocess import ComputeMask
        at = ComputeMask()
        at.inputs.mean_volume = mean_volume
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def brain_mask(self) -> None:
        return self.res.outputs.brain_mask

###############################################################################


class nipy_EstimateContrast:
    """
    Note:
        dependencies: Nipype,nipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, contrasts=[(0,)], beta="path", nvbeta='', s2="path", dof='', constants='', axis='', reg_names=[''], **options):
        from nipype.interfaces.nipy.model import EstimateContrast
        at = EstimateContrast()
        at.inputs.contrasts = contrasts
        at.inputs.beta = beta
        at.inputs.nvbeta = nvbeta
        at.inputs.s2 = s2
        at.inputs.dof = dof
        at.inputs.constants = constants
        at.inputs.axis = axis
        at.inputs.reg_names = reg_names
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def stat_maps(self) -> list[None]:
        return self.res.outputs.stat_maps

    def z_maps(self) -> list[None]:
        return self.res.outputs.z_maps

    def p_maps(self) -> list[None]:
        return self.res.outputs.p_maps

###############################################################################


class nipy_FitGLM:
    """
    Note:
        dependencies: Nipype,nipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, session_info='', TR=0.0, **options):
        from nipype.interfaces.nipy.model import FitGLM
        at = FitGLM()
        at.inputs.session_info = session_info
        at.inputs.TR = TR
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def beta(self) -> None:
        return self.res.outputs.beta

    def nvbeta(self) -> str:
        return self.res.outputs.nvbeta

    def s2(self) -> None:
        return self.res.outputs.s2

    def dof(self) -> str:
        return self.res.outputs.dof

    def constants(self) -> str:
        return self.res.outputs.constants

    def axis(self) -> str:
        return self.res.outputs.axis

    def reg_names(self) -> list[str]:
        return self.res.outputs.reg_names

    def residuals(self) -> None:
        return self.res.outputs.residuals

    def a(self) -> None:
        return self.res.outputs.a

###############################################################################


class nipy_Similarity:
    """
    Note:
        dependencies: Nipype,nipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, volume1="path", volume2="path", **options):
        from nipype.interfaces.nipy.utils import Similarity
        at = Similarity()
        at.inputs.volume1 = volume1
        at.inputs.volume2 = volume2
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def similarity(self) -> float:
        return self.res.outputs.similarity

###############################################################################


class nipy_SpaceTimeRealigner:
    """
    Note:
        dependencies: Nipype,nipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file=["path"], **options):
        from nipype.interfaces.nipy.preprocess import SpaceTimeRealigner
        at = SpaceTimeRealigner()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> list[None]:
        return self.res.outputs.out_file

    def par_file(self) -> list[None]:
        return self.res.outputs.par_file

###############################################################################


