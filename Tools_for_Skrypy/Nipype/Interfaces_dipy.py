class dipy_APMQball:
    """
    Note:
        dependencies: Nipype,dipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", in_bval="path", in_bvec="path", **options):
        from nipype.interfaces.dipy.anisotropic_power import APMQball
        at = APMQball()
        at.inputs.in_file = in_file
        at.inputs.in_bval = in_bval
        at.inputs.in_bvec = in_bvec
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dipy_CSD:
    """
    Note:
        dependencies: Nipype,dipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", in_bval="path", in_bvec="path", **options):
        from nipype.interfaces.dipy.reconstruction import CSD
        at = CSD()
        at.inputs.in_file = in_file
        at.inputs.in_bval = in_bval
        at.inputs.in_bvec = in_bvec
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def model(self) -> None:
        return self.res.outputs.model

    def out_fods(self) -> None:
        return self.res.outputs.out_fods

###############################################################################


class dipy_DTI:
    """
    Note:
        dependencies: Nipype,dipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", in_bval="path", in_bvec="path", **options):
        from nipype.interfaces.dipy.tensors import DTI
        at = DTI()
        at.inputs.in_file = in_file
        at.inputs.in_bval = in_bval
        at.inputs.in_bvec = in_bvec
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def fa_file(self) -> None:
        return self.res.outputs.fa_file

    def md_file(self) -> None:
        return self.res.outputs.md_file

    def rd_file(self) -> None:
        return self.res.outputs.rd_file

    def ad_file(self) -> None:
        return self.res.outputs.ad_file

    def color_fa_file(self) -> None:
        return self.res.outputs.color_fa_file

###############################################################################


class dipy_Denoise:
    """
    Note:
        dependencies: Nipype,dipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", noise_model="enumerate(('rician','gaussian'))", **options):
        from nipype.interfaces.dipy.preprocess import Denoise
        at = Denoise()
        at.inputs.in_file = in_file
        at.inputs.noise_model = noise_model
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dipy_EstimateResponseSH:
    """
    Note:
        dependencies: Nipype,dipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_evals="path", in_file="path", in_bval="path", in_bvec="path", **options):
        from nipype.interfaces.dipy.reconstruction import EstimateResponseSH
        at = EstimateResponseSH()
        at.inputs.in_evals = in_evals
        at.inputs.in_file = in_file
        at.inputs.in_bval = in_bval
        at.inputs.in_bvec = in_bvec
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def response(self) -> None:
        return self.res.outputs.response

    def out_mask(self) -> None:
        return self.res.outputs.out_mask

###############################################################################


class dipy_RESTORE:
    """
    Note:
        dependencies: Nipype,dipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", in_bval="path", in_bvec="path", **options):
        from nipype.interfaces.dipy.reconstruction import RESTORE
        at = RESTORE()
        at.inputs.in_file = in_file
        at.inputs.in_bval = in_bval
        at.inputs.in_bvec = in_bvec
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def fa(self) -> None:
        return self.res.outputs.fa

    def md(self) -> None:
        return self.res.outputs.md

    def rd(self) -> None:
        return self.res.outputs.rd

    def mode(self) -> None:
        return self.res.outputs.mode

    def trace(self) -> None:
        return self.res.outputs.trace

    def evals(self) -> None:
        return self.res.outputs.evals

    def evecs(self) -> None:
        return self.res.outputs.evecs

###############################################################################


class dipy_Resample:
    """
    Note:
        dependencies: Nipype,dipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", interp=0, **options):
        from nipype.interfaces.dipy.preprocess import Resample
        at = Resample()
        at.inputs.in_file = in_file
        at.inputs.interp = interp
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dipy_SimulateMultiTensor:
    """
    Note:
        dependencies: Nipype,dipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_dirs=["path"], in_frac=["path"], in_vfms=["path"], baseline="path", **options):
        from nipype.interfaces.dipy.simulate import SimulateMultiTensor
        at = SimulateMultiTensor()
        at.inputs.in_dirs = in_dirs
        at.inputs.in_frac = in_frac
        at.inputs.in_vfms = in_vfms
        at.inputs.baseline = baseline
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_mask(self) -> None:
        return self.res.outputs.out_mask

    def out_bvec(self) -> None:
        return self.res.outputs.out_bvec

    def out_bval(self) -> None:
        return self.res.outputs.out_bval

###############################################################################


class dipy_StreamlineTractography:
    """
    Note:
        dependencies: Nipype,dipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", gfa_thresh=0.0, peak_threshold=0.0, min_angle=0.0, multiprocess=True, save_seeds=True, num_seeds=0, **options):
        from nipype.interfaces.dipy.tracks import StreamlineTractography
        at = StreamlineTractography()
        at.inputs.in_file = in_file
        at.inputs.gfa_thresh = gfa_thresh
        at.inputs.peak_threshold = peak_threshold
        at.inputs.min_angle = min_angle
        at.inputs.multiprocess = multiprocess
        at.inputs.save_seeds = save_seeds
        at.inputs.num_seeds = num_seeds
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracks(self) -> None:
        return self.res.outputs.tracks

    def gfa(self) -> None:
        return self.res.outputs.gfa

    def odf_peaks(self) -> None:
        return self.res.outputs.odf_peaks

    def out_seeds(self) -> None:
        return self.res.outputs.out_seeds

###############################################################################


class dipy_TensorMode:
    """
    Note:
        dependencies: Nipype,dipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", in_bval="path", in_bvec="path", **options):
        from nipype.interfaces.dipy.tensors import TensorMode
        at = TensorMode()
        at.inputs.in_file = in_file
        at.inputs.in_bval = in_bval
        at.inputs.in_bvec = in_bvec
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dipy_TrackDensityMap:
    """
    Note:
        dependencies: Nipype,dipy
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.dipy.tracks import TrackDensityMap
        at = TrackDensityMap()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


