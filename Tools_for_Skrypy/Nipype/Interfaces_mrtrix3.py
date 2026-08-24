class mrtrix3_ACTPrepareFSL:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.preprocess import ACTPrepareFSL
        at = ACTPrepareFSL()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_BrainMask:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.utils import BrainMask
        at = BrainMask()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_BuildConnectome:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.connectivity import BuildConnectome
        at = BuildConnectome()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_ComputeTDI:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix3.utils import ComputeTDI
        at = ComputeTDI()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_ConstrainedSphericalDeconvolution:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, algorithm="enumerate(('csd','msmt_csd'))", in_file="path", wm_txt="path", wm_odf="path", **options):
        from nipype.interfaces.mrtrix3.reconst import ConstrainedSphericalDeconvolution
        at = ConstrainedSphericalDeconvolution()
        at.inputs.algorithm = algorithm
        at.inputs.in_file = in_file
        at.inputs.wm_txt = wm_txt
        at.inputs.wm_odf = wm_odf
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def wm_odf(self) -> None:
        return self.res.outputs.wm_odf

    def gm_odf(self) -> None:
        return self.res.outputs.gm_odf

    def csf_odf(self) -> None:
        return self.res.outputs.csf_odf

    def predicted_signal(self) -> None:
        return self.res.outputs.predicted_signal

###############################################################################


class mrtrix3_DWIBiasCorrect:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix3.preprocess import DWIBiasCorrect
        at = DWIBiasCorrect()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def bias(self) -> None:
        return self.res.outputs.bias

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_DWIDenoise:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix3.preprocess import DWIDenoise
        at = DWIDenoise()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def noise(self) -> None:
        return self.res.outputs.noise

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_DWIExtract:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.utils import DWIExtract
        at = DWIExtract()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_DWIPreproc:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", rpe_options="enumerate(('none','pair','all','header'))", **options):
        from nipype.interfaces.mrtrix3.preprocess import DWIPreproc
        at = DWIPreproc()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        at.inputs.rpe_options = rpe_options
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_grad_mrtrix(self) -> None:
        return self.res.outputs.out_grad_mrtrix

    def out_fsl_bvec(self) -> None:
        return self.res.outputs.out_fsl_bvec

    def out_fsl_bval(self) -> None:
        return self.res.outputs.out_fsl_bval

###############################################################################


class mrtrix3_EstimateFOD:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, algorithm="enumerate(('csd','msmt_csd'))", in_file="path", wm_txt="path", wm_odf="path", **options):
        from nipype.interfaces.mrtrix3.reconst import EstimateFOD
        at = EstimateFOD()
        at.inputs.algorithm = algorithm
        at.inputs.in_file = in_file
        at.inputs.wm_txt = wm_txt
        at.inputs.wm_odf = wm_odf
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def wm_odf(self) -> None:
        return self.res.outputs.wm_odf

    def gm_odf(self) -> None:
        return self.res.outputs.gm_odf

    def csf_odf(self) -> None:
        return self.res.outputs.csf_odf

    def predicted_signal(self) -> None:
        return self.res.outputs.predicted_signal

###############################################################################


class mrtrix3_FitTensor:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.reconst import FitTensor
        at = FitTensor()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def predicted_signal(self) -> None:
        return self.res.outputs.predicted_signal

###############################################################################


class mrtrix3_Generate5tt:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, algorithm="enumerate(('fsl','gif','freesurfer','hsvs'))", in_file="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.utils import Generate5tt
        at = Generate5tt()
        at.inputs.algorithm = algorithm
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_Generate5tt2gmwmi:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", mask_out="path", **options):
        from nipype.interfaces.mrtrix3.utils import Generate5tt2gmwmi
        at = Generate5tt2gmwmi()
        at.inputs.in_file = in_file
        at.inputs.mask_out = mask_out
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mask_out(self) -> None:
        return self.res.outputs.mask_out

###############################################################################


class mrtrix3_LabelConfig:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.connectivity import LabelConfig
        at = LabelConfig()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_LabelConvert:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", in_lut="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.connectivity import LabelConvert
        at = LabelConvert()
        at.inputs.in_file = in_file
        at.inputs.in_lut = in_lut
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_MRCat:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], out_file="path", **options):
        from nipype.interfaces.mrtrix3.utils import MRCat
        at = MRCat()
        at.inputs.in_files = in_files
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_MRConvert:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.utils import MRConvert
        at = MRConvert()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def json_export(self) -> None:
        return self.res.outputs.json_export

    def out_bvec(self) -> None:
        return self.res.outputs.out_bvec

    def out_bval(self) -> None:
        return self.res.outputs.out_bval

###############################################################################


class mrtrix3_MRDeGibbs:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix3.preprocess import MRDeGibbs
        at = MRDeGibbs()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_MRMath:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", operation="enumerate(('mean','median','sum','product','rms','norm','var','std','min','max','absmax','magmax'))", **options):
        from nipype.interfaces.mrtrix3.utils import MRMath
        at = MRMath()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        at.inputs.operation = operation
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_MRResize:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix3.utils import MRResize
        at = MRResize()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_MRTransform:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.mrtrix3.utils import MRTransform
        at = MRTransform()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_MTNormalise:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mrtrix3.utils import MTNormalise
        at = MTNormalise()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file_wm(self) -> None:
        return self.res.outputs.out_file_wm

    def out_file_gm(self) -> None:
        return self.res.outputs.out_file_gm

    def out_file_csf(self) -> None:
        return self.res.outputs.out_file_csf

###############################################################################


class mrtrix3_MaskFilter:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", filter='', out_file="path", **options):
        from nipype.interfaces.mrtrix3.utils import MaskFilter
        at = MaskFilter()
        at.inputs.in_file = in_file
        at.inputs.filter = filter
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_Mesh2PVE:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", reference="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.utils import Mesh2PVE
        at = Mesh2PVE()
        at.inputs.in_file = in_file
        at.inputs.reference = reference
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_ReplaceFSwithFIRST:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", in_t1w="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.preprocess import ReplaceFSwithFIRST
        at = ReplaceFSwithFIRST()
        at.inputs.in_file = in_file
        at.inputs.in_t1w = in_t1w
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_ResponseSD:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, algorithm="enumerate(('msmt_5tt','dhollander','tournier','tax'))", in_file="path", **options):
        from nipype.interfaces.mrtrix3.preprocess import ResponseSD
        at = ResponseSD()
        at.inputs.algorithm = algorithm
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def wm_file(self) -> None:
        return self.res.outputs.wm_file

    def gm_file(self) -> None:
        return self.res.outputs.gm_file

    def csf_file(self) -> None:
        return self.res.outputs.csf_file

###############################################################################


class mrtrix3_SH2Amp:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", directions="path", **options):
        from nipype.interfaces.mrtrix3.utils import SH2Amp
        at = SH2Amp()
        at.inputs.in_file = in_file
        at.inputs.directions = directions
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_SHConv:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", response="path", **options):
        from nipype.interfaces.mrtrix3.utils import SHConv
        at = SHConv()
        at.inputs.in_file = in_file
        at.inputs.response = response
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_TCK2VTK:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix3.utils import TCK2VTK
        at = TCK2VTK()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix3_TensorMetrics:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix3.utils import TensorMetrics
        at = TensorMetrics()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_fa(self) -> None:
        return self.res.outputs.out_fa

    def out_adc(self) -> None:
        return self.res.outputs.out_adc

    def out_ad(self) -> None:
        return self.res.outputs.out_ad

    def out_rd(self) -> None:
        return self.res.outputs.out_rd

    def out_cl(self) -> None:
        return self.res.outputs.out_cl

    def out_cp(self) -> None:
        return self.res.outputs.out_cp

    def out_cs(self) -> None:
        return self.res.outputs.out_cs

    def out_evec(self) -> None:
        return self.res.outputs.out_evec

    def out_eval(self) -> None:
        return self.res.outputs.out_eval

###############################################################################


class mrtrix3_Tractography:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.mrtrix3.tracking import Tractography
        at = Tractography()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_seeds(self) -> None:
        return self.res.outputs.out_seeds

###############################################################################


class mrtrix3_TransformFSLConvert:
    """
    Note:
        dependencies: Nipype,mrtrix3
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", reference="path", in_transform="path", out_transform="path", flirt_import=True, **options):
        from nipype.interfaces.mrtrix3.utils import TransformFSLConvert
        at = TransformFSLConvert()
        at.inputs.in_file = in_file
        at.inputs.reference = reference
        at.inputs.in_transform = in_transform
        at.inputs.out_transform = out_transform
        at.inputs.flirt_import = flirt_import
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_transform(self) -> None:
        return self.res.outputs.out_transform

###############################################################################


