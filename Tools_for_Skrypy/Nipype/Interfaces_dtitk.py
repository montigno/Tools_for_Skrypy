class dtitk_AffScalarVol:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.dtitk.registration import AffScalarVol
        at = AffScalarVol()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dtitk_AffSymTensor3DVol:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.dtitk.registration import AffSymTensor3DVol
        at = AffSymTensor3DVol()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dtitk_Affine:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, fixed_file="path", moving_file="path", similarity_metric="enumerate(('EDS','GDS','DDS','NMI'))", sampling_xyz=(0,), ftol=0.0, **options):
        from nipype.interfaces.dtitk.registration import Affine
        at = Affine()
        at.inputs.fixed_file = fixed_file
        at.inputs.moving_file = moving_file
        at.inputs.similarity_metric = similarity_metric
        at.inputs.sampling_xyz = sampling_xyz
        at.inputs.ftol = ftol
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_file_xfm(self) -> None:
        return self.res.outputs.out_file_xfm

###############################################################################


class dtitk_BinThresh:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", lower_bound=0.0, upper_bound=0.0, inside_value=0.0, outside_value=0.0, **options):
        from nipype.interfaces.dtitk.utils import BinThresh
        at = BinThresh()
        at.inputs.in_file = in_file
        at.inputs.lower_bound = lower_bound
        at.inputs.upper_bound = upper_bound
        at.inputs.inside_value = inside_value
        at.inputs.outside_value = outside_value
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dtitk_ComposeXfm:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_df="path", in_aff="path", **options):
        from nipype.interfaces.dtitk.registration import ComposeXfm
        at = ComposeXfm()
        at.inputs.in_df = in_df
        at.inputs.in_aff = in_aff
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dtitk_Diffeo:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, legacy='', n_iters=0, ftol=0.0, **options):
        from nipype.interfaces.dtitk.registration import Diffeo
        at = Diffeo()
        at.inputs.legacy = legacy
        at.inputs.n_iters = n_iters
        at.inputs.ftol = ftol
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_file_xfm(self) -> None:
        return self.res.outputs.out_file_xfm

###############################################################################


class dtitk_DiffeoScalarVol:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", transform="path", **options):
        from nipype.interfaces.dtitk.registration import DiffeoScalarVol
        at = DiffeoScalarVol()
        at.inputs.in_file = in_file
        at.inputs.transform = transform
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dtitk_DiffeoSymTensor3DVol:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", transform="path", **options):
        from nipype.interfaces.dtitk.registration import DiffeoSymTensor3DVol
        at = DiffeoSymTensor3DVol()
        at.inputs.in_file = in_file
        at.inputs.transform = transform
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dtitk_Rigid:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, fixed_file="path", moving_file="path", similarity_metric="enumerate(('EDS','GDS','DDS','NMI'))", sampling_xyz=(0,), ftol=0.0, **options):
        from nipype.interfaces.dtitk.registration import Rigid
        at = Rigid()
        at.inputs.fixed_file = fixed_file
        at.inputs.moving_file = moving_file
        at.inputs.similarity_metric = similarity_metric
        at.inputs.sampling_xyz = sampling_xyz
        at.inputs.ftol = ftol
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_file_xfm(self) -> None:
        return self.res.outputs.out_file_xfm

###############################################################################


class dtitk_SVAdjustVoxSp:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.dtitk.utils import SVAdjustVoxSp
        at = SVAdjustVoxSp()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dtitk_SVResample:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.dtitk.utils import SVResample
        at = SVResample()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dtitk_TVAdjustVoxSp:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.dtitk.utils import TVAdjustVoxSp
        at = TVAdjustVoxSp()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dtitk_TVResample:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.dtitk.utils import TVResample
        at = TVResample()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dtitk_TVtool:
    """
    Note:
        dependencies: Nipype,dtitk
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.dtitk.utils import TVtool
        at = TVtool()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


