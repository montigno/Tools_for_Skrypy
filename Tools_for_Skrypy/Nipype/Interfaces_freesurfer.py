class freesurfer_AddXFormToHeader:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", transform="path", **options):
        from nipype.interfaces.freesurfer.utils import AddXFormToHeader
        at = AddXFormToHeader()
        at.inputs.in_file = in_file
        at.inputs.transform = transform
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_Aparc2Aseg:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subject_id='', out_file="path", lh_white="path", rh_white="path", lh_pial="path", rh_pial="path", lh_ribbon="path", rh_ribbon="path", ribbon="path", lh_annotation="path", rh_annotation="path", **options):
        from nipype.interfaces.freesurfer.utils import Aparc2Aseg
        at = Aparc2Aseg()
        at.inputs.subject_id = subject_id
        at.inputs.out_file = out_file
        at.inputs.lh_white = lh_white
        at.inputs.rh_white = rh_white
        at.inputs.lh_pial = lh_pial
        at.inputs.rh_pial = rh_pial
        at.inputs.lh_ribbon = lh_ribbon
        at.inputs.rh_ribbon = rh_ribbon
        at.inputs.ribbon = ribbon
        at.inputs.lh_annotation = lh_annotation
        at.inputs.rh_annotation = rh_annotation
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_Apas2Aseg:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.freesurfer.utils import Apas2Aseg
        at = Apas2Aseg()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_ApplyMask:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", mask_file="path", **options):
        from nipype.interfaces.freesurfer.utils import ApplyMask
        at = ApplyMask()
        at.inputs.in_file = in_file
        at.inputs.mask_file = mask_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_ApplyVolTransform:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source_file="path", **options):
        from nipype.interfaces.freesurfer.preprocess import ApplyVolTransform
        at = ApplyVolTransform()
        at.inputs.source_file = source_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def transformed_file(self) -> None:
        return self.res.outputs.transformed_file

###############################################################################


class freesurfer_BBRegister:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subject_id='', source_file="path", contrast_type="enumerate(('t1','t2','bold','dti'))", **options):
        from nipype.interfaces.freesurfer.preprocess import BBRegister
        at = BBRegister()
        at.inputs.subject_id = subject_id
        at.inputs.source_file = source_file
        at.inputs.contrast_type = contrast_type
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_reg_file(self) -> None:
        return self.res.outputs.out_reg_file

    def out_fsl_file(self) -> None:
        return self.res.outputs.out_fsl_file

    def out_lta_file(self) -> None:
        return self.res.outputs.out_lta_file

    def min_cost_file(self) -> None:
        return self.res.outputs.min_cost_file

    def init_cost_file(self) -> None:
        return self.res.outputs.init_cost_file

    def registered_file(self) -> None:
        return self.res.outputs.registered_file

###############################################################################


class freesurfer_Binarize:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.model import Binarize
        at = Binarize()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def binary_file(self) -> None:
        return self.res.outputs.binary_file

    def count_file(self) -> None:
        return self.res.outputs.count_file

###############################################################################


class freesurfer_CALabel:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", transform="path", template="path", **options):
        from nipype.interfaces.freesurfer.preprocess import CALabel
        at = CALabel()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        at.inputs.transform = transform
        at.inputs.template = template
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_CANormalize:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", atlas="path", transform="path", **options):
        from nipype.interfaces.freesurfer.preprocess import CANormalize
        at = CANormalize()
        at.inputs.in_file = in_file
        at.inputs.atlas = atlas
        at.inputs.transform = transform
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def control_points(self) -> None:
        return self.res.outputs.control_points

###############################################################################


class freesurfer_CARegister:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.preprocess import CARegister
        at = CARegister()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_CheckTalairachAlignment:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.freesurfer.utils import CheckTalairachAlignment
        at = CheckTalairachAlignment()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_Concatenate:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.freesurfer.model import Concatenate
        at = Concatenate()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def concatenated_file(self) -> None:
        return self.res.outputs.concatenated_file

###############################################################################


class freesurfer_ConcatenateLTA:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_lta1="path", in_lta2="path", **options):
        from nipype.interfaces.freesurfer.preprocess import ConcatenateLTA
        at = ConcatenateLTA()
        at.inputs.in_lta1 = in_lta1
        at.inputs.in_lta2 = in_lta2
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_Contrast:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subject_id='', hemisphere="enumerate(('lh','rh'))", thickness="path", white="path", annotation="path", cortex="path", orig="path", rawavg="path", **options):
        from nipype.interfaces.freesurfer.utils import Contrast
        at = Contrast()
        at.inputs.subject_id = subject_id
        at.inputs.hemisphere = hemisphere
        at.inputs.thickness = thickness
        at.inputs.white = white
        at.inputs.annotation = annotation
        at.inputs.cortex = cortex
        at.inputs.orig = orig
        at.inputs.rawavg = rawavg
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_contrast(self) -> None:
        return self.res.outputs.out_contrast

    def out_stats(self) -> None:
        return self.res.outputs.out_stats

    def out_log(self) -> None:
        return self.res.outputs.out_log

###############################################################################


class freesurfer_Curvature:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.utils import Curvature
        at = Curvature()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_mean(self) -> None:
        return self.res.outputs.out_mean

    def out_gauss(self) -> None:
        return self.res.outputs.out_gauss

###############################################################################


class freesurfer_CurvatureStats:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, curvfile1="path", curvfile2="path", hemisphere="enumerate(('lh','rh'))", subject_id='', **options):
        from nipype.interfaces.freesurfer.utils import CurvatureStats
        at = CurvatureStats()
        at.inputs.curvfile1 = curvfile1
        at.inputs.curvfile2 = curvfile2
        at.inputs.hemisphere = hemisphere
        at.inputs.subject_id = subject_id
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_DICOMConvert:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dicom_dir="path", base_output_dir="path", **options):
        from nipype.interfaces.freesurfer.preprocess import DICOMConvert
        at = DICOMConvert()
        at.inputs.dicom_dir = dicom_dir
        at.inputs.base_output_dir = base_output_dir
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class freesurfer_EMRegister:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", template="path", **options):
        from nipype.interfaces.freesurfer.registration import EMRegister
        at = EMRegister()
        at.inputs.in_file = in_file
        at.inputs.template = template
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_EditWMwithAseg:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", brain_file="path", seg_file="path", out_file="path", **options):
        from nipype.interfaces.freesurfer.preprocess import EditWMwithAseg
        at = EditWMwithAseg()
        at.inputs.in_file = in_file
        at.inputs.brain_file = brain_file
        at.inputs.seg_file = seg_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_EulerNumber:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.utils import EulerNumber
        at = EulerNumber()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def euler(self) -> int:
        return self.res.outputs.euler

    def defects(self) -> int:
        return self.res.outputs.defects

###############################################################################


class freesurfer_ExtractMainComponent:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.utils import ExtractMainComponent
        at = ExtractMainComponent()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_FitMSParams:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.freesurfer.preprocess import FitMSParams
        at = FitMSParams()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def t1_image(self) -> None:
        return self.res.outputs.t1_image

    def pd_image(self) -> None:
        return self.res.outputs.pd_image

    def t2star_image(self) -> None:
        return self.res.outputs.t2star_image

###############################################################################


class freesurfer_FixTopology:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_orig="path", in_inflated="path", in_brain="path", in_wm="path", hemisphere='', subject_id='', copy_inputs=True, **options):
        from nipype.interfaces.freesurfer.utils import FixTopology
        at = FixTopology()
        at.inputs.in_orig = in_orig
        at.inputs.in_inflated = in_inflated
        at.inputs.in_brain = in_brain
        at.inputs.in_wm = in_wm
        at.inputs.hemisphere = hemisphere
        at.inputs.subject_id = subject_id
        at.inputs.copy_inputs = copy_inputs
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_FuseSegmentations:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, timepoints=[''], out_file="path", in_segmentations=["path"], in_segmentations_noCC=["path"], in_norms=["path"], **options):
        from nipype.interfaces.freesurfer.longitudinal import FuseSegmentations
        at = FuseSegmentations()
        at.inputs.timepoints = timepoints
        at.inputs.out_file = out_file
        at.inputs.in_segmentations = in_segmentations
        at.inputs.in_segmentations_noCC = in_segmentations_noCC
        at.inputs.in_norms = in_norms
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_GLMFit:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.model import GLMFit
        at = GLMFit()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def glm_dir(self) -> None:
        return self.res.outputs.glm_dir

    def beta_file(self) -> None:
        return self.res.outputs.beta_file

    def error_file(self) -> None:
        return self.res.outputs.error_file

    def error_var_file(self) -> None:
        return self.res.outputs.error_var_file

    def error_stddev_file(self) -> None:
        return self.res.outputs.error_stddev_file

    def estimate_file(self) -> None:
        return self.res.outputs.estimate_file

    def mask_file(self) -> None:
        return self.res.outputs.mask_file

    def fwhm_file(self) -> None:
        return self.res.outputs.fwhm_file

    def dof_file(self) -> None:
        return self.res.outputs.dof_file

    def gamma_file(self) -> list[str]:
        return self.res.outputs.gamma_file

    def gamma_var_file(self) -> list[str]:
        return self.res.outputs.gamma_var_file

    def sig_file(self) -> list[str]:
        return self.res.outputs.sig_file

    def ftest_file(self) -> list[str]:
        return self.res.outputs.ftest_file

    def spatial_eigenvectors(self) -> None:
        return self.res.outputs.spatial_eigenvectors

    def frame_eigenvectors(self) -> None:
        return self.res.outputs.frame_eigenvectors

    def singular_values(self) -> None:
        return self.res.outputs.singular_values

    def svd_stats_file(self) -> None:
        return self.res.outputs.svd_stats_file

    def k2p_file(self) -> None:
        return self.res.outputs.k2p_file

    def bp_file(self) -> None:
        return self.res.outputs.bp_file

###############################################################################


class freesurfer_GTMPVC:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", segmentation="path", **options):
        from nipype.interfaces.freesurfer.petsurfer import GTMPVC
        at = GTMPVC()
        at.inputs.in_file = in_file
        at.inputs.segmentation = segmentation
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def pvc_dir(self) -> None:
        return self.res.outputs.pvc_dir

    def ref_file(self) -> None:
        return self.res.outputs.ref_file

    def hb_nifti(self) -> None:
        return self.res.outputs.hb_nifti

    def hb_dat(self) -> None:
        return self.res.outputs.hb_dat

    def nopvc_file(self) -> None:
        return self.res.outputs.nopvc_file

    def gtm_file(self) -> None:
        return self.res.outputs.gtm_file

    def gtm_stats(self) -> None:
        return self.res.outputs.gtm_stats

    def input_file(self) -> None:
        return self.res.outputs.input_file

    def reg_pet2anat(self) -> None:
        return self.res.outputs.reg_pet2anat

    def reg_anat2pet(self) -> None:
        return self.res.outputs.reg_anat2pet

    def reg_rbvpet2anat(self) -> None:
        return self.res.outputs.reg_rbvpet2anat

    def reg_anat2rbvpet(self) -> None:
        return self.res.outputs.reg_anat2rbvpet

    def mgx_ctxgm(self) -> None:
        return self.res.outputs.mgx_ctxgm

    def mgx_subctxgm(self) -> None:
        return self.res.outputs.mgx_subctxgm

    def mgx_gm(self) -> None:
        return self.res.outputs.mgx_gm

    def rbv(self) -> None:
        return self.res.outputs.rbv

    def opt_params(self) -> None:
        return self.res.outputs.opt_params

    def yhat0(self) -> None:
        return self.res.outputs.yhat0

    def yhat(self) -> None:
        return self.res.outputs.yhat

    def yhat_full_fov(self) -> None:
        return self.res.outputs.yhat_full_fov

    def yhat_with_noise(self) -> None:
        return self.res.outputs.yhat_with_noise

    def eres(self) -> None:
        return self.res.outputs.eres

    def tissue_fraction(self) -> None:
        return self.res.outputs.tissue_fraction

    def tissue_fraction_psf(self) -> None:
        return self.res.outputs.tissue_fraction_psf

    def seg(self) -> None:
        return self.res.outputs.seg

    def seg_ctab(self) -> None:
        return self.res.outputs.seg_ctab

###############################################################################


class freesurfer_GTMSeg:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subject_id='', **options):
        from nipype.interfaces.freesurfer.petsurfer import GTMSeg
        at = GTMSeg()
        at.inputs.subject_id = subject_id
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_Jacobian:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_origsurf="path", in_mappedsurf="path", **options):
        from nipype.interfaces.freesurfer.utils import Jacobian
        at = Jacobian()
        at.inputs.in_origsurf = in_origsurf
        at.inputs.in_mappedsurf = in_mappedsurf
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_Label2Annot:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, hemisphere="enumerate(('lh','rh'))", subject_id='', in_labels=[''], out_annot='', orig="path", **options):
        from nipype.interfaces.freesurfer.model import Label2Annot
        at = Label2Annot()
        at.inputs.hemisphere = hemisphere
        at.inputs.subject_id = subject_id
        at.inputs.in_labels = in_labels
        at.inputs.out_annot = out_annot
        at.inputs.orig = orig
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_Label2Label:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, hemisphere="enumerate(('lh','rh'))", subject_id='', sphere_reg="path", white="path", source_sphere_reg="path", source_white="path", source_label="path", source_subject='', **options):
        from nipype.interfaces.freesurfer.model import Label2Label
        at = Label2Label()
        at.inputs.hemisphere = hemisphere
        at.inputs.subject_id = subject_id
        at.inputs.sphere_reg = sphere_reg
        at.inputs.white = white
        at.inputs.source_sphere_reg = source_sphere_reg
        at.inputs.source_white = source_white
        at.inputs.source_label = source_label
        at.inputs.source_subject = source_subject
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_Label2Vol:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, template_file="path", **options):
        from nipype.interfaces.freesurfer.model import Label2Vol
        at = Label2Vol()
        at.inputs.template_file = template_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def vol_label_file(self) -> None:
        return self.res.outputs.vol_label_file

###############################################################################


class freesurfer_MNIBiasCorrection:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.preprocess import MNIBiasCorrection
        at = MNIBiasCorrection()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_MPRtoMNI305:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, reference_dir="path", target='', **options):
        from nipype.interfaces.freesurfer.registration import MPRtoMNI305
        at = MPRtoMNI305()
        at.inputs.reference_dir = reference_dir
        at.inputs.target = target
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def log_file(self) -> None:
        return self.res.outputs.log_file

###############################################################################


class freesurfer_MRIConvert:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.preprocess import MRIConvert
        at = MRIConvert()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> list[None]:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_MRICoreg:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source_file="path", **options):
        from nipype.interfaces.freesurfer.registration import MRICoreg
        at = MRICoreg()
        at.inputs.source_file = source_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_reg_file(self) -> None:
        return self.res.outputs.out_reg_file

    def out_lta_file(self) -> None:
        return self.res.outputs.out_lta_file

    def out_params_file(self) -> None:
        return self.res.outputs.out_params_file

###############################################################################


class freesurfer_MRIFill:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.freesurfer.utils import MRIFill
        at = MRIFill()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def log_file(self) -> None:
        return self.res.outputs.log_file

###############################################################################


class freesurfer_MRIMarchingCubes:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", label_value=0, **options):
        from nipype.interfaces.freesurfer.utils import MRIMarchingCubes
        at = MRIMarchingCubes()
        at.inputs.in_file = in_file
        at.inputs.label_value = label_value
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def surface(self) -> None:
        return self.res.outputs.surface

###############################################################################


class freesurfer_MRIPretess:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_filled="path", label=0, in_norm="path", **options):
        from nipype.interfaces.freesurfer.utils import MRIPretess
        at = MRIPretess()
        at.inputs.in_filled = in_filled
        at.inputs.label = label
        at.inputs.in_norm = in_norm
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_MRISPreproc:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, target='', hemi="enumerate(('lh','rh'))", **options):
        from nipype.interfaces.freesurfer.model import MRISPreproc
        at = MRISPreproc()
        at.inputs.target = target
        at.inputs.hemi = hemi
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_MRISPreprocReconAll:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, target='', hemi="enumerate(('lh','rh'))", **options):
        from nipype.interfaces.freesurfer.model import MRISPreprocReconAll
        at = MRISPreprocReconAll()
        at.inputs.target = target
        at.inputs.hemi = hemi
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_MRITessellate:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", label_value=0, **options):
        from nipype.interfaces.freesurfer.utils import MRITessellate
        at = MRITessellate()
        at.inputs.in_file = in_file
        at.inputs.label_value = label_value
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def surface(self) -> None:
        return self.res.outputs.surface

###############################################################################


class freesurfer_MRIsCALabel:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subject_id='', hemisphere="enumerate(('lh','rh'))", canonsurf="path", classifier="path", smoothwm="path", curv="path", sulc="path", **options):
        from nipype.interfaces.freesurfer.preprocess import MRIsCALabel
        at = MRIsCALabel()
        at.inputs.subject_id = subject_id
        at.inputs.hemisphere = hemisphere
        at.inputs.canonsurf = canonsurf
        at.inputs.classifier = classifier
        at.inputs.smoothwm = smoothwm
        at.inputs.curv = curv
        at.inputs.sulc = sulc
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_MRIsCalc:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file1="path", action='', out_file="path", **options):
        from nipype.interfaces.freesurfer.utils import MRIsCalc
        at = MRIsCalc()
        at.inputs.in_file1 = in_file1
        at.inputs.action = action
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_MRIsCombine:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files="path", out_file="path", **options):
        from nipype.interfaces.freesurfer.utils import MRIsCombine
        at = MRIsCombine()
        at.inputs.in_files = in_files
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_MRIsConvert:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.utils import MRIsConvert
        at = MRIsConvert()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def converted(self) -> None:
        return self.res.outputs.converted

###############################################################################


class freesurfer_MRIsExpand:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", distance=0.0, **options):
        from nipype.interfaces.freesurfer.utils import MRIsExpand
        at = MRIsExpand()
        at.inputs.in_file = in_file
        at.inputs.distance = distance
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_MRIsInflate:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.utils import MRIsInflate
        at = MRIsInflate()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_sulc(self) -> None:
        return self.res.outputs.out_sulc

###############################################################################


class freesurfer_MS_LDA:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, lda_labels=0, weight_file="path", vol_synth_file="path", images=["path"], **options):
        from nipype.interfaces.freesurfer.model import MS_LDA
        at = MS_LDA()
        at.inputs.lda_labels = lda_labels
        at.inputs.weight_file = weight_file
        at.inputs.vol_synth_file = vol_synth_file
        at.inputs.images = images
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def weight_file(self) -> None:
        return self.res.outputs.weight_file

    def vol_synth_file(self) -> None:
        return self.res.outputs.vol_synth_file

###############################################################################


class freesurfer_MakeAverageSubject:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subjects_ids=[''], **options):
        from nipype.interfaces.freesurfer.utils import MakeAverageSubject
        at = MakeAverageSubject()
        at.inputs.subjects_ids = subjects_ids
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def average_subject_name(self) -> str:
        return self.res.outputs.average_subject_name

###############################################################################


class freesurfer_MakeSurfaces:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, hemisphere="enumerate(('lh','rh'))", subject_id='', in_orig="path", in_wm="path", in_filled="path", **options):
        from nipype.interfaces.freesurfer.utils import MakeSurfaces
        at = MakeSurfaces()
        at.inputs.hemisphere = hemisphere
        at.inputs.subject_id = subject_id
        at.inputs.in_orig = in_orig
        at.inputs.in_wm = in_wm
        at.inputs.in_filled = in_filled
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_white(self) -> None:
        return self.res.outputs.out_white

    def out_curv(self) -> None:
        return self.res.outputs.out_curv

    def out_area(self) -> None:
        return self.res.outputs.out_area

    def out_cortex(self) -> None:
        return self.res.outputs.out_cortex

    def out_pial(self) -> None:
        return self.res.outputs.out_pial

    def out_thickness(self) -> None:
        return self.res.outputs.out_thickness

###############################################################################


class freesurfer_Normalize:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.preprocess import Normalize
        at = Normalize()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_OneSampleTTest:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.model import OneSampleTTest
        at = OneSampleTTest()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def glm_dir(self) -> None:
        return self.res.outputs.glm_dir

    def beta_file(self) -> None:
        return self.res.outputs.beta_file

    def error_file(self) -> None:
        return self.res.outputs.error_file

    def error_var_file(self) -> None:
        return self.res.outputs.error_var_file

    def error_stddev_file(self) -> None:
        return self.res.outputs.error_stddev_file

    def estimate_file(self) -> None:
        return self.res.outputs.estimate_file

    def mask_file(self) -> None:
        return self.res.outputs.mask_file

    def fwhm_file(self) -> None:
        return self.res.outputs.fwhm_file

    def dof_file(self) -> None:
        return self.res.outputs.dof_file

    def gamma_file(self) -> list[str]:
        return self.res.outputs.gamma_file

    def gamma_var_file(self) -> list[str]:
        return self.res.outputs.gamma_var_file

    def sig_file(self) -> list[str]:
        return self.res.outputs.sig_file

    def ftest_file(self) -> list[str]:
        return self.res.outputs.ftest_file

    def spatial_eigenvectors(self) -> None:
        return self.res.outputs.spatial_eigenvectors

    def frame_eigenvectors(self) -> None:
        return self.res.outputs.frame_eigenvectors

    def singular_values(self) -> None:
        return self.res.outputs.singular_values

    def svd_stats_file(self) -> None:
        return self.res.outputs.svd_stats_file

    def k2p_file(self) -> None:
        return self.res.outputs.k2p_file

    def bp_file(self) -> None:
        return self.res.outputs.bp_file

###############################################################################


class freesurfer_Paint:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_surf="path", template="path", **options):
        from nipype.interfaces.freesurfer.registration import Paint
        at = Paint()
        at.inputs.in_surf = in_surf
        at.inputs.template = template
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_ParcellationStats:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subject_id='', hemisphere="enumerate(('lh','rh'))", wm="path", lh_white="path", rh_white="path", lh_pial="path", rh_pial="path", transform="path", thickness="path", brainmask="path", aseg="path", ribbon="path", **options):
        from nipype.interfaces.freesurfer.utils import ParcellationStats
        at = ParcellationStats()
        at.inputs.subject_id = subject_id
        at.inputs.hemisphere = hemisphere
        at.inputs.wm = wm
        at.inputs.lh_white = lh_white
        at.inputs.rh_white = rh_white
        at.inputs.lh_pial = lh_pial
        at.inputs.rh_pial = rh_pial
        at.inputs.transform = transform
        at.inputs.thickness = thickness
        at.inputs.brainmask = brainmask
        at.inputs.aseg = aseg
        at.inputs.ribbon = ribbon
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_table(self) -> None:
        return self.res.outputs.out_table

    def out_color(self) -> None:
        return self.res.outputs.out_color

###############################################################################


class freesurfer_ParseDICOMDir:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dicom_dir="path", **options):
        from nipype.interfaces.freesurfer.preprocess import ParseDICOMDir
        at = ParseDICOMDir()
        at.inputs.dicom_dir = dicom_dir
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def dicom_info_file(self) -> None:
        return self.res.outputs.dicom_info_file

###############################################################################


class freesurfer_ReconAll:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.freesurfer.preprocess import ReconAll
        at = ReconAll()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def subjects_dir(self) -> None:
        return self.res.outputs.subjects_dir

    def subject_id(self) -> str:
        return self.res.outputs.subject_id

    def T1(self) -> None:
        return self.res.outputs.T1

    def aseg(self) -> None:
        return self.res.outputs.aseg

    def brain(self) -> None:
        return self.res.outputs.brain

    def brainmask(self) -> None:
        return self.res.outputs.brainmask

    def filled(self) -> None:
        return self.res.outputs.filled

    def norm(self) -> None:
        return self.res.outputs.norm

    def nu(self) -> None:
        return self.res.outputs.nu

    def orig(self) -> None:
        return self.res.outputs.orig

    def rawavg(self) -> None:
        return self.res.outputs.rawavg

    def ribbon(self) -> list[None]:
        return self.res.outputs.ribbon

    def wm(self) -> None:
        return self.res.outputs.wm

    def wmparc(self) -> None:
        return self.res.outputs.wmparc

    def curv(self) -> list[None]:
        return self.res.outputs.curv

    def avg_curv(self) -> list[None]:
        return self.res.outputs.avg_curv

    def inflated(self) -> list[None]:
        return self.res.outputs.inflated

    def pial(self) -> list[None]:
        return self.res.outputs.pial

    def area_pial(self) -> list[None]:
        return self.res.outputs.area_pial

    def curv_pial(self) -> list[None]:
        return self.res.outputs.curv_pial

    def smoothwm(self) -> list[None]:
        return self.res.outputs.smoothwm

    def sphere(self) -> list[None]:
        return self.res.outputs.sphere

    def sulc(self) -> list[None]:
        return self.res.outputs.sulc

    def thickness(self) -> list[None]:
        return self.res.outputs.thickness

    def volume(self) -> list[None]:
        return self.res.outputs.volume

    def white(self) -> list[None]:
        return self.res.outputs.white

    def jacobian_white(self) -> list[None]:
        return self.res.outputs.jacobian_white

    def graymid(self) -> list[None]:
        return self.res.outputs.graymid

    def label(self) -> list[None]:
        return self.res.outputs.label

    def annot(self) -> list[None]:
        return self.res.outputs.annot

    def aparc_aseg(self) -> list[None]:
        return self.res.outputs.aparc_aseg

    def sphere_reg(self) -> list[None]:
        return self.res.outputs.sphere_reg

    def aseg_stats(self) -> list[None]:
        return self.res.outputs.aseg_stats

    def wmparc_stats(self) -> list[None]:
        return self.res.outputs.wmparc_stats

    def aparc_stats(self) -> list[None]:
        return self.res.outputs.aparc_stats

    def BA_stats(self) -> list[None]:
        return self.res.outputs.BA_stats

    def aparc_a2009s_stats(self) -> list[None]:
        return self.res.outputs.aparc_a2009s_stats

    def curv_stats(self) -> list[None]:
        return self.res.outputs.curv_stats

    def entorhinal_exvivo_stats(self) -> list[None]:
        return self.res.outputs.entorhinal_exvivo_stats

###############################################################################


class freesurfer_Register:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_surf="path", target="path", in_sulc="path", **options):
        from nipype.interfaces.freesurfer.registration import Register
        at = Register()
        at.inputs.in_surf = in_surf
        at.inputs.target = target
        at.inputs.in_sulc = in_sulc
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_RegisterAVItoTalairach:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", target="path", vox2vox="path", **options):
        from nipype.interfaces.freesurfer.registration import RegisterAVItoTalairach
        at = RegisterAVItoTalairach()
        at.inputs.in_file = in_file
        at.inputs.target = target
        at.inputs.vox2vox = vox2vox
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def log_file(self) -> None:
        return self.res.outputs.log_file

###############################################################################


class freesurfer_RelabelHypointensities:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, lh_white="path", rh_white="path", aseg="path", **options):
        from nipype.interfaces.freesurfer.utils import RelabelHypointensities
        at = RelabelHypointensities()
        at.inputs.lh_white = lh_white
        at.inputs.rh_white = rh_white
        at.inputs.aseg = aseg
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_RemoveIntersection:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.utils import RemoveIntersection
        at = RemoveIntersection()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_RemoveNeck:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", transform="path", template="path", **options):
        from nipype.interfaces.freesurfer.utils import RemoveNeck
        at = RemoveNeck()
        at.inputs.in_file = in_file
        at.inputs.transform = transform
        at.inputs.template = template
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_Resample:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", voxel_size=(0,), **options):
        from nipype.interfaces.freesurfer.preprocess import Resample
        at = Resample()
        at.inputs.in_file = in_file
        at.inputs.voxel_size = voxel_size
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def resampled_file(self) -> None:
        return self.res.outputs.resampled_file

###############################################################################


class freesurfer_RobustRegister:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source_file="path", target_file="path", **options):
        from nipype.interfaces.freesurfer.preprocess import RobustRegister
        at = RobustRegister()
        at.inputs.source_file = source_file
        at.inputs.target_file = target_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_reg_file(self) -> None:
        return self.res.outputs.out_reg_file

    def registered_file(self) -> None:
        return self.res.outputs.registered_file

    def weights_file(self) -> None:
        return self.res.outputs.weights_file

    def half_source(self) -> None:
        return self.res.outputs.half_source

    def half_targ(self) -> None:
        return self.res.outputs.half_targ

    def half_weights(self) -> None:
        return self.res.outputs.half_weights

    def half_source_xfm(self) -> None:
        return self.res.outputs.half_source_xfm

    def half_targ_xfm(self) -> None:
        return self.res.outputs.half_targ_xfm

###############################################################################


class freesurfer_RobustTemplate:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], out_file="path", **options):
        from nipype.interfaces.freesurfer.longitudinal import RobustTemplate
        at = RobustTemplate()
        at.inputs.in_files = in_files
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def transform_outputs(self) -> list[None]:
        return self.res.outputs.transform_outputs

    def scaled_intensity_outputs(self) -> list[None]:
        return self.res.outputs.scaled_intensity_outputs

###############################################################################


class freesurfer_SampleToSurface:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source_file="path", hemi="enumerate(('lh','rh'))", **options):
        from nipype.interfaces.freesurfer.utils import SampleToSurface
        at = SampleToSurface()
        at.inputs.source_file = source_file
        at.inputs.hemi = hemi
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def hits_file(self) -> None:
        return self.res.outputs.hits_file

    def vox_file(self) -> None:
        return self.res.outputs.vox_file

###############################################################################


class freesurfer_SegStats:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.freesurfer.model import SegStats
        at = SegStats()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def summary_file(self) -> None:
        return self.res.outputs.summary_file

    def avgwf_txt_file(self) -> None:
        return self.res.outputs.avgwf_txt_file

    def avgwf_file(self) -> None:
        return self.res.outputs.avgwf_file

    def sf_avg_file(self) -> None:
        return self.res.outputs.sf_avg_file

###############################################################################


class freesurfer_SegStatsReconAll:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subject_id='', ribbon="path", transform="path", lh_orig_nofix="path", rh_orig_nofix="path", lh_white="path", rh_white="path", lh_pial="path", rh_pial="path", **options):
        from nipype.interfaces.freesurfer.model import SegStatsReconAll
        at = SegStatsReconAll()
        at.inputs.subject_id = subject_id
        at.inputs.ribbon = ribbon
        at.inputs.transform = transform
        at.inputs.lh_orig_nofix = lh_orig_nofix
        at.inputs.rh_orig_nofix = rh_orig_nofix
        at.inputs.lh_white = lh_white
        at.inputs.rh_white = rh_white
        at.inputs.lh_pial = lh_pial
        at.inputs.rh_pial = rh_pial
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def summary_file(self) -> None:
        return self.res.outputs.summary_file

    def avgwf_txt_file(self) -> None:
        return self.res.outputs.avgwf_txt_file

    def avgwf_file(self) -> None:
        return self.res.outputs.avgwf_file

    def sf_avg_file(self) -> None:
        return self.res.outputs.sf_avg_file

###############################################################################


class freesurfer_SegmentCC:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", in_norm="path", out_rotation="path", subject_id='', **options):
        from nipype.interfaces.freesurfer.preprocess import SegmentCC
        at = SegmentCC()
        at.inputs.in_file = in_file
        at.inputs.in_norm = in_norm
        at.inputs.out_rotation = out_rotation
        at.inputs.subject_id = subject_id
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_rotation(self) -> None:
        return self.res.outputs.out_rotation

###############################################################################


class freesurfer_SegmentWM:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.freesurfer.preprocess import SegmentWM
        at = SegmentWM()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_Smooth:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", reg_file="path", **options):
        from nipype.interfaces.freesurfer.preprocess import Smooth
        at = Smooth()
        at.inputs.in_file = in_file
        at.inputs.reg_file = reg_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def smoothed_file(self) -> None:
        return self.res.outputs.smoothed_file

###############################################################################


class freesurfer_SmoothTessellation:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.utils import SmoothTessellation
        at = SmoothTessellation()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def surface(self) -> None:
        return self.res.outputs.surface

###############################################################################


class freesurfer_Sphere:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.freesurfer.utils import Sphere
        at = Sphere()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_SphericalAverage:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_surf="path", hemisphere="enumerate(('lh','rh'))", fname='', which="enumerate(('coords','label','vals','curv','area'))", subject_id='', **options):
        from nipype.interfaces.freesurfer.model import SphericalAverage
        at = SphericalAverage()
        at.inputs.in_surf = in_surf
        at.inputs.hemisphere = hemisphere
        at.inputs.fname = fname
        at.inputs.which = which
        at.inputs.subject_id = subject_id
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_Surface2VolTransform:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, hemi='', **options):
        from nipype.interfaces.freesurfer.utils import Surface2VolTransform
        at = Surface2VolTransform()
        at.inputs.hemi = hemi
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def transformed_file(self) -> None:
        return self.res.outputs.transformed_file

    def vertexvol_file(self) -> None:
        return self.res.outputs.vertexvol_file

###############################################################################


class freesurfer_SurfaceSmooth:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", subject_id='', hemi="enumerate(('lh','rh'))", **options):
        from nipype.interfaces.freesurfer.utils import SurfaceSmooth
        at = SurfaceSmooth()
        at.inputs.in_file = in_file
        at.inputs.subject_id = subject_id
        at.inputs.hemi = hemi
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_SurfaceSnapshots:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subject_id='', hemi="enumerate(('lh','rh'))", surface='', **options):
        from nipype.interfaces.freesurfer.utils import SurfaceSnapshots
        at = SurfaceSnapshots()
        at.inputs.subject_id = subject_id
        at.inputs.hemi = hemi
        at.inputs.surface = surface
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def snapshots(self) -> list[None]:
        return self.res.outputs.snapshots

###############################################################################


class freesurfer_SurfaceTransform:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source_subject='', hemi="enumerate(('lh','rh'))", target_subject='', **options):
        from nipype.interfaces.freesurfer.utils import SurfaceTransform
        at = SurfaceTransform()
        at.inputs.source_subject = source_subject
        at.inputs.hemi = hemi
        at.inputs.target_subject = target_subject
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_SynthesizeFLASH:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, tr=0.0, flip_angle=0.0, te=0.0, t1_image="path", pd_image="path", **options):
        from nipype.interfaces.freesurfer.preprocess import SynthesizeFLASH
        at = SynthesizeFLASH()
        at.inputs.tr = tr
        at.inputs.flip_angle = flip_angle
        at.inputs.te = te
        at.inputs.t1_image = t1_image
        at.inputs.pd_image = pd_image
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class freesurfer_TalairachAVI:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.freesurfer.utils import TalairachAVI
        at = TalairachAVI()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def out_log(self) -> None:
        return self.res.outputs.out_log

    def out_txt(self) -> None:
        return self.res.outputs.out_txt

###############################################################################


class freesurfer_TalairachQC:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, log_file="path", **options):
        from nipype.interfaces.freesurfer.utils import TalairachQC
        at = TalairachQC()
        at.inputs.log_file = log_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def log_file(self) -> None:
        return self.res.outputs.log_file

###############################################################################


class freesurfer_Tkregister2:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, moving_image="path", reg_file="path", **options):
        from nipype.interfaces.freesurfer.utils import Tkregister2
        at = Tkregister2()
        at.inputs.moving_image = moving_image
        at.inputs.reg_file = reg_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def reg_file(self) -> None:
        return self.res.outputs.reg_file

    def fsl_file(self) -> None:
        return self.res.outputs.fsl_file

    def lta_file(self) -> None:
        return self.res.outputs.lta_file

###############################################################################


class freesurfer_UnpackSDICOMDir:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, source_dir="path", **options):
        from nipype.interfaces.freesurfer.preprocess import UnpackSDICOMDir
        at = UnpackSDICOMDir()
        at.inputs.source_dir = source_dir
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class freesurfer_VolumeMask:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, left_whitelabel=0, left_ribbonlabel=0, right_whitelabel=0, right_ribbonlabel=0, lh_pial="path", rh_pial="path", lh_white="path", rh_white="path", subject_id='', **options):
        from nipype.interfaces.freesurfer.utils import VolumeMask
        at = VolumeMask()
        at.inputs.left_whitelabel = left_whitelabel
        at.inputs.left_ribbonlabel = left_ribbonlabel
        at.inputs.right_whitelabel = right_whitelabel
        at.inputs.right_ribbonlabel = right_ribbonlabel
        at.inputs.lh_pial = lh_pial
        at.inputs.rh_pial = rh_pial
        at.inputs.lh_white = lh_white
        at.inputs.rh_white = rh_white
        at.inputs.subject_id = subject_id
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_ribbon(self) -> None:
        return self.res.outputs.out_ribbon

    def lh_ribbon(self) -> None:
        return self.res.outputs.lh_ribbon

    def rh_ribbon(self) -> None:
        return self.res.outputs.rh_ribbon

###############################################################################


class freesurfer_WatershedSkullStrip:
    """
    Note:
        dependencies: Nipype,freesurfer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.freesurfer.preprocess import WatershedSkullStrip
        at = WatershedSkullStrip()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


