class spm_Analyze2nii:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, analyze_file="path", **options):
        from nipype.interfaces.spm.utils import Analyze2nii
        at = Analyze2nii()
        at.inputs.analyze_file = analyze_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def nifti_file(self) -> None:
        return self.res.outputs.nifti_file

    def matlab_cmd(self) -> str:
        return self.res.outputs.matlab_cmd

    def paths(self) -> list[None]:
        return self.res.outputs.paths

    def mfile(self) -> bool:
        return self.res.outputs.mfile

    def use_mcr(self) -> bool:
        return self.res.outputs.use_mcr

    def use_v8struct(self) -> bool:
        return self.res.outputs.use_v8struct

###############################################################################


class spm_ApplyInverseDeformation:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.spm.utils import ApplyInverseDeformation
        at = ApplyInverseDeformation()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_files(self) -> list[None]:
        return self.res.outputs.out_files

###############################################################################


class spm_ApplyTransform:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", mat="path", **options):
        from nipype.interfaces.spm.utils import ApplyTransform
        at = ApplyTransform()
        at.inputs.in_file = in_file
        at.inputs.mat = mat
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class spm_ApplyVDM:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], vdmfile="path", **options):
        from nipype.interfaces.spm.preprocess import ApplyVDM
        at = ApplyVDM()
        at.inputs.in_files = in_files
        at.inputs.vdmfile = vdmfile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_files(self) -> list[list[None]]:
        return self.res.outputs.out_files

    def mean_image(self) -> None:
        return self.res.outputs.mean_image

###############################################################################


class spm_CalcCoregAffine:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, target="path", moving="path", **options):
        from nipype.interfaces.spm.utils import CalcCoregAffine
        at = CalcCoregAffine()
        at.inputs.target = target
        at.inputs.moving = moving
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mat(self) -> None:
        return self.res.outputs.mat

    def invmat(self) -> None:
        return self.res.outputs.invmat

###############################################################################


class spm_Coregister:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, target="path", source=["path"], **options):
        from nipype.interfaces.spm.preprocess import Coregister
        at = Coregister()
        at.inputs.target = target
        at.inputs.source = source
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def coregistered_source(self) -> list[None]:
        return self.res.outputs.coregistered_source

    def coregistered_files(self) -> list[None]:
        return self.res.outputs.coregistered_files

###############################################################################


class spm_CreateWarped:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, image_files=["path"], flowfield_files=["path"], **options):
        from nipype.interfaces.spm.preprocess import CreateWarped
        at = CreateWarped()
        at.inputs.image_files = image_files
        at.inputs.flowfield_files = flowfield_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def warped_files(self) -> list[None]:
        return self.res.outputs.warped_files

###############################################################################


class spm_DARTEL:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, image_files=[["path"]], **options):
        from nipype.interfaces.spm.preprocess import DARTEL
        at = DARTEL()
        at.inputs.image_files = image_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def final_template_file(self) -> None:
        return self.res.outputs.final_template_file

    def template_files(self) -> list[None]:
        return self.res.outputs.template_files

    def dartel_flow_fields(self) -> list[None]:
        return self.res.outputs.dartel_flow_fields

###############################################################################


class spm_DARTELNorm2MNI:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, template_file="path", flowfield_files=["path"], apply_to_files=["path"], **options):
        from nipype.interfaces.spm.preprocess import DARTELNorm2MNI
        at = DARTELNorm2MNI()
        at.inputs.template_file = template_file
        at.inputs.flowfield_files = flowfield_files
        at.inputs.apply_to_files = apply_to_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def normalized_files(self) -> list[None]:
        return self.res.outputs.normalized_files

    def normalization_parameter_file(self) -> None:
        return self.res.outputs.normalization_parameter_file

###############################################################################


class spm_DicomImport:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.spm.utils import DicomImport
        at = DicomImport()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_files(self) -> list[None]:
        return self.res.outputs.out_files

###############################################################################


class spm_EstimateContrast:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, spm_mat_file="path", contrasts=[(0,)], beta_images=["path"], residual_image="path", **options):
        from nipype.interfaces.spm.model import EstimateContrast
        at = EstimateContrast()
        at.inputs.spm_mat_file = spm_mat_file
        at.inputs.contrasts = contrasts
        at.inputs.beta_images = beta_images
        at.inputs.residual_image = residual_image
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def con_images(self) -> list[None]:
        return self.res.outputs.con_images

    def spmT_images(self) -> list[None]:
        return self.res.outputs.spmT_images

    def ess_images(self) -> list[None]:
        return self.res.outputs.ess_images

    def spmF_images(self) -> list[None]:
        return self.res.outputs.spmF_images

    def spm_mat_file(self) -> None:
        return self.res.outputs.spm_mat_file

###############################################################################


class spm_EstimateModel:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, spm_mat_file="path", estimation_method="enumerate(('Classical','Bayesian2','Bayesian'))", **options):
        from nipype.interfaces.spm.model import EstimateModel
        at = EstimateModel()
        at.inputs.spm_mat_file = spm_mat_file
        at.inputs.estimation_method = estimation_method
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mask_image(self) -> None:
        return self.res.outputs.mask_image

    def beta_images(self) -> list[None]:
        return self.res.outputs.beta_images

    def residual_image(self) -> None:
        return self.res.outputs.residual_image

    def residual_images(self) -> list[None]:
        return self.res.outputs.residual_images

    def RPVimage(self) -> None:
        return self.res.outputs.RPVimage

    def spm_mat_file(self) -> None:
        return self.res.outputs.spm_mat_file

    def labels(self) -> None:
        return self.res.outputs.labels

    def SDerror(self) -> list[None]:
        return self.res.outputs.SDerror

    def ARcoef(self) -> list[None]:
        return self.res.outputs.ARcoef

    def Cbetas(self) -> list[None]:
        return self.res.outputs.Cbetas

    def SDbetas(self) -> list[None]:
        return self.res.outputs.SDbetas

    def con_images(self) -> list[None]:
        return self.res.outputs.con_images

    def spmT_images(self) -> list[None]:
        return self.res.outputs.spmT_images

    def ess_images(self) -> list[None]:
        return self.res.outputs.ess_images

    def spmF_images(self) -> list[None]:
        return self.res.outputs.spmF_images

###############################################################################


class spm_FieldMap:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, phase_file="path", magnitude_file="path", echo_times=(0,), blip_direction='', total_readout_time=0.0, epi_file="path", **options):
        from nipype.interfaces.spm.preprocess import FieldMap
        at = FieldMap()
        at.inputs.phase_file = phase_file
        at.inputs.magnitude_file = magnitude_file
        at.inputs.echo_times = echo_times
        at.inputs.blip_direction = blip_direction
        at.inputs.total_readout_time = total_readout_time
        at.inputs.epi_file = epi_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def vdm(self) -> None:
        return self.res.outputs.vdm

###############################################################################


class spm_Level1Design:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, timing_units="enumerate(('secs','scans'))", interscan_interval=0.0, session_info='', bases="enumerate(('hrf','fourier','fourier_han','gamma','fir'))", **options):
        from nipype.interfaces.spm.model import Level1Design
        at = Level1Design()
        at.inputs.timing_units = timing_units
        at.inputs.interscan_interval = interscan_interval
        at.inputs.session_info = session_info
        at.inputs.bases = bases
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def spm_mat_file(self) -> None:
        return self.res.outputs.spm_mat_file

###############################################################################


class spm_MultiChannelNewSegment:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.spm.preprocess import MultiChannelNewSegment
        at = MultiChannelNewSegment()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def native_class_images(self) -> list[list[None]]:
        return self.res.outputs.native_class_images

    def dartel_input_images(self) -> list[list[None]]:
        return self.res.outputs.dartel_input_images

    def normalized_class_images(self) -> list[list[None]]:
        return self.res.outputs.normalized_class_images

    def modulated_class_images(self) -> list[list[None]]:
        return self.res.outputs.modulated_class_images

    def transformation_mat(self) -> list[None]:
        return self.res.outputs.transformation_mat

    def bias_corrected_images(self) -> list[None]:
        return self.res.outputs.bias_corrected_images

    def bias_field_images(self) -> list[None]:
        return self.res.outputs.bias_field_images

    def forward_deformation_field(self) -> list[None]:
        return self.res.outputs.forward_deformation_field

    def inverse_deformation_field(self) -> list[None]:
        return self.res.outputs.inverse_deformation_field

###############################################################################


class spm_MultipleRegressionDesign:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files="path", **options):
        from nipype.interfaces.spm.model import MultipleRegressionDesign
        at = MultipleRegressionDesign()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def spm_mat_file(self) -> None:
        return self.res.outputs.spm_mat_file

###############################################################################


class spm_NewSegment:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, channel_files=["path"], **options):
        from nipype.interfaces.spm.preprocess import NewSegment
        at = NewSegment()
        at.inputs.channel_files = channel_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def native_class_images(self) -> list[list[None]]:
        return self.res.outputs.native_class_images

    def dartel_input_images(self) -> list[list[None]]:
        return self.res.outputs.dartel_input_images

    def normalized_class_images(self) -> list[list[None]]:
        return self.res.outputs.normalized_class_images

    def modulated_class_images(self) -> list[list[None]]:
        return self.res.outputs.modulated_class_images

    def transformation_mat(self) -> list[None]:
        return self.res.outputs.transformation_mat

    def bias_corrected_images(self) -> list[None]:
        return self.res.outputs.bias_corrected_images

    def bias_field_images(self) -> list[None]:
        return self.res.outputs.bias_field_images

    def forward_deformation_field(self) -> list[None]:
        return self.res.outputs.forward_deformation_field

    def inverse_deformation_field(self) -> list[None]:
        return self.res.outputs.inverse_deformation_field

###############################################################################


class spm_Normalize:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.spm.preprocess import Normalize
        at = Normalize()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def normalization_parameters(self) -> list[None]:
        return self.res.outputs.normalization_parameters

    def normalized_source(self) -> list[None]:
        return self.res.outputs.normalized_source

    def normalized_files(self) -> list[None]:
        return self.res.outputs.normalized_files

###############################################################################


class spm_Normalize12:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.spm.preprocess import Normalize12
        at = Normalize12()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def deformation_field(self) -> list[None]:
        return self.res.outputs.deformation_field

    def normalized_image(self) -> list[None]:
        return self.res.outputs.normalized_image

    def normalized_files(self) -> list[None]:
        return self.res.outputs.normalized_files

###############################################################################


class spm_OneSampleTTestDesign:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files="path", **options):
        from nipype.interfaces.spm.model import OneSampleTTestDesign
        at = OneSampleTTestDesign()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def spm_mat_file(self) -> None:
        return self.res.outputs.spm_mat_file

###############################################################################


class spm_PairedTTestDesign:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, paired_files="path", **options):
        from nipype.interfaces.spm.model import PairedTTestDesign
        at = PairedTTestDesign()
        at.inputs.paired_files = paired_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def spm_mat_file(self) -> None:
        return self.res.outputs.spm_mat_file

###############################################################################


class spm_Realign:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.spm.preprocess import Realign
        at = Realign()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mean_image(self) -> None:
        return self.res.outputs.mean_image

    def modified_in_files(self) -> list[list[None]]:
        return self.res.outputs.modified_in_files

    def realigned_files(self) -> list[list[None]]:
        return self.res.outputs.realigned_files

    def realignment_parameters(self) -> list[None]:
        return self.res.outputs.realignment_parameters

###############################################################################


class spm_RealignUnwarp:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.spm.preprocess import RealignUnwarp
        at = RealignUnwarp()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mean_image(self) -> None:
        return self.res.outputs.mean_image

    def modified_in_files(self) -> list[list[None]]:
        return self.res.outputs.modified_in_files

    def realigned_unwarped_files(self) -> list[list[None]]:
        return self.res.outputs.realigned_unwarped_files

    def realignment_parameters(self) -> list[None]:
        return self.res.outputs.realignment_parameters

###############################################################################


class spm_Reslice:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", space_defining="path", **options):
        from nipype.interfaces.spm.utils import Reslice
        at = Reslice()
        at.inputs.in_file = in_file
        at.inputs.space_defining = space_defining
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class spm_ResliceToReference:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.spm.utils import ResliceToReference
        at = ResliceToReference()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_files(self) -> list[None]:
        return self.res.outputs.out_files

###############################################################################


class spm_SPMCommand:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.spm.base import SPMCommand
        at = SPMCommand()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class spm_Segment:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, data=["path"], **options):
        from nipype.interfaces.spm.preprocess import Segment
        at = Segment()
        at.inputs.data = data
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def native_gm_image(self) -> None:
        return self.res.outputs.native_gm_image

    def normalized_gm_image(self) -> None:
        return self.res.outputs.normalized_gm_image

    def modulated_gm_image(self) -> None:
        return self.res.outputs.modulated_gm_image

    def native_wm_image(self) -> None:
        return self.res.outputs.native_wm_image

    def normalized_wm_image(self) -> None:
        return self.res.outputs.normalized_wm_image

    def modulated_wm_image(self) -> None:
        return self.res.outputs.modulated_wm_image

    def native_csf_image(self) -> None:
        return self.res.outputs.native_csf_image

    def normalized_csf_image(self) -> None:
        return self.res.outputs.normalized_csf_image

    def modulated_csf_image(self) -> None:
        return self.res.outputs.modulated_csf_image

    def modulated_input_image(self) -> None:
        return self.res.outputs.modulated_input_image

    def bias_corrected_image(self) -> None:
        return self.res.outputs.bias_corrected_image

    def transformation_mat(self) -> None:
        return self.res.outputs.transformation_mat

    def inverse_transformation_mat(self) -> None:
        return self.res.outputs.inverse_transformation_mat

###############################################################################


class spm_SliceTiming:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=[["path"]], num_slices=0, time_repetition=0.0, time_acquisition=0.0, slice_order=[0.0], ref_slice=0.0, **options):
        from nipype.interfaces.spm.preprocess import SliceTiming
        at = SliceTiming()
        at.inputs.in_files = in_files
        at.inputs.num_slices = num_slices
        at.inputs.time_repetition = time_repetition
        at.inputs.time_acquisition = time_acquisition
        at.inputs.slice_order = slice_order
        at.inputs.ref_slice = ref_slice
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def timecorrected_files(self) -> list[list[None]]:
        return self.res.outputs.timecorrected_files

###############################################################################


class spm_Smooth:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.spm.preprocess import Smooth
        at = Smooth()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def smoothed_files(self) -> list[None]:
        return self.res.outputs.smoothed_files

###############################################################################


class spm_Threshold:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, spm_mat_file="path", stat_image="path", contrast_index=0, **options):
        from nipype.interfaces.spm.model import Threshold
        at = Threshold()
        at.inputs.spm_mat_file = spm_mat_file
        at.inputs.stat_image = stat_image
        at.inputs.contrast_index = contrast_index
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def thresholded_map(self) -> None:
        return self.res.outputs.thresholded_map

    def n_clusters(self) -> int:
        return self.res.outputs.n_clusters

    def pre_topo_fdr_map(self) -> None:
        return self.res.outputs.pre_topo_fdr_map

    def pre_topo_n_clusters(self) -> int:
        return self.res.outputs.pre_topo_n_clusters

    def activation_forced(self) -> bool:
        return self.res.outputs.activation_forced

    def cluster_forming_thr(self) -> float:
        return self.res.outputs.cluster_forming_thr

###############################################################################


class spm_TwoSampleTTestDesign:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, group1_files="path", group2_files="path", **options):
        from nipype.interfaces.spm.model import TwoSampleTTestDesign
        at = TwoSampleTTestDesign()
        at.inputs.group1_files = group1_files
        at.inputs.group2_files = group2_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def spm_mat_file(self) -> None:
        return self.res.outputs.spm_mat_file

###############################################################################


class spm_VBMSegment:
    """
    Note:
        dependencies: Nipype,spm
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.spm.preprocess import VBMSegment
        at = VBMSegment()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def native_class_images(self) -> list[list[None]]:
        return self.res.outputs.native_class_images

    def dartel_input_images(self) -> list[list[None]]:
        return self.res.outputs.dartel_input_images

    def normalized_class_images(self) -> list[list[None]]:
        return self.res.outputs.normalized_class_images

    def modulated_class_images(self) -> list[list[None]]:
        return self.res.outputs.modulated_class_images

    def transformation_mat(self) -> list[None]:
        return self.res.outputs.transformation_mat

    def bias_corrected_images(self) -> list[None]:
        return self.res.outputs.bias_corrected_images

    def normalized_bias_corrected_images(self) -> list[None]:
        return self.res.outputs.normalized_bias_corrected_images

    def pve_label_native_images(self) -> list[None]:
        return self.res.outputs.pve_label_native_images

    def pve_label_normalized_images(self) -> list[None]:
        return self.res.outputs.pve_label_normalized_images

    def pve_label_registered_images(self) -> list[None]:
        return self.res.outputs.pve_label_registered_images

    def forward_deformation_field(self) -> list[None]:
        return self.res.outputs.forward_deformation_field

    def inverse_deformation_field(self) -> list[None]:
        return self.res.outputs.inverse_deformation_field

    def jacobian_determinant_images(self) -> list[None]:
        return self.res.outputs.jacobian_determinant_images

###############################################################################


