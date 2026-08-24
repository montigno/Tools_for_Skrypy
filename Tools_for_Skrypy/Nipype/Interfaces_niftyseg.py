class niftyseg_BinaryMaths:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, operation="enumerate(('mul','div','add','sub','pow','thr','uthr','smo','edge','sobel3','sobel5','min','smol','geo','llsnorm','masknan','hdr_copy','splitinter'))", in_file="path", **options):
        from nipype.interfaces.niftyseg.maths import BinaryMaths
        at = BinaryMaths()
        at.inputs.operation = operation
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyseg_BinaryMathsInteger:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, operation="enumerate(('dil','ero','tp','equal','pad','crop'))", operand_value=0, in_file="path", **options):
        from nipype.interfaces.niftyseg.maths import BinaryMathsInteger
        at = BinaryMathsInteger()
        at.inputs.operation = operation
        at.inputs.operand_value = operand_value
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyseg_BinaryStats:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, operation="enumerate(('p','sa','ss','svp','al','d','ncc','nmi','Vl','Nl'))", in_file="path", **options):
        from nipype.interfaces.niftyseg.stats import BinaryStats
        at = BinaryStats()
        at.inputs.operation = operation
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output(self) -> str:
        return self.res.outputs.output

###############################################################################


class niftyseg_CalcTopNCC:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", num_templates=0, in_templates=["path"], top_templates=0, **options):
        from nipype.interfaces.niftyseg.label_fusion import CalcTopNCC
        at = CalcTopNCC()
        at.inputs.in_file = in_file
        at.inputs.num_templates = num_templates
        at.inputs.in_templates = in_templates
        at.inputs.top_templates = top_templates
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_files(self) -> str:
        return self.res.outputs.out_files

###############################################################################


class niftyseg_EM:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.niftyseg.em import EM
        at = EM()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_bc_file(self) -> None:
        return self.res.outputs.out_bc_file

    def out_outlier_file(self) -> None:
        return self.res.outputs.out_outlier_file

###############################################################################


class niftyseg_FillLesions:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", lesion_mask="path", **options):
        from nipype.interfaces.niftyseg.lesions import FillLesions
        at = FillLesions()
        at.inputs.in_file = in_file
        at.inputs.lesion_mask = lesion_mask
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyseg_LabelFusion:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", file_to_seg="path", classifier_type="enumerate(('STEPS','STAPLE','MV','SBA'))", **options):
        from nipype.interfaces.niftyseg.label_fusion import LabelFusion
        at = LabelFusion()
        at.inputs.in_file = in_file
        at.inputs.file_to_seg = file_to_seg
        at.inputs.classifier_type = classifier_type
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyseg_Merge:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dimension=0, merge_files=["path"], in_file="path", **options):
        from nipype.interfaces.niftyseg.maths import Merge
        at = Merge()
        at.inputs.dimension = dimension
        at.inputs.merge_files = merge_files
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyseg_PatchMatch:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", mask_file="path", database_file="path", **options):
        from nipype.interfaces.niftyseg.patchmatch import PatchMatch
        at = PatchMatch()
        at.inputs.in_file = in_file
        at.inputs.mask_file = mask_file
        at.inputs.database_file = database_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyseg_TupleMaths:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, operation="enumerate(('lncc','lssd','lltsnorm'))", in_file="path", **options):
        from nipype.interfaces.niftyseg.maths import TupleMaths
        at = TupleMaths()
        at.inputs.operation = operation
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyseg_UnaryMaths:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, operation="enumerate(('sqrt','exp','log','recip','abs','bin','otsu','lconcomp','concomp6','concomp26','fill','euc','tpmax','tmean','tmax','tmin','splitlab','removenan','isnan','subsamp2','scl','4to5','range'))", in_file="path", **options):
        from nipype.interfaces.niftyseg.maths import UnaryMaths
        at = UnaryMaths()
        at.inputs.operation = operation
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyseg_UnaryStats:
    """
    Note:
        dependencies: Nipype,niftyseg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, operation="enumerate(('r','R','a','s','v','vl','vp','n','np','e','ne','x','X','c','B','xvox','xdim'))", in_file="path", **options):
        from nipype.interfaces.niftyseg.stats import UnaryStats
        at = UnaryStats()
        at.inputs.operation = operation
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output(self) -> str:
        return self.res.outputs.output

###############################################################################


