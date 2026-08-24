class fsl_AR1Image:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.maths import AR1Image
        at = AR1Image()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_ApplyMask:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, mask_file="path", in_file="path", **options):
        from nipype.interfaces.fsl.maths import ApplyMask
        at = ApplyMask()
        at.inputs.mask_file = mask_file
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_ApplyTOPUP:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], encoding_file="path", **options):
        from nipype.interfaces.fsl.epi import ApplyTOPUP
        at = ApplyTOPUP()
        at.inputs.in_files = in_files
        at.inputs.encoding_file = encoding_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_corrected(self) -> None:
        return self.res.outputs.out_corrected

###############################################################################


class fsl_ApplyWarp:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", ref_file="path", **options):
        from nipype.interfaces.fsl.preprocess import ApplyWarp
        at = ApplyWarp()
        at.inputs.in_file = in_file
        at.inputs.ref_file = ref_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_ApplyXFM:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", reference="path", **options):
        from nipype.interfaces.fsl.preprocess import ApplyXFM
        at = ApplyXFM()
        at.inputs.in_file = in_file
        at.inputs.reference = reference
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_matrix_file(self) -> None:
        return self.res.outputs.out_matrix_file

    def out_log(self) -> None:
        return self.res.outputs.out_log

###############################################################################


class fsl_AvScale:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.fsl.utils import AvScale
        at = AvScale()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def rotation_translation_matrix(self) -> list[list[float]]:
        return self.res.outputs.rotation_translation_matrix

    def scales(self) -> list[float]:
        return self.res.outputs.scales

    def skews(self) -> list[float]:
        return self.res.outputs.skews

    def average_scaling(self) -> float:
        return self.res.outputs.average_scaling

    def determinant(self) -> float:
        return self.res.outputs.determinant

    def forward_half_transform(self) -> list[list[float]]:
        return self.res.outputs.forward_half_transform

    def backward_half_transform(self) -> list[list[float]]:
        return self.res.outputs.backward_half_transform

    def left_right_orientation_preserved(self) -> bool:
        return self.res.outputs.left_right_orientation_preserved

    def rot_angles(self) -> list[float]:
        return self.res.outputs.rot_angles

    def translations(self) -> list[float]:
        return self.res.outputs.translations

###############################################################################


class fsl_B0Calc:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.possum import B0Calc
        at = B0Calc()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_BEDPOSTX:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dwi="path", mask="path", bvecs="path", bvals="path", n_fibres=0, out_dir="path", **options):
        from nipype.interfaces.fsl.dti import BEDPOSTX
        at = BEDPOSTX()
        at.inputs.dwi = dwi
        at.inputs.mask = mask
        at.inputs.bvecs = bvecs
        at.inputs.bvals = bvals
        at.inputs.n_fibres = n_fibres
        at.inputs.out_dir = out_dir
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mean_dsamples(self) -> None:
        return self.res.outputs.mean_dsamples

    def mean_fsamples(self) -> list[None]:
        return self.res.outputs.mean_fsamples

    def mean_S0samples(self) -> None:
        return self.res.outputs.mean_S0samples

    def mean_phsamples(self) -> list[None]:
        return self.res.outputs.mean_phsamples

    def mean_thsamples(self) -> list[None]:
        return self.res.outputs.mean_thsamples

    def merged_thsamples(self) -> list[None]:
        return self.res.outputs.merged_thsamples

    def merged_phsamples(self) -> list[None]:
        return self.res.outputs.merged_phsamples

    def merged_fsamples(self) -> list[None]:
        return self.res.outputs.merged_fsamples

    def dyads(self) -> list[None]:
        return self.res.outputs.dyads

    def dyads_dispersion(self) -> list[None]:
        return self.res.outputs.dyads_dispersion

###############################################################################


class fsl_BEDPOSTX5:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dwi="path", mask="path", bvecs="path", bvals="path", n_fibres=0, out_dir="path", **options):
        from nipype.interfaces.fsl.dti import BEDPOSTX5
        at = BEDPOSTX5()
        at.inputs.dwi = dwi
        at.inputs.mask = mask
        at.inputs.bvecs = bvecs
        at.inputs.bvals = bvals
        at.inputs.n_fibres = n_fibres
        at.inputs.out_dir = out_dir
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mean_dsamples(self) -> None:
        return self.res.outputs.mean_dsamples

    def mean_fsamples(self) -> list[None]:
        return self.res.outputs.mean_fsamples

    def mean_S0samples(self) -> None:
        return self.res.outputs.mean_S0samples

    def mean_phsamples(self) -> list[None]:
        return self.res.outputs.mean_phsamples

    def mean_thsamples(self) -> list[None]:
        return self.res.outputs.mean_thsamples

    def merged_thsamples(self) -> list[None]:
        return self.res.outputs.merged_thsamples

    def merged_phsamples(self) -> list[None]:
        return self.res.outputs.merged_phsamples

    def merged_fsamples(self) -> list[None]:
        return self.res.outputs.merged_fsamples

    def dyads(self) -> list[None]:
        return self.res.outputs.dyads

    def dyads_dispersion(self) -> list[None]:
        return self.res.outputs.dyads_dispersion

###############################################################################


class fsl_BET:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.preprocess import BET
        at = BET()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def mask_file(self) -> None:
        return self.res.outputs.mask_file

    def outline_file(self) -> None:
        return self.res.outputs.outline_file

    def meshfile(self) -> None:
        return self.res.outputs.meshfile

    def inskull_mask_file(self) -> None:
        return self.res.outputs.inskull_mask_file

    def inskull_mesh_file(self) -> None:
        return self.res.outputs.inskull_mesh_file

    def outskull_mask_file(self) -> None:
        return self.res.outputs.outskull_mask_file

    def outskull_mesh_file(self) -> None:
        return self.res.outputs.outskull_mesh_file

    def outskin_mask_file(self) -> None:
        return self.res.outputs.outskin_mask_file

    def outskin_mesh_file(self) -> None:
        return self.res.outputs.outskin_mesh_file

    def skull_mask_file(self) -> None:
        return self.res.outputs.skull_mask_file

    def skull_file(self) -> None:
        return self.res.outputs.skull_file

###############################################################################


class fsl_BinaryMaths:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, operation="enumerate(('add','sub','mul','div','rem','max','min'))", in_file="path", **options):
        from nipype.interfaces.fsl.maths import BinaryMaths
        at = BinaryMaths()
        at.inputs.operation = operation
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_ChangeDataType:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, output_datatype="enumerate(('float','char','int','short','double','input'))", in_file="path", **options):
        from nipype.interfaces.fsl.maths import ChangeDataType
        at = ChangeDataType()
        at.inputs.output_datatype = output_datatype
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_Cluster:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", threshold=0.0, **options):
        from nipype.interfaces.fsl.model import Cluster
        at = Cluster()
        at.inputs.in_file = in_file
        at.inputs.threshold = threshold
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def index_file(self) -> None:
        return self.res.outputs.index_file

    def threshold_file(self) -> None:
        return self.res.outputs.threshold_file

    def localmax_txt_file(self) -> None:
        return self.res.outputs.localmax_txt_file

    def localmax_vol_file(self) -> None:
        return self.res.outputs.localmax_vol_file

    def size_file(self) -> None:
        return self.res.outputs.size_file

    def max_file(self) -> None:
        return self.res.outputs.max_file

    def mean_file(self) -> None:
        return self.res.outputs.mean_file

    def pval_file(self) -> None:
        return self.res.outputs.pval_file

###############################################################################


class fsl_Complex:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.fsl.utils import Complex
        at = Complex()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def magnitude_out_file(self) -> None:
        return self.res.outputs.magnitude_out_file

    def phase_out_file(self) -> None:
        return self.res.outputs.phase_out_file

    def real_out_file(self) -> None:
        return self.res.outputs.real_out_file

    def imaginary_out_file(self) -> None:
        return self.res.outputs.imaginary_out_file

    def complex_out_file(self) -> None:
        return self.res.outputs.complex_out_file

###############################################################################


class fsl_ContrastMgr:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, tcon_file="path", param_estimates=["path"], corrections="path", dof_file="path", sigmasquareds="path", **options):
        from nipype.interfaces.fsl.model import ContrastMgr
        at = ContrastMgr()
        at.inputs.tcon_file = tcon_file
        at.inputs.param_estimates = param_estimates
        at.inputs.corrections = corrections
        at.inputs.dof_file = dof_file
        at.inputs.sigmasquareds = sigmasquareds
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def copes(self) -> list[None]:
        return self.res.outputs.copes

    def varcopes(self) -> list[None]:
        return self.res.outputs.varcopes

    def zstats(self) -> list[None]:
        return self.res.outputs.zstats

    def tstats(self) -> list[None]:
        return self.res.outputs.tstats

    def fstats(self) -> list[None]:
        return self.res.outputs.fstats

    def zfstats(self) -> list[None]:
        return self.res.outputs.zfstats

    def neffs(self) -> list[None]:
        return self.res.outputs.neffs

###############################################################################


class fsl_ConvertWarp:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, reference="path", **options):
        from nipype.interfaces.fsl.utils import ConvertWarp
        at = ConvertWarp()
        at.inputs.reference = reference
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_ConvertXFM:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import ConvertXFM
        at = ConvertXFM()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_CopyGeom:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", dest_file="path", **options):
        from nipype.interfaces.fsl.utils import CopyGeom
        at = CopyGeom()
        at.inputs.in_file = in_file
        at.inputs.dest_file = dest_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_DTIFit:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dwi="path", mask="path", bvecs="path", bvals="path", **options):
        from nipype.interfaces.fsl.dti import DTIFit
        at = DTIFit()
        at.inputs.dwi = dwi
        at.inputs.mask = mask
        at.inputs.bvecs = bvecs
        at.inputs.bvals = bvals
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def V1(self) -> None:
        return self.res.outputs.V1

    def V2(self) -> None:
        return self.res.outputs.V2

    def V3(self) -> None:
        return self.res.outputs.V3

    def L1(self) -> None:
        return self.res.outputs.L1

    def L2(self) -> None:
        return self.res.outputs.L2

    def L3(self) -> None:
        return self.res.outputs.L3

    def MD(self) -> None:
        return self.res.outputs.MD

    def FA(self) -> None:
        return self.res.outputs.FA

    def MO(self) -> None:
        return self.res.outputs.MO

    def S0(self) -> None:
        return self.res.outputs.S0

    def tensor(self) -> None:
        return self.res.outputs.tensor

    def sse(self) -> None:
        return self.res.outputs.sse

###############################################################################


class fsl_DilateImage:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, operation="enumerate(('mean','modal','max'))", in_file="path", **options):
        from nipype.interfaces.fsl.maths import DilateImage
        at = DilateImage()
        at.inputs.operation = operation
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_DistanceMap:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.dti import DistanceMap
        at = DistanceMap()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def distance_map(self) -> None:
        return self.res.outputs.distance_map

    def local_max_file(self) -> None:
        return self.res.outputs.local_max_file

###############################################################################


class fsl_EPIDeWarp:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, mag_file="path", dph_file="path", **options):
        from nipype.interfaces.fsl.epi import EPIDeWarp
        at = EPIDeWarp()
        at.inputs.mag_file = mag_file
        at.inputs.dph_file = dph_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def unwarped_file(self) -> None:
        return self.res.outputs.unwarped_file

    def vsm_file(self) -> None:
        return self.res.outputs.vsm_file

    def exfdw(self) -> None:
        return self.res.outputs.exfdw

    def exf_mask(self) -> None:
        return self.res.outputs.exf_mask

###############################################################################


class fsl_Eddy:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", in_mask="path", in_index="path", in_acqp="path", in_bvec="path", in_bval="path", **options):
        from nipype.interfaces.fsl.epi import Eddy
        at = Eddy()
        at.inputs.in_file = in_file
        at.inputs.in_mask = in_mask
        at.inputs.in_index = in_index
        at.inputs.in_acqp = in_acqp
        at.inputs.in_bvec = in_bvec
        at.inputs.in_bval = in_bval
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_corrected(self) -> None:
        return self.res.outputs.out_corrected

    def out_parameter(self) -> None:
        return self.res.outputs.out_parameter

    def out_rotated_bvecs(self) -> None:
        return self.res.outputs.out_rotated_bvecs

    def out_movement_rms(self) -> None:
        return self.res.outputs.out_movement_rms

    def out_restricted_movement_rms(self) -> None:
        return self.res.outputs.out_restricted_movement_rms

    def out_shell_alignment_parameters(self) -> None:
        return self.res.outputs.out_shell_alignment_parameters

    def out_shell_pe_translation_parameters(self) -> None:
        return self.res.outputs.out_shell_pe_translation_parameters

    def out_outlier_map(self) -> None:
        return self.res.outputs.out_outlier_map

    def out_outlier_n_stdev_map(self) -> None:
        return self.res.outputs.out_outlier_n_stdev_map

    def out_outlier_n_sqr_stdev_map(self) -> None:
        return self.res.outputs.out_outlier_n_sqr_stdev_map

    def out_outlier_report(self) -> None:
        return self.res.outputs.out_outlier_report

    def out_outlier_free(self) -> None:
        return self.res.outputs.out_outlier_free

    def out_movement_over_time(self) -> None:
        return self.res.outputs.out_movement_over_time

    def out_cnr_maps(self) -> None:
        return self.res.outputs.out_cnr_maps

    def out_residuals(self) -> None:
        return self.res.outputs.out_residuals

###############################################################################


class fsl_EddyCorrect:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", ref_num=0, **options):
        from nipype.interfaces.fsl.epi import EddyCorrect
        at = EddyCorrect()
        at.inputs.in_file = in_file
        at.inputs.ref_num = ref_num
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def eddy_corrected(self) -> None:
        return self.res.outputs.eddy_corrected

###############################################################################


class fsl_EddyQuad:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, idx_file="path", param_file="path", mask_file="path", bval_file="path", **options):
        from nipype.interfaces.fsl.epi import EddyQuad
        at = EddyQuad()
        at.inputs.idx_file = idx_file
        at.inputs.param_file = param_file
        at.inputs.mask_file = mask_file
        at.inputs.bval_file = bval_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def qc_json(self) -> None:
        return self.res.outputs.qc_json

    def qc_pdf(self) -> None:
        return self.res.outputs.qc_pdf

    def avg_b_png(self) -> list[None]:
        return self.res.outputs.avg_b_png

    def avg_b0_pe_png(self) -> list[None]:
        return self.res.outputs.avg_b0_pe_png

    def cnr_png(self) -> list[None]:
        return self.res.outputs.cnr_png

    def vdm_png(self) -> None:
        return self.res.outputs.vdm_png

    def residuals(self) -> None:
        return self.res.outputs.residuals

    def clean_volumes(self) -> None:
        return self.res.outputs.clean_volumes

###############################################################################


class fsl_EpiReg:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, epi="path", t1_head="path", t1_brain="path", **options):
        from nipype.interfaces.fsl.epi import EpiReg
        at = EpiReg()
        at.inputs.epi = epi
        at.inputs.t1_head = t1_head
        at.inputs.t1_brain = t1_brain
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_1vol(self) -> None:
        return self.res.outputs.out_1vol

    def fmap2str_mat(self) -> None:
        return self.res.outputs.fmap2str_mat

    def fmap2epi_mat(self) -> None:
        return self.res.outputs.fmap2epi_mat

    def fmap_epi(self) -> None:
        return self.res.outputs.fmap_epi

    def fmap_str(self) -> None:
        return self.res.outputs.fmap_str

    def fmapmag_str(self) -> None:
        return self.res.outputs.fmapmag_str

    def epi2str_inv(self) -> None:
        return self.res.outputs.epi2str_inv

    def epi2str_mat(self) -> None:
        return self.res.outputs.epi2str_mat

    def shiftmap(self) -> None:
        return self.res.outputs.shiftmap

    def fullwarp(self) -> None:
        return self.res.outputs.fullwarp

    def wmseg(self) -> None:
        return self.res.outputs.wmseg

    def seg(self) -> None:
        return self.res.outputs.seg

    def wmedge(self) -> None:
        return self.res.outputs.wmedge

###############################################################################


class fsl_ErodeImage:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.maths import ErodeImage
        at = ErodeImage()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_ExtractROI:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import ExtractROI
        at = ExtractROI()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def roi_file(self) -> None:
        return self.res.outputs.roi_file

###############################################################################


class fsl_FAST:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.fsl.preprocess import FAST
        at = FAST()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tissue_class_map(self) -> None:
        return self.res.outputs.tissue_class_map

    def tissue_class_files(self) -> list[None]:
        return self.res.outputs.tissue_class_files

    def restored_image(self) -> list[None]:
        return self.res.outputs.restored_image

    def mixeltype(self) -> None:
        return self.res.outputs.mixeltype

    def partial_volume_map(self) -> None:
        return self.res.outputs.partial_volume_map

    def partial_volume_files(self) -> list[None]:
        return self.res.outputs.partial_volume_files

    def bias_field(self) -> list[None]:
        return self.res.outputs.bias_field

    def probability_maps(self) -> list[None]:
        return self.res.outputs.probability_maps

###############################################################################


class fsl_FEAT:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, fsf_file="path", **options):
        from nipype.interfaces.fsl.model import FEAT
        at = FEAT()
        at.inputs.fsf_file = fsf_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def feat_dir(self) -> None:
        return self.res.outputs.feat_dir

###############################################################################


class fsl_FEATModel:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, fsf_file="path", ev_files=["path"], **options):
        from nipype.interfaces.fsl.model import FEATModel
        at = FEATModel()
        at.inputs.fsf_file = fsf_file
        at.inputs.ev_files = ev_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def design_file(self) -> None:
        return self.res.outputs.design_file

    def design_image(self) -> None:
        return self.res.outputs.design_image

    def design_cov(self) -> None:
        return self.res.outputs.design_cov

    def con_file(self) -> None:
        return self.res.outputs.con_file

    def fcon_file(self) -> None:
        return self.res.outputs.fcon_file

###############################################################################


class fsl_FEATRegister:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, feat_dirs=["path"], reg_image="path", **options):
        from nipype.interfaces.fsl.model import FEATRegister
        at = FEATRegister()
        at.inputs.feat_dirs = feat_dirs
        at.inputs.reg_image = reg_image
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def fsf_file(self) -> None:
        return self.res.outputs.fsf_file

###############################################################################


class fsl_FILMGLS:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.model import FILMGLS
        at = FILMGLS()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def param_estimates(self) -> list[None]:
        return self.res.outputs.param_estimates

    def residual4d(self) -> None:
        return self.res.outputs.residual4d

    def dof_file(self) -> None:
        return self.res.outputs.dof_file

    def sigmasquareds(self) -> None:
        return self.res.outputs.sigmasquareds

    def results_dir(self) -> None:
        return self.res.outputs.results_dir

    def thresholdac(self) -> None:
        return self.res.outputs.thresholdac

    def logfile(self) -> None:
        return self.res.outputs.logfile

    def copes(self) -> list[None]:
        return self.res.outputs.copes

    def varcopes(self) -> list[None]:
        return self.res.outputs.varcopes

    def zstats(self) -> list[None]:
        return self.res.outputs.zstats

    def tstats(self) -> list[None]:
        return self.res.outputs.tstats

    def fstats(self) -> list[None]:
        return self.res.outputs.fstats

    def zfstats(self) -> list[None]:
        return self.res.outputs.zfstats

###############################################################################


class fsl_FIRST:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.fsl.preprocess import FIRST
        at = FIRST()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def vtk_surfaces(self) -> list[None]:
        return self.res.outputs.vtk_surfaces

    def bvars(self) -> list[None]:
        return self.res.outputs.bvars

    def original_segmentations(self) -> None:
        return self.res.outputs.original_segmentations

    def segmentation_file(self) -> None:
        return self.res.outputs.segmentation_file

###############################################################################


class fsl_FLAMEO:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, cope_file="path", mask_file="path", design_file="path", t_con_file="path", cov_split_file="path", run_mode="enumerate(('fe','ols','flame1','flame12'))", **options):
        from nipype.interfaces.fsl.model import FLAMEO
        at = FLAMEO()
        at.inputs.cope_file = cope_file
        at.inputs.mask_file = mask_file
        at.inputs.design_file = design_file
        at.inputs.t_con_file = t_con_file
        at.inputs.cov_split_file = cov_split_file
        at.inputs.run_mode = run_mode
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def pes(self) -> list[None]:
        return self.res.outputs.pes

    def res4d(self) -> list[None]:
        return self.res.outputs.res4d

    def copes(self) -> list[None]:
        return self.res.outputs.copes

    def var_copes(self) -> list[None]:
        return self.res.outputs.var_copes

    def zstats(self) -> list[None]:
        return self.res.outputs.zstats

    def tstats(self) -> list[None]:
        return self.res.outputs.tstats

    def zfstats(self) -> list[None]:
        return self.res.outputs.zfstats

    def fstats(self) -> list[None]:
        return self.res.outputs.fstats

    def mrefvars(self) -> list[None]:
        return self.res.outputs.mrefvars

    def tdof(self) -> list[None]:
        return self.res.outputs.tdof

    def weights(self) -> list[None]:
        return self.res.outputs.weights

    def stats_dir(self) -> None:
        return self.res.outputs.stats_dir

###############################################################################


class fsl_FLIRT:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", reference="path", **options):
        from nipype.interfaces.fsl.preprocess import FLIRT
        at = FLIRT()
        at.inputs.in_file = in_file
        at.inputs.reference = reference
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_matrix_file(self) -> None:
        return self.res.outputs.out_matrix_file

    def out_log(self) -> None:
        return self.res.outputs.out_log

###############################################################################


class fsl_FNIRT:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, ref_file="path", in_file="path", **options):
        from nipype.interfaces.fsl.preprocess import FNIRT
        at = FNIRT()
        at.inputs.ref_file = ref_file
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def fieldcoeff_file(self) -> None:
        return self.res.outputs.fieldcoeff_file

    def warped_file(self) -> None:
        return self.res.outputs.warped_file

    def field_file(self) -> None:
        return self.res.outputs.field_file

    def jacobian_file(self) -> None:
        return self.res.outputs.jacobian_file

    def modulatedref_file(self) -> None:
        return self.res.outputs.modulatedref_file

    def out_intensitymap_file(self) -> None:
        return self.res.outputs.out_intensitymap_file

    def log_file(self) -> None:
        return self.res.outputs.log_file

###############################################################################


class fsl_FUGUE:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.fsl.preprocess import FUGUE
        at = FUGUE()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def unwarped_file(self) -> None:
        return self.res.outputs.unwarped_file

    def warped_file(self) -> None:
        return self.res.outputs.warped_file

    def shift_out_file(self) -> None:
        return self.res.outputs.shift_out_file

    def fmap_out_file(self) -> None:
        return self.res.outputs.fmap_out_file

###############################################################################


class fsl_FilterRegressor:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", design_file="path", **options):
        from nipype.interfaces.fsl.utils import FilterRegressor
        at = FilterRegressor()
        at.inputs.in_file = in_file
        at.inputs.design_file = design_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_FindTheBiggest:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.fsl.dti import FindTheBiggest
        at = FindTheBiggest()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_GLM:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", design="path", **options):
        from nipype.interfaces.fsl.model import GLM
        at = GLM()
        at.inputs.in_file = in_file
        at.inputs.design = design
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_cope(self) -> list[None]:
        return self.res.outputs.out_cope

    def out_z(self) -> list[None]:
        return self.res.outputs.out_z

    def out_t(self) -> list[None]:
        return self.res.outputs.out_t

    def out_p(self) -> list[None]:
        return self.res.outputs.out_p

    def out_f(self) -> list[None]:
        return self.res.outputs.out_f

    def out_pf(self) -> list[None]:
        return self.res.outputs.out_pf

    def out_res(self) -> list[None]:
        return self.res.outputs.out_res

    def out_varcb(self) -> list[None]:
        return self.res.outputs.out_varcb

    def out_sigsq(self) -> list[None]:
        return self.res.outputs.out_sigsq

    def out_data(self) -> list[None]:
        return self.res.outputs.out_data

    def out_vnscales(self) -> list[None]:
        return self.res.outputs.out_vnscales

###############################################################################


class fsl_ICA_AROMA:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, out_dir="path", denoise_type="enumerate(('nonaggr','aggr','both','no'))", **options):
        from nipype.interfaces.fsl.aroma import ICA_AROMA
        at = ICA_AROMA()
        at.inputs.out_dir = out_dir
        at.inputs.denoise_type = denoise_type
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def aggr_denoised_file(self) -> None:
        return self.res.outputs.aggr_denoised_file

    def nonaggr_denoised_file(self) -> None:
        return self.res.outputs.nonaggr_denoised_file

    def out_dir(self) -> None:
        return self.res.outputs.out_dir

###############################################################################


class fsl_ImageMaths:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import ImageMaths
        at = ImageMaths()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_ImageMeants:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import ImageMeants
        at = ImageMeants()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_ImageStats:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", op_string='', **options):
        from nipype.interfaces.fsl.utils import ImageStats
        at = ImageStats()
        at.inputs.in_file = in_file
        at.inputs.op_string = op_string
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_stat(self) -> str:
        return self.res.outputs.out_stat

###############################################################################


class fsl_InvWarp:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, warp="path", reference="path", **options):
        from nipype.interfaces.fsl.utils import InvWarp
        at = InvWarp()
        at.inputs.warp = warp
        at.inputs.reference = reference
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def inverse_warp(self) -> None:
        return self.res.outputs.inverse_warp

###############################################################################


class fsl_IsotropicSmooth:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.maths import IsotropicSmooth
        at = IsotropicSmooth()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_L2Model:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.fsl.model import L2Model
        at = L2Model()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def design_mat(self) -> None:
        return self.res.outputs.design_mat

    def design_con(self) -> None:
        return self.res.outputs.design_con

    def design_grp(self) -> None:
        return self.res.outputs.design_grp

###############################################################################


class fsl_Level1Design:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, interscan_interval=0.0, session_info='', bases="enumerate(('dgamma','derivs','gamma','gammasigma','gammadelay','custom','bfcustompath','none'))", model_serial_correlations=True, **options):
        from nipype.interfaces.fsl.model import Level1Design
        at = Level1Design()
        at.inputs.interscan_interval = interscan_interval
        at.inputs.session_info = session_info
        at.inputs.bases = bases
        at.inputs.model_serial_correlations = model_serial_correlations
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def fsf_files(self) -> list[None]:
        return self.res.outputs.fsf_files

    def ev_files(self) -> list[list[None]]:
        return self.res.outputs.ev_files

###############################################################################


class fsl_MCFLIRT:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.preprocess import MCFLIRT
        at = MCFLIRT()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def variance_img(self) -> None:
        return self.res.outputs.variance_img

    def std_img(self) -> None:
        return self.res.outputs.std_img

    def mean_img(self) -> None:
        return self.res.outputs.mean_img

    def par_file(self) -> None:
        return self.res.outputs.par_file

    def mat_file(self) -> list[None]:
        return self.res.outputs.mat_file

    def rms_files(self) -> list[None]:
        return self.res.outputs.rms_files

###############################################################################


class fsl_MELODIC:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.fsl.model import MELODIC
        at = MELODIC()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_dir(self) -> None:
        return self.res.outputs.out_dir

    def report_dir(self) -> None:
        return self.res.outputs.report_dir

###############################################################################


class fsl_MakeDyadicVectors:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, theta_vol="path", phi_vol="path", **options):
        from nipype.interfaces.fsl.dti import MakeDyadicVectors
        at = MakeDyadicVectors()
        at.inputs.theta_vol = theta_vol
        at.inputs.phi_vol = phi_vol
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def dyads(self) -> None:
        return self.res.outputs.dyads

    def dispersion(self) -> None:
        return self.res.outputs.dispersion

###############################################################################


class fsl_MaxnImage:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.maths import MaxnImage
        at = MaxnImage()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_MeanImage:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.maths import MeanImage
        at = MeanImage()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_MedianImage:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.maths import MedianImage
        at = MedianImage()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_Merge:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], dimension="enumerate(('t','x','y','z','a'))", **options):
        from nipype.interfaces.fsl.utils import Merge
        at = Merge()
        at.inputs.in_files = in_files
        at.inputs.dimension = dimension
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def merged_file(self) -> None:
        return self.res.outputs.merged_file

###############################################################################


class fsl_MinImage:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.maths import MinImage
        at = MinImage()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_MotionOutliers:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import MotionOutliers
        at = MotionOutliers()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_metric_values(self) -> None:
        return self.res.outputs.out_metric_values

    def out_metric_plot(self) -> None:
        return self.res.outputs.out_metric_plot

###############################################################################


class fsl_MultiImageMaths:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, op_string='', operand_files=["path"], in_file="path", **options):
        from nipype.interfaces.fsl.maths import MultiImageMaths
        at = MultiImageMaths()
        at.inputs.op_string = op_string
        at.inputs.operand_files = operand_files
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_MultipleRegressDesign:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, contrasts=[(0,)], regressors=[{}], **options):
        from nipype.interfaces.fsl.model import MultipleRegressDesign
        at = MultipleRegressDesign()
        at.inputs.contrasts = contrasts
        at.inputs.regressors = regressors
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def design_mat(self) -> None:
        return self.res.outputs.design_mat

    def design_con(self) -> None:
        return self.res.outputs.design_con

    def design_fts(self) -> None:
        return self.res.outputs.design_fts

    def design_grp(self) -> None:
        return self.res.outputs.design_grp

###############################################################################


class fsl_Overlay:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, background_image="path", stat_image="path", stat_thresh=(0,), **options):
        from nipype.interfaces.fsl.utils import Overlay
        at = Overlay()
        at.inputs.background_image = background_image
        at.inputs.stat_image = stat_image
        at.inputs.stat_thresh = stat_thresh
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_PRELUDE:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.fsl.preprocess import PRELUDE
        at = PRELUDE()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def unwrapped_phase_file(self) -> None:
        return self.res.outputs.unwrapped_phase_file

###############################################################################


class fsl_PercentileImage:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.maths import PercentileImage
        at = PercentileImage()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_PlotMotionParams:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file=["path"], in_source="enumerate(('spm','fsl'))", plot_type="enumerate(('rotations','translations','displacement'))", **options):
        from nipype.interfaces.fsl.utils import PlotMotionParams
        at = PlotMotionParams()
        at.inputs.in_file = in_file
        at.inputs.in_source = in_source
        at.inputs.plot_type = plot_type
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_PlotTimeSeries:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file=["path"], **options):
        from nipype.interfaces.fsl.utils import PlotTimeSeries
        at = PlotTimeSeries()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_PowerSpectrum:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import PowerSpectrum
        at = PowerSpectrum()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_PrepareFieldmap:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_phase="path", in_magnitude="path", delta_TE=0.0, **options):
        from nipype.interfaces.fsl.epi import PrepareFieldmap
        at = PrepareFieldmap()
        at.inputs.in_phase = in_phase
        at.inputs.in_magnitude = in_magnitude
        at.inputs.delta_TE = delta_TE
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_fieldmap(self) -> None:
        return self.res.outputs.out_fieldmap

###############################################################################


class fsl_ProbTrackX:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, thsamples=["path"], phsamples=["path"], fsamples=["path"], mask="path", seed=["path"], **options):
        from nipype.interfaces.fsl.dti import ProbTrackX
        at = ProbTrackX()
        at.inputs.thsamples = thsamples
        at.inputs.phsamples = phsamples
        at.inputs.fsamples = fsamples
        at.inputs.mask = mask
        at.inputs.seed = seed
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def log(self) -> None:
        return self.res.outputs.log

    def fdt_paths(self) -> list[None]:
        return self.res.outputs.fdt_paths

    def way_total(self) -> None:
        return self.res.outputs.way_total

    def targets(self) -> list[None]:
        return self.res.outputs.targets

    def particle_files(self) -> list[None]:
        return self.res.outputs.particle_files

###############################################################################


class fsl_ProbTrackX2:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, thsamples=["path"], phsamples=["path"], fsamples=["path"], mask="path", seed=["path"], **options):
        from nipype.interfaces.fsl.dti import ProbTrackX2
        at = ProbTrackX2()
        at.inputs.thsamples = thsamples
        at.inputs.phsamples = phsamples
        at.inputs.fsamples = fsamples
        at.inputs.mask = mask
        at.inputs.seed = seed
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def network_matrix(self) -> None:
        return self.res.outputs.network_matrix

    def matrix1_dot(self) -> None:
        return self.res.outputs.matrix1_dot

    def lookup_tractspace(self) -> None:
        return self.res.outputs.lookup_tractspace

    def matrix2_dot(self) -> None:
        return self.res.outputs.matrix2_dot

    def matrix3_dot(self) -> None:
        return self.res.outputs.matrix3_dot

    def log(self) -> None:
        return self.res.outputs.log

    def fdt_paths(self) -> list[None]:
        return self.res.outputs.fdt_paths

    def way_total(self) -> None:
        return self.res.outputs.way_total

    def targets(self) -> list[None]:
        return self.res.outputs.targets

    def particle_files(self) -> list[None]:
        return self.res.outputs.particle_files

###############################################################################


class fsl_ProjThresh:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], threshold=0, **options):
        from nipype.interfaces.fsl.dti import ProjThresh
        at = ProjThresh()
        at.inputs.in_files = in_files
        at.inputs.threshold = threshold
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_files(self) -> list[None]:
        return self.res.outputs.out_files

###############################################################################


class fsl_Randomise:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.model import Randomise
        at = Randomise()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tstat_files(self) -> list[None]:
        return self.res.outputs.tstat_files

    def fstat_files(self) -> list[None]:
        return self.res.outputs.fstat_files

    def t_p_files(self) -> list[None]:
        return self.res.outputs.t_p_files

    def f_p_files(self) -> list[None]:
        return self.res.outputs.f_p_files

    def t_corrected_p_files(self) -> list[None]:
        return self.res.outputs.t_corrected_p_files

    def f_corrected_p_files(self) -> list[None]:
        return self.res.outputs.f_corrected_p_files

###############################################################################


class fsl_Reorient2Std:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import Reorient2Std
        at = Reorient2Std()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_RobustFOV:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import RobustFOV
        at = RobustFOV()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_roi(self) -> None:
        return self.res.outputs.out_roi

    def out_transform(self) -> None:
        return self.res.outputs.out_transform

###############################################################################


class fsl_SMM:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, spatial_data_file="path", mask="path", **options):
        from nipype.interfaces.fsl.model import SMM
        at = SMM()
        at.inputs.spatial_data_file = spatial_data_file
        at.inputs.mask = mask
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def null_p_map(self) -> None:
        return self.res.outputs.null_p_map

    def activation_p_map(self) -> None:
        return self.res.outputs.activation_p_map

    def deactivation_p_map(self) -> None:
        return self.res.outputs.deactivation_p_map

###############################################################################


class fsl_SUSAN:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", brightness_threshold=0.0, fwhm=0.0, **options):
        from nipype.interfaces.fsl.preprocess import SUSAN
        at = SUSAN()
        at.inputs.in_file = in_file
        at.inputs.brightness_threshold = brightness_threshold
        at.inputs.fwhm = fwhm
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def smoothed_file(self) -> None:
        return self.res.outputs.smoothed_file

###############################################################################


class fsl_SigLoss:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.epi import SigLoss
        at = SigLoss()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_Slice:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import Slice
        at = Slice()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_files(self) -> list[None]:
        return self.res.outputs.out_files

###############################################################################


class fsl_SliceTimer:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.preprocess import SliceTimer
        at = SliceTimer()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def slice_time_corrected_file(self) -> None:
        return self.res.outputs.slice_time_corrected_file

###############################################################################


class fsl_Slicer:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import Slicer
        at = Slicer()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_Smooth:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import Smooth
        at = Smooth()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def smoothed_file(self) -> None:
        return self.res.outputs.smoothed_file

###############################################################################


class fsl_SmoothEstimate:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, mask_file="path", **options):
        from nipype.interfaces.fsl.model import SmoothEstimate
        at = SmoothEstimate()
        at.inputs.mask_file = mask_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def dlh(self) -> float:
        return self.res.outputs.dlh

    def volume(self) -> int:
        return self.res.outputs.volume

    def resels(self) -> float:
        return self.res.outputs.resels

###############################################################################


class fsl_SpatialFilter:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, operation="enumerate(('mean','median','meanu'))", in_file="path", **options):
        from nipype.interfaces.fsl.maths import SpatialFilter
        at = SpatialFilter()
        at.inputs.operation = operation
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_Split:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", dimension="enumerate(('t','x','y','z'))", **options):
        from nipype.interfaces.fsl.utils import Split
        at = Split()
        at.inputs.in_file = in_file
        at.inputs.dimension = dimension
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_files(self) -> list[None]:
        return self.res.outputs.out_files

###############################################################################


class fsl_SwapDimensions:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", new_dims="enumerate(('x','-x','y','-y','z','-z','RL','LR','AP','PA','IS','SI'))", **options):
        from nipype.interfaces.fsl.utils import SwapDimensions
        at = SwapDimensions()
        at.inputs.in_file = in_file
        at.inputs.new_dims = new_dims
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_TOPUP:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.epi import TOPUP
        at = TOPUP()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_fieldcoef(self) -> None:
        return self.res.outputs.out_fieldcoef

    def out_movpar(self) -> None:
        return self.res.outputs.out_movpar

    def out_enc_file(self) -> None:
        return self.res.outputs.out_enc_file

    def out_field(self) -> None:
        return self.res.outputs.out_field

    def out_warps(self) -> list[None]:
        return self.res.outputs.out_warps

    def out_jacs(self) -> list[None]:
        return self.res.outputs.out_jacs

    def out_mats(self) -> list[None]:
        return self.res.outputs.out_mats

    def out_corrected(self) -> None:
        return self.res.outputs.out_corrected

    def out_logfile(self) -> None:
        return self.res.outputs.out_logfile

###############################################################################


class fsl_TemporalFilter:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.maths import TemporalFilter
        at = TemporalFilter()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_Text2Vest:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.fsl.utils import Text2Vest
        at = Text2Vest()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_Threshold:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, thresh=0.0, in_file="path", **options):
        from nipype.interfaces.fsl.maths import Threshold
        at = Threshold()
        at.inputs.thresh = thresh
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_TractSkeleton:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.dti import TractSkeleton
        at = TractSkeleton()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def projected_data(self) -> None:
        return self.res.outputs.projected_data

    def skeleton_file(self) -> None:
        return self.res.outputs.skeleton_file

###############################################################################


class fsl_TrainingSetCreator:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.fsl.fix import TrainingSetCreator
        at = TrainingSetCreator()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mel_icas_out(self) -> list[None]:
        return self.res.outputs.mel_icas_out

###############################################################################


class fsl_UnaryMaths:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, operation="enumerate(('exp','log','sin','cos','tan','asin','acos','atan','sqr','sqrt','recip','abs','bin','binv','fillh','fillh26','index','edge','nan','nanm','rand','randn','range'))", in_file="path", **options):
        from nipype.interfaces.fsl.maths import UnaryMaths
        at = UnaryMaths()
        at.inputs.operation = operation
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_VecReg:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", ref_vol="path", **options):
        from nipype.interfaces.fsl.dti import VecReg
        at = VecReg()
        at.inputs.in_file = in_file
        at.inputs.ref_vol = ref_vol
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_Vest2Text:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.fsl.utils import Vest2Text
        at = Vest2Text()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_WarpPoints:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, src_file="path", dest_file="path", in_coords="path", **options):
        from nipype.interfaces.fsl.utils import WarpPoints
        at = WarpPoints()
        at.inputs.src_file = src_file
        at.inputs.dest_file = dest_file
        at.inputs.in_coords = in_coords
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_WarpPointsFromStd:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, img_file="path", std_file="path", in_coords="path", **options):
        from nipype.interfaces.fsl.utils import WarpPointsFromStd
        at = WarpPointsFromStd()
        at.inputs.img_file = img_file
        at.inputs.std_file = std_file
        at.inputs.in_coords = in_coords
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_WarpPointsToStd:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, img_file="path", std_file="path", in_coords="path", **options):
        from nipype.interfaces.fsl.utils import WarpPointsToStd
        at = WarpPointsToStd()
        at.inputs.img_file = img_file
        at.inputs.std_file = std_file
        at.inputs.in_coords = in_coords
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class fsl_WarpUtils:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", reference="path", write_jacobian=True, **options):
        from nipype.interfaces.fsl.utils import WarpUtils
        at = WarpUtils()
        at.inputs.in_file = in_file
        at.inputs.reference = reference
        at.inputs.write_jacobian = write_jacobian
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_jacobian(self) -> None:
        return self.res.outputs.out_jacobian

###############################################################################


class fsl_XFibres:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dwi="path", mask="path", bvecs="path", bvals="path", n_fibres=0, **options):
        from nipype.interfaces.fsl.dti import XFibres
        at = XFibres()
        at.inputs.dwi = dwi
        at.inputs.mask = mask
        at.inputs.bvecs = bvecs
        at.inputs.bvals = bvals
        at.inputs.n_fibres = n_fibres
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def dyads(self) -> list[None]:
        return self.res.outputs.dyads

    def fsamples(self) -> list[None]:
        return self.res.outputs.fsamples

    def mean_dsamples(self) -> None:
        return self.res.outputs.mean_dsamples

    def mean_fsamples(self) -> list[None]:
        return self.res.outputs.mean_fsamples

    def mean_S0samples(self) -> None:
        return self.res.outputs.mean_S0samples

    def mean_tausamples(self) -> None:
        return self.res.outputs.mean_tausamples

    def phsamples(self) -> list[None]:
        return self.res.outputs.phsamples

    def thsamples(self) -> list[None]:
        return self.res.outputs.thsamples

###############################################################################


class fsl_XFibres5:
    """
    Note:
        dependencies: Nipype,fsl
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dwi="path", mask="path", bvecs="path", bvals="path", n_fibres=0, **options):
        from nipype.interfaces.fsl.dti import XFibres5
        at = XFibres5()
        at.inputs.dwi = dwi
        at.inputs.mask = mask
        at.inputs.bvecs = bvecs
        at.inputs.bvals = bvals
        at.inputs.n_fibres = n_fibres
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def dyads(self) -> list[None]:
        return self.res.outputs.dyads

    def fsamples(self) -> list[None]:
        return self.res.outputs.fsamples

    def mean_dsamples(self) -> None:
        return self.res.outputs.mean_dsamples

    def mean_fsamples(self) -> list[None]:
        return self.res.outputs.mean_fsamples

    def mean_S0samples(self) -> None:
        return self.res.outputs.mean_S0samples

    def mean_tausamples(self) -> None:
        return self.res.outputs.mean_tausamples

    def phsamples(self) -> list[None]:
        return self.res.outputs.phsamples

    def thsamples(self) -> list[None]:
        return self.res.outputs.thsamples

###############################################################################


