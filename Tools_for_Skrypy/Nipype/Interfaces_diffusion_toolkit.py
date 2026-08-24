class diffusion_toolkit_DTIRecon:
    """
    Note:
        dependencies: Nipype,diffusion_toolkit
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, DWI="path", bvecs="path", bvals="path", **options):
        from nipype.interfaces.diffusion_toolkit.dti import DTIRecon
        at = DTIRecon()
        at.inputs.DWI = DWI
        at.inputs.bvecs = bvecs
        at.inputs.bvals = bvals
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def ADC(self) -> None:
        return self.res.outputs.ADC

    def B0(self) -> None:
        return self.res.outputs.B0

    def L1(self) -> None:
        return self.res.outputs.L1

    def L2(self) -> None:
        return self.res.outputs.L2

    def L3(self) -> None:
        return self.res.outputs.L3

    def exp(self) -> None:
        return self.res.outputs.exp

    def FA(self) -> None:
        return self.res.outputs.FA

    def FA_color(self) -> None:
        return self.res.outputs.FA_color

    def tensor(self) -> None:
        return self.res.outputs.tensor

    def V1(self) -> None:
        return self.res.outputs.V1

    def V2(self) -> None:
        return self.res.outputs.V2

    def V3(self) -> None:
        return self.res.outputs.V3

###############################################################################


class diffusion_toolkit_DTITracker:
    """
    Note:
        dependencies: Nipype,diffusion_toolkit
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, mask1_file="path", **options):
        from nipype.interfaces.diffusion_toolkit.dti import DTITracker
        at = DTITracker()
        at.inputs.mask1_file = mask1_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def track_file(self) -> None:
        return self.res.outputs.track_file

    def mask_file(self) -> None:
        return self.res.outputs.mask_file

###############################################################################


class diffusion_toolkit_HARDIMat:
    """
    Note:
        dependencies: Nipype,diffusion_toolkit
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, bvecs="path", bvals="path", **options):
        from nipype.interfaces.diffusion_toolkit.odf import HARDIMat
        at = HARDIMat()
        at.inputs.bvecs = bvecs
        at.inputs.bvals = bvals
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class diffusion_toolkit_ODFRecon:
    """
    Note:
        dependencies: Nipype,diffusion_toolkit
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, DWI="path", n_directions=0, n_output_directions=0, matrix="path", n_b0=0, **options):
        from nipype.interfaces.diffusion_toolkit.odf import ODFRecon
        at = ODFRecon()
        at.inputs.DWI = DWI
        at.inputs.n_directions = n_directions
        at.inputs.n_output_directions = n_output_directions
        at.inputs.matrix = matrix
        at.inputs.n_b0 = n_b0
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def B0(self) -> None:
        return self.res.outputs.B0

    def DWI(self) -> None:
        return self.res.outputs.DWI

    def max(self) -> None:
        return self.res.outputs.max

    def ODF(self) -> None:
        return self.res.outputs.ODF

    def entropy(self) -> None:
        return self.res.outputs.entropy

###############################################################################


class diffusion_toolkit_ODFTracker:
    """
    Note:
        dependencies: Nipype,diffusion_toolkit
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, max="path", ODF="path", mask1_file="path", **options):
        from nipype.interfaces.diffusion_toolkit.odf import ODFTracker
        at = ODFTracker()
        at.inputs.max = max
        at.inputs.ODF = ODF
        at.inputs.mask1_file = mask1_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def track_file(self) -> None:
        return self.res.outputs.track_file

###############################################################################


class diffusion_toolkit_SplineFilter:
    """
    Note:
        dependencies: Nipype,diffusion_toolkit
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, track_file="path", step_length=0.0, **options):
        from nipype.interfaces.diffusion_toolkit.postproc import SplineFilter
        at = SplineFilter()
        at.inputs.track_file = track_file
        at.inputs.step_length = step_length
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def smoothed_track_file(self) -> None:
        return self.res.outputs.smoothed_track_file

###############################################################################


class diffusion_toolkit_TrackMerge:
    """
    Note:
        dependencies: Nipype,diffusion_toolkit
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, track_files=["path"], **options):
        from nipype.interfaces.diffusion_toolkit.postproc import TrackMerge
        at = TrackMerge()
        at.inputs.track_files = track_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def track_file(self) -> None:
        return self.res.outputs.track_file

###############################################################################


