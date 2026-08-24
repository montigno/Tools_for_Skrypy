class minc_Average:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.minc.minc import Average
        at = Average()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_BBox:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import BBox
        at = BBox()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_Beast:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, library_dir="path", input_file="path", **options):
        from nipype.interfaces.minc.minc import Beast
        at = Beast()
        at.inputs.library_dir = library_dir
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_BestLinReg:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source="path", target="path", **options):
        from nipype.interfaces.minc.minc import BestLinReg
        at = BestLinReg()
        at.inputs.source = source
        at.inputs.target = target
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_xfm(self) -> None:
        return self.res.outputs.output_xfm

    def output_mnc(self) -> None:
        return self.res.outputs.output_mnc

###############################################################################


class minc_BigAverage:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_files=["path"], **options):
        from nipype.interfaces.minc.minc import BigAverage
        at = BigAverage()
        at.inputs.input_files = input_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

    def sd_file(self) -> None:
        return self.res.outputs.sd_file

###############################################################################


class minc_Blob:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Blob
        at = Blob()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_Blur:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Blur
        at = Blur()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

    def gradient_dxyz(self) -> None:
        return self.res.outputs.gradient_dxyz

    def partial_dx(self) -> None:
        return self.res.outputs.partial_dx

    def partial_dy(self) -> None:
        return self.res.outputs.partial_dy

    def partial_dz(self) -> None:
        return self.res.outputs.partial_dz

    def partial_dxyz(self) -> None:
        return self.res.outputs.partial_dxyz

###############################################################################


class minc_Calc:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_files=["path"], **options):
        from nipype.interfaces.minc.minc import Calc
        at = Calc()
        at.inputs.input_files = input_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_Convert:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Convert
        at = Convert()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_Copy:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Copy
        at = Copy()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_Dump:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Dump
        at = Dump()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_Extract:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Extract
        at = Extract()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_Gennlxfm:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.minc.minc import Gennlxfm
        at = Gennlxfm()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

    def output_grid(self) -> None:
        return self.res.outputs.output_grid

###############################################################################


class minc_Math:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.minc.minc import Math
        at = Math()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_NlpFit:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source="path", target="path", config_file="path", init_xfm="path", source_mask="path", **options):
        from nipype.interfaces.minc.minc import NlpFit
        at = NlpFit()
        at.inputs.source = source
        at.inputs.target = target
        at.inputs.config_file = config_file
        at.inputs.init_xfm = init_xfm
        at.inputs.source_mask = source_mask
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_xfm(self) -> None:
        return self.res.outputs.output_xfm

    def output_grid(self) -> None:
        return self.res.outputs.output_grid

###############################################################################


class minc_Norm:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Norm
        at = Norm()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

    def output_threshold_mask(self) -> None:
        return self.res.outputs.output_threshold_mask

###############################################################################


class minc_Pik:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Pik
        at = Pik()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_Resample:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Resample
        at = Resample()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_Reshape:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Reshape
        at = Reshape()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_ToEcat:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import ToEcat
        at = ToEcat()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_ToRaw:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import ToRaw
        at = ToRaw()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_VolSymm:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import VolSymm
        at = VolSymm()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

    def trans_file(self) -> None:
        return self.res.outputs.trans_file

    def output_grid(self) -> None:
        return self.res.outputs.output_grid

###############################################################################


class minc_Volcentre:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Volcentre
        at = Volcentre()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_Voliso:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Voliso
        at = Voliso()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_Volpad:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import Volpad
        at = Volpad()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class minc_XfmAvg:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_files=["path"], **options):
        from nipype.interfaces.minc.minc import XfmAvg
        at = XfmAvg()
        at.inputs.input_files = input_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

    def output_grid(self) -> None:
        return self.res.outputs.output_grid

###############################################################################


class minc_XfmConcat:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_files=["path"], **options):
        from nipype.interfaces.minc.minc import XfmConcat
        at = XfmConcat()
        at.inputs.input_files = input_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

    def output_grids(self) -> list[None]:
        return self.res.outputs.output_grids

###############################################################################


class minc_XfmInvert:
    """
    Note:
        dependencies: Nipype,minc
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", **options):
        from nipype.interfaces.minc.minc import XfmInvert
        at = XfmInvert()
        at.inputs.input_file = input_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

    def output_grid(self) -> None:
        return self.res.outputs.output_grid

###############################################################################


