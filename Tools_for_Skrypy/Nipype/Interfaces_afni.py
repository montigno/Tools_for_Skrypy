class afni_ABoverlap:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file_a="path", in_file_b="path", **options):
        from nipype.interfaces.afni.utils import ABoverlap
        at = ABoverlap()
        at.inputs.in_file_a = in_file_a
        at.inputs.in_file_b = in_file_b
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_AFNItoNIFTI:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import AFNItoNIFTI
        at = AFNItoNIFTI()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_AlignEpiAnatPy:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", anat="path", epi_base="enumerate(('mean','median','max'))", **options):
        from nipype.interfaces.afni.preprocess import AlignEpiAnatPy
        at = AlignEpiAnatPy()
        at.inputs.in_file = in_file
        at.inputs.anat = anat
        at.inputs.epi_base = epi_base
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def anat_al_orig(self) -> None:
        return self.res.outputs.anat_al_orig

    def epi_al_orig(self) -> None:
        return self.res.outputs.epi_al_orig

    def epi_tlrc_al(self) -> None:
        return self.res.outputs.epi_tlrc_al

    def anat_al_mat(self) -> None:
        return self.res.outputs.anat_al_mat

    def epi_al_mat(self) -> None:
        return self.res.outputs.epi_al_mat

    def epi_vr_al_mat(self) -> None:
        return self.res.outputs.epi_vr_al_mat

    def epi_reg_al_mat(self) -> None:
        return self.res.outputs.epi_reg_al_mat

    def epi_al_tlrc_mat(self) -> None:
        return self.res.outputs.epi_al_tlrc_mat

    def epi_vr_motion(self) -> None:
        return self.res.outputs.epi_vr_motion

    def skullstrip(self) -> None:
        return self.res.outputs.skullstrip

###############################################################################


class afni_Allineate:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import Allineate
        at = Allineate()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_matrix(self) -> None:
        return self.res.outputs.out_matrix

    def out_param_file(self) -> None:
        return self.res.outputs.out_param_file

    def out_weight_file(self) -> None:
        return self.res.outputs.out_weight_file

    def allcostx(self) -> None:
        return self.res.outputs.allcostx

###############################################################################


class afni_AutoTLRC:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", base='', **options):
        from nipype.interfaces.afni.preprocess import AutoTLRC
        at = AutoTLRC()
        at.inputs.in_file = in_file
        at.inputs.base = base
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_AutoTcorrelate:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import AutoTcorrelate
        at = AutoTcorrelate()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Autobox:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import Autobox
        at = Autobox()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def x_min(self) -> int:
        return self.res.outputs.x_min

    def x_max(self) -> int:
        return self.res.outputs.x_max

    def y_min(self) -> int:
        return self.res.outputs.y_min

    def y_max(self) -> int:
        return self.res.outputs.y_max

    def z_min(self) -> int:
        return self.res.outputs.z_min

    def z_max(self) -> int:
        return self.res.outputs.z_max

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Automask:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import Automask
        at = Automask()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def brain_file(self) -> None:
        return self.res.outputs.brain_file

###############################################################################


class afni_Axialize:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import Axialize
        at = Axialize()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Bandpass:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", lowpass=0.0, highpass=0.0, **options):
        from nipype.interfaces.afni.preprocess import Bandpass
        at = Bandpass()
        at.inputs.in_file = in_file
        at.inputs.lowpass = lowpass
        at.inputs.highpass = highpass
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_BlurInMask:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", fwhm=0.0, **options):
        from nipype.interfaces.afni.preprocess import BlurInMask
        at = BlurInMask()
        at.inputs.in_file = in_file
        at.inputs.fwhm = fwhm
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_BlurToFWHM:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import BlurToFWHM
        at = BlurToFWHM()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_BrickStat:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import BrickStat
        at = BrickStat()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def min_val(self) -> float:
        return self.res.outputs.min_val

###############################################################################


class afni_Bucket:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file=[(0,)], **options):
        from nipype.interfaces.afni.utils import Bucket
        at = Bucket()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Calc:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file_a="path", expr='', **options):
        from nipype.interfaces.afni.utils import Calc
        at = Calc()
        at.inputs.in_file_a = in_file_a
        at.inputs.expr = expr
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Cat:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], out_file="path", **options):
        from nipype.interfaces.afni.utils import Cat
        at = Cat()
        at.inputs.in_files = in_files
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_CatMatvec:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file=[(0,)], out_file="path", **options):
        from nipype.interfaces.afni.utils import CatMatvec
        at = CatMatvec()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_CenterMass:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import CenterMass
        at = CenterMass()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def cm_file(self) -> None:
        return self.res.outputs.cm_file

    def cm(self) -> list[tuple]:
        return self.res.outputs.cm

###############################################################################


class afni_ClipLevel:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import ClipLevel
        at = ClipLevel()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def clip_val(self) -> float:
        return self.res.outputs.clip_val

###############################################################################


class afni_ConvertDset:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", out_type="enumerate(('niml','niml_asc','niml_bi','1D','1Dp','1Dpt','gii','gii_asc','gii_b64','gii_b64gz'))", **options):
        from nipype.interfaces.afni.utils import ConvertDset
        at = ConvertDset()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        at.inputs.out_type = out_type
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Copy:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import Copy
        at = Copy()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Deconvolve:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.afni.model import Deconvolve
        at = Deconvolve()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def reml_script(self) -> None:
        return self.res.outputs.reml_script

    def x1D(self) -> None:
        return self.res.outputs.x1D

    def cbucket(self) -> None:
        return self.res.outputs.cbucket

###############################################################################


class afni_DegreeCentrality:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import DegreeCentrality
        at = DegreeCentrality()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def oned_file(self) -> None:
        return self.res.outputs.oned_file

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Despike:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import Despike
        at = Despike()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Detrend:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import Detrend
        at = Detrend()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Dot:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.afni.utils import Dot
        at = Dot()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_ECM:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import ECM
        at = ECM()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Edge3:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import Edge3
        at = Edge3()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Eval:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file_a="path", expr='', **options):
        from nipype.interfaces.afni.utils import Eval
        at = Eval()
        at.inputs.in_file_a = in_file_a
        at.inputs.expr = expr
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_FWHMx:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import FWHMx
        at = FWHMx()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_subbricks(self) -> None:
        return self.res.outputs.out_subbricks

    def out_detrend(self) -> None:
        return self.res.outputs.out_detrend

    def fwhm(self) -> tuple:
        return self.res.outputs.fwhm

    def acf_param(self) -> tuple:
        return self.res.outputs.acf_param

    def out_acf(self) -> None:
        return self.res.outputs.out_acf

###############################################################################


class afni_Fim:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", ideal_file="path", **options):
        from nipype.interfaces.afni.preprocess import Fim
        at = Fim()
        at.inputs.in_file = in_file
        at.inputs.ideal_file = ideal_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Fourier:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", lowpass=0.0, highpass=0.0, **options):
        from nipype.interfaces.afni.preprocess import Fourier
        at = Fourier()
        at.inputs.in_file = in_file
        at.inputs.lowpass = lowpass
        at.inputs.highpass = highpass
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_GCOR:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import GCOR
        at = GCOR()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out(self) -> float:
        return self.res.outputs.out

###############################################################################


class afni_Hist:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import Hist
        at = Hist()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_show(self) -> None:
        return self.res.outputs.out_show

###############################################################################


class afni_LFCD:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import LFCD
        at = LFCD()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_LocalBistat:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file1="path", in_file2="path", neighborhood="enumerate(('SPHERE','RHDD','TOHD'))", stat="enumerate(('pearson','spearman','quadrant','mutinfo','normuti','jointent','hellinger','crU','crM','crA','L2slope','L1slope','num','ALL'))", **options):
        from nipype.interfaces.afni.utils import LocalBistat
        at = LocalBistat()
        at.inputs.in_file1 = in_file1
        at.inputs.in_file2 = in_file2
        at.inputs.neighborhood = neighborhood
        at.inputs.stat = stat
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Localstat:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", neighborhood="enumerate(('SPHERE','RHDD','TOHD'))", stat="enumerate(('mean','stdev','var','cvar','median','MAD','min','max','absmax','num','sum','FWHM','FWHMbar','rank','frank','P2skew','ALL','mMP2s','mmMP2s','perc'))", **options):
        from nipype.interfaces.afni.utils import Localstat
        at = Localstat()
        at.inputs.in_file = in_file
        at.inputs.neighborhood = neighborhood
        at.inputs.stat = stat
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_MaskTool:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file=["path"], **options):
        from nipype.interfaces.afni.utils import MaskTool
        at = MaskTool()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Maskave:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import Maskave
        at = Maskave()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Means:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file_a="path", **options):
        from nipype.interfaces.afni.preprocess import Means
        at = Means()
        at.inputs.in_file_a = in_file_a
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Merge:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.afni.utils import Merge
        at = Merge()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_NetCorr:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", in_rois="path", **options):
        from nipype.interfaces.afni.preprocess import NetCorr
        at = NetCorr()
        at.inputs.in_file = in_file
        at.inputs.in_rois = in_rois
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_corr_matrix(self) -> None:
        return self.res.outputs.out_corr_matrix

    def out_corr_maps(self) -> list[None]:
        return self.res.outputs.out_corr_maps

###############################################################################


class afni_Notes:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import Notes
        at = Notes()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_NwarpAdjust:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, warps="path", **options):
        from nipype.interfaces.afni.utils import NwarpAdjust
        at = NwarpAdjust()
        at.inputs.warps = warps
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_NwarpApply:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file=["path"], warp='', **options):
        from nipype.interfaces.afni.utils import NwarpApply
        at = NwarpApply()
        at.inputs.in_file = in_file
        at.inputs.warp = warp
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_NwarpCat:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files="enumerate(('IDENT','INV','SQRT','SQRTINV'))", **options):
        from nipype.interfaces.afni.utils import NwarpCat
        at = NwarpCat()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_OneDToolPy:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import OneDToolPy
        at = OneDToolPy()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_OutlierCount:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import OutlierCount
        at = OutlierCount()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_outliers(self) -> None:
        return self.res.outputs.out_outliers

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_QualityIndex:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import QualityIndex
        at = QualityIndex()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Qwarp:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", base_file="path", **options):
        from nipype.interfaces.afni.preprocess import Qwarp
        at = Qwarp()
        at.inputs.in_file = in_file
        at.inputs.base_file = base_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def warped_source(self) -> None:
        return self.res.outputs.warped_source

    def warped_base(self) -> None:
        return self.res.outputs.warped_base

    def source_warp(self) -> None:
        return self.res.outputs.source_warp

    def base_warp(self) -> None:
        return self.res.outputs.base_warp

    def weights(self) -> None:
        return self.res.outputs.weights

###############################################################################


class afni_QwarpPlusMinus:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", base_file="path", **options):
        from nipype.interfaces.afni.preprocess import QwarpPlusMinus
        at = QwarpPlusMinus()
        at.inputs.in_file = in_file
        at.inputs.base_file = base_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def warped_source(self) -> None:
        return self.res.outputs.warped_source

    def warped_base(self) -> None:
        return self.res.outputs.warped_base

    def source_warp(self) -> None:
        return self.res.outputs.source_warp

    def base_warp(self) -> None:
        return self.res.outputs.base_warp

    def weights(self) -> None:
        return self.res.outputs.weights

###############################################################################


class afni_ROIStats:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import ROIStats
        at = ROIStats()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_ReHo:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import ReHo
        at = ReHo()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_vals(self) -> None:
        return self.res.outputs.out_vals

###############################################################################


class afni_Refit:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import Refit
        at = Refit()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Remlfit:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], matrix="path", **options):
        from nipype.interfaces.afni.model import Remlfit
        at = Remlfit()
        at.inputs.in_files = in_files
        at.inputs.matrix = matrix
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def var_file(self) -> None:
        return self.res.outputs.var_file

    def rbeta_file(self) -> None:
        return self.res.outputs.rbeta_file

    def glt_file(self) -> None:
        return self.res.outputs.glt_file

    def fitts_file(self) -> None:
        return self.res.outputs.fitts_file

    def errts_file(self) -> None:
        return self.res.outputs.errts_file

    def wherr_file(self) -> None:
        return self.res.outputs.wherr_file

    def ovar(self) -> None:
        return self.res.outputs.ovar

    def obeta(self) -> None:
        return self.res.outputs.obeta

    def obuck(self) -> None:
        return self.res.outputs.obuck

    def oglt(self) -> None:
        return self.res.outputs.oglt

    def ofitts(self) -> None:
        return self.res.outputs.ofitts

    def oerrts(self) -> None:
        return self.res.outputs.oerrts

###############################################################################


class afni_Resample:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import Resample
        at = Resample()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Retroicor:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import Retroicor
        at = Retroicor()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_SVMTest:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, model='', in_file="path", **options):
        from nipype.interfaces.afni.svm import SVMTest
        at = SVMTest()
        at.inputs.model = model
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_SVMTrain:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, ttype='', in_file="path", **options):
        from nipype.interfaces.afni.svm import SVMTrain
        at = SVMTrain()
        at.inputs.ttype = ttype
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def model(self) -> None:
        return self.res.outputs.model

    def alphas(self) -> None:
        return self.res.outputs.alphas

###############################################################################


class afni_Seg:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", mask="path", **options):
        from nipype.interfaces.afni.preprocess import Seg
        at = Seg()
        at.inputs.in_file = in_file
        at.inputs.mask = mask
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_SkullStrip:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import SkullStrip
        at = SkullStrip()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Synthesize:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, cbucket="path", matrix="path", select=[''], **options):
        from nipype.interfaces.afni.model import Synthesize
        at = Synthesize()
        at.inputs.cbucket = cbucket
        at.inputs.matrix = matrix
        at.inputs.select = select
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_TCat:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.afni.utils import TCat
        at = TCat()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_TCatSubBrick:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=[(0,)], **options):
        from nipype.interfaces.afni.utils import TCatSubBrick
        at = TCatSubBrick()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_TCorr1D:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, xset="path", y_1d="path", **options):
        from nipype.interfaces.afni.preprocess import TCorr1D
        at = TCorr1D()
        at.inputs.xset = xset
        at.inputs.y_1d = y_1d
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_TCorrMap:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import TCorrMap
        at = TCorrMap()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mean_file(self) -> None:
        return self.res.outputs.mean_file

    def zmean(self) -> None:
        return self.res.outputs.zmean

    def qmean(self) -> None:
        return self.res.outputs.qmean

    def pmean(self) -> None:
        return self.res.outputs.pmean

    def absolute_threshold(self) -> None:
        return self.res.outputs.absolute_threshold

    def var_absolute_threshold(self) -> None:
        return self.res.outputs.var_absolute_threshold

    def var_absolute_threshold_normalize(self) -> None:
        return self.res.outputs.var_absolute_threshold_normalize

    def correlation_maps(self) -> None:
        return self.res.outputs.correlation_maps

    def correlation_maps_masked(self) -> None:
        return self.res.outputs.correlation_maps_masked

    def average_expr(self) -> None:
        return self.res.outputs.average_expr

    def average_expr_nonzero(self) -> None:
        return self.res.outputs.average_expr_nonzero

    def sum_expr(self) -> None:
        return self.res.outputs.sum_expr

    def histogram(self) -> None:
        return self.res.outputs.histogram

###############################################################################


class afni_TCorrelate:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, xset="path", yset="path", **options):
        from nipype.interfaces.afni.preprocess import TCorrelate
        at = TCorrelate()
        at.inputs.xset = xset
        at.inputs.yset = yset
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_TNorm:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import TNorm
        at = TNorm()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_TProject:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import TProject
        at = TProject()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_TShift:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import TShift
        at = TShift()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def timing_file(self) -> None:
        return self.res.outputs.timing_file

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_TSmooth:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import TSmooth
        at = TSmooth()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_TStat:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import TStat
        at = TStat()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_To3D:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_folder="path", **options):
        from nipype.interfaces.afni.utils import To3D
        at = To3D()
        at.inputs.in_folder = in_folder
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Undump:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import Undump
        at = Undump()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Unifize:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import Unifize
        at = Unifize()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def scale_file(self) -> None:
        return self.res.outputs.scale_file

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Volreg:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import Volreg
        at = Volreg()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def md1d_file(self) -> None:
        return self.res.outputs.md1d_file

    def oned_file(self) -> None:
        return self.res.outputs.oned_file

    def oned_matrix_save(self) -> None:
        return self.res.outputs.oned_matrix_save

###############################################################################


class afni_Warp:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.preprocess import Warp
        at = Warp()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def warp_file(self) -> None:
        return self.res.outputs.warp_file

###############################################################################


class afni_ZCutUp:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.afni.utils import ZCutUp
        at = ZCutUp()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Zcat:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.afni.utils import Zcat
        at = Zcat()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class afni_Zeropad:
    """
    Note:
        dependencies: Nipype,afni
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files="path", **options):
        from nipype.interfaces.afni.utils import Zeropad
        at = Zeropad()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


