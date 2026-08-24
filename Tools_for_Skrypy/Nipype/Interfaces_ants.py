class ants_AI:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, fixed_image="path", moving_image="path", metric="enumerate(('Mattes','GC','MI','Regular','Random','None'))", **options):
        from nipype.interfaces.ants.utils import AI
        at = AI()
        at.inputs.fixed_image = fixed_image
        at.inputs.moving_image = moving_image
        at.inputs.metric = metric
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_transform(self) -> None:
        return self.res.outputs.output_transform

###############################################################################


class ants_ANTS:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, fixed_image=["path"], moving_image=["path"], metric="enumerate(('CC','MI','SMI','PR','SSD','MSQ','PSE'))", metric_weight=[0.0], radius=[0], output_transform_prefix='', transformation_model="enumerate(('Diff','Elast','Exp','Greedy Exp','SyN'))", **options):
        from nipype.interfaces.ants.registration import ANTS
        at = ANTS()
        at.inputs.fixed_image = fixed_image
        at.inputs.moving_image = moving_image
        at.inputs.metric = metric
        at.inputs.metric_weight = metric_weight
        at.inputs.radius = radius
        at.inputs.output_transform_prefix = output_transform_prefix
        at.inputs.transformation_model = transformation_model
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def affine_transform(self) -> None:
        return self.res.outputs.affine_transform

    def warp_transform(self) -> None:
        return self.res.outputs.warp_transform

    def inverse_warp_transform(self) -> None:
        return self.res.outputs.inverse_warp_transform

    def metaheader(self) -> None:
        return self.res.outputs.metaheader

    def metaheader_raw(self) -> None:
        return self.res.outputs.metaheader_raw

###############################################################################


class ants_AffineInitializer:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, fixed_image="path", moving_image="path", **options):
        from nipype.interfaces.ants.utils import AffineInitializer
        at = AffineInitializer()
        at.inputs.fixed_image = fixed_image
        at.inputs.moving_image = moving_image
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class ants_AntsJointFusion:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, target_image=[["path"]], atlas_image=[["path"]], atlas_segmentation_image=["path"], **options):
        from nipype.interfaces.ants.segmentation import AntsJointFusion
        at = AntsJointFusion()
        at.inputs.target_image = target_image
        at.inputs.atlas_image = atlas_image
        at.inputs.atlas_segmentation_image = atlas_segmentation_image
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_label_fusion(self) -> None:
        return self.res.outputs.out_label_fusion

    def out_intensity_fusion(self) -> list[None]:
        return self.res.outputs.out_intensity_fusion

    def out_label_post_prob(self) -> list[None]:
        return self.res.outputs.out_label_post_prob

    def out_atlas_voting_weight(self) -> list[None]:
        return self.res.outputs.out_atlas_voting_weight

###############################################################################


class ants_ApplyTransforms:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_image="path", reference_image="path", transforms=["path"], **options):
        from nipype.interfaces.ants.resampling import ApplyTransforms
        at = ApplyTransforms()
        at.inputs.input_image = input_image
        at.inputs.reference_image = reference_image
        at.inputs.transforms = transforms
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

###############################################################################


class ants_ApplyTransformsToPoints:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_file="path", transforms=["path"], **options):
        from nipype.interfaces.ants.resampling import ApplyTransformsToPoints
        at = ApplyTransformsToPoints()
        at.inputs.input_file = input_file
        at.inputs.transforms = transforms
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class ants_Atropos:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, intensity_images=["path"], mask_image="path", initialization="enumerate(('Random','Otsu','KMeans','PriorProbabilityImages','PriorLabelImage'))", number_of_tissue_classes=0, **options):
        from nipype.interfaces.ants.segmentation import Atropos
        at = Atropos()
        at.inputs.intensity_images = intensity_images
        at.inputs.mask_image = mask_image
        at.inputs.initialization = initialization
        at.inputs.number_of_tissue_classes = number_of_tissue_classes
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def classified_image(self) -> None:
        return self.res.outputs.classified_image

    def posteriors(self) -> list[None]:
        return self.res.outputs.posteriors

###############################################################################


class ants_AverageAffineTransform:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dimension='', output_affine_transform="path", transforms=["path"], **options):
        from nipype.interfaces.ants.utils import AverageAffineTransform
        at = AverageAffineTransform()
        at.inputs.dimension = dimension
        at.inputs.output_affine_transform = output_affine_transform
        at.inputs.transforms = transforms
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def affine_transform(self) -> None:
        return self.res.outputs.affine_transform

###############################################################################


class ants_AverageImages:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dimension='', normalize=True, images=["path"], **options):
        from nipype.interfaces.ants.utils import AverageImages
        at = AverageImages()
        at.inputs.dimension = dimension
        at.inputs.normalize = normalize
        at.inputs.images = images
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_average_image(self) -> None:
        return self.res.outputs.output_average_image

###############################################################################


class ants_BrainExtraction:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, anatomical_image="path", brain_template="path", brain_probability_mask="path", **options):
        from nipype.interfaces.ants.segmentation import BrainExtraction
        at = BrainExtraction()
        at.inputs.anatomical_image = anatomical_image
        at.inputs.brain_template = brain_template
        at.inputs.brain_probability_mask = brain_probability_mask
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def BrainExtractionMask(self) -> None:
        return self.res.outputs.BrainExtractionMask

    def BrainExtractionBrain(self) -> None:
        return self.res.outputs.BrainExtractionBrain

    def BrainExtractionCSF(self) -> None:
        return self.res.outputs.BrainExtractionCSF

    def BrainExtractionGM(self) -> None:
        return self.res.outputs.BrainExtractionGM

    def BrainExtractionInitialAffine(self) -> None:
        return self.res.outputs.BrainExtractionInitialAffine

    def BrainExtractionInitialAffineFixed(self) -> None:
        return self.res.outputs.BrainExtractionInitialAffineFixed

    def BrainExtractionInitialAffineMoving(self) -> None:
        return self.res.outputs.BrainExtractionInitialAffineMoving

    def BrainExtractionLaplacian(self) -> None:
        return self.res.outputs.BrainExtractionLaplacian

    def BrainExtractionPrior0GenericAffine(self) -> None:
        return self.res.outputs.BrainExtractionPrior0GenericAffine

    def BrainExtractionPrior1InverseWarp(self) -> None:
        return self.res.outputs.BrainExtractionPrior1InverseWarp

    def BrainExtractionPrior1Warp(self) -> None:
        return self.res.outputs.BrainExtractionPrior1Warp

    def BrainExtractionPriorWarped(self) -> None:
        return self.res.outputs.BrainExtractionPriorWarped

    def BrainExtractionSegmentation(self) -> None:
        return self.res.outputs.BrainExtractionSegmentation

    def BrainExtractionTemplateLaplacian(self) -> None:
        return self.res.outputs.BrainExtractionTemplateLaplacian

    def BrainExtractionTmp(self) -> None:
        return self.res.outputs.BrainExtractionTmp

    def BrainExtractionWM(self) -> None:
        return self.res.outputs.BrainExtractionWM

    def N4Corrected0(self) -> None:
        return self.res.outputs.N4Corrected0

    def N4Truncated0(self) -> None:
        return self.res.outputs.N4Truncated0

###############################################################################


class ants_ComposeMultiTransform:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, transforms=["path"], **options):
        from nipype.interfaces.ants.utils import ComposeMultiTransform
        at = ComposeMultiTransform()
        at.inputs.transforms = transforms
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_transform(self) -> None:
        return self.res.outputs.output_transform

###############################################################################


class ants_CompositeTransformUtil:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file=["path"], **options):
        from nipype.interfaces.ants.registration import CompositeTransformUtil
        at = CompositeTransformUtil()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def affine_transform(self) -> None:
        return self.res.outputs.affine_transform

    def displacement_field(self) -> None:
        return self.res.outputs.displacement_field

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class ants_ConvertScalarImageToRGB:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dimension='', input_image="path", colormap="enumerate(('grey','red','green','blue','copper','jet','hsv','spring','summer','autumn','winter','hot','cool','overunder','custom'))", minimum_input=0, maximum_input=0, **options):
        from nipype.interfaces.ants.visualization import ConvertScalarImageToRGB
        at = ConvertScalarImageToRGB()
        at.inputs.dimension = dimension
        at.inputs.input_image = input_image
        at.inputs.colormap = colormap
        at.inputs.minimum_input = minimum_input
        at.inputs.maximum_input = maximum_input
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

###############################################################################


class ants_CorticalThickness:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, anatomical_image="path", brain_template="path", brain_probability_mask="path", segmentation_priors=["path"], t1_registration_template="path", **options):
        from nipype.interfaces.ants.segmentation import CorticalThickness
        at = CorticalThickness()
        at.inputs.anatomical_image = anatomical_image
        at.inputs.brain_template = brain_template
        at.inputs.brain_probability_mask = brain_probability_mask
        at.inputs.segmentation_priors = segmentation_priors
        at.inputs.t1_registration_template = t1_registration_template
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def BrainExtractionMask(self) -> None:
        return self.res.outputs.BrainExtractionMask

    def ExtractedBrainN4(self) -> None:
        return self.res.outputs.ExtractedBrainN4

    def BrainSegmentation(self) -> None:
        return self.res.outputs.BrainSegmentation

    def BrainSegmentationN4(self) -> None:
        return self.res.outputs.BrainSegmentationN4

    def BrainSegmentationPosteriors(self) -> list[None]:
        return self.res.outputs.BrainSegmentationPosteriors

    def CorticalThickness(self) -> None:
        return self.res.outputs.CorticalThickness

    def TemplateToSubject1GenericAffine(self) -> None:
        return self.res.outputs.TemplateToSubject1GenericAffine

    def TemplateToSubject0Warp(self) -> None:
        return self.res.outputs.TemplateToSubject0Warp

    def SubjectToTemplate1Warp(self) -> None:
        return self.res.outputs.SubjectToTemplate1Warp

    def SubjectToTemplate0GenericAffine(self) -> None:
        return self.res.outputs.SubjectToTemplate0GenericAffine

    def SubjectToTemplateLogJacobian(self) -> None:
        return self.res.outputs.SubjectToTemplateLogJacobian

    def CorticalThicknessNormedToTemplate(self) -> None:
        return self.res.outputs.CorticalThicknessNormedToTemplate

    def BrainVolumes(self) -> None:
        return self.res.outputs.BrainVolumes

###############################################################################


class ants_CreateJacobianDeterminantImage:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, imageDimension='', deformationField="path", outputImage="path", **options):
        from nipype.interfaces.ants.utils import CreateJacobianDeterminantImage
        at = CreateJacobianDeterminantImage()
        at.inputs.imageDimension = imageDimension
        at.inputs.deformationField = deformationField
        at.inputs.outputImage = outputImage
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def jacobian_image(self) -> None:
        return self.res.outputs.jacobian_image

###############################################################################


class ants_CreateTiledMosaic:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_image="path", rgb_image="path", **options):
        from nipype.interfaces.ants.visualization import CreateTiledMosaic
        at = CreateTiledMosaic()
        at.inputs.input_image = input_image
        at.inputs.rgb_image = rgb_image
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

###############################################################################


class ants_DenoiseImage:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_image="path", **options):
        from nipype.interfaces.ants.segmentation import DenoiseImage
        at = DenoiseImage()
        at.inputs.input_image = input_image
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

    def noise_image(self) -> None:
        return self.res.outputs.noise_image

###############################################################################


class ants_ImageMath:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, operation="enumerate(('m','vm','+','v+','-','v-','/','^','max','exp','addtozero','overadd','abs','total','mean','vtotal','Decision','Neg','Project','G','MD','ME','MO','MC','GD','GE','GO','GC','ExtractContours','Translate','4DTensorTo3DTensor','ExtractVectorComponent','TensorColor','TensorFA','TensorFADenominator','TensorFANumerator','TensorMeanDiffusion','TensorRadialDiffusion','TensorAxialDiffusion','TensorEigenvalue','TensorToVector','TensorToVectorComponent','TensorMask','Byte','CorruptImage','D','MaurerDistance','ExtractSlice','FillHoles','Convolve','Finite','FlattenImage','GetLargestComponent','Grad','RescaleImage','WindowImage','NeighborhoodStats','ReplicateDisplacement','ReplicateImage','LabelStats','Laplacian','Canny','Lipschitz','MTR','Normalize','PadImage','SigmoidImage','Sharpen','UnsharpMask','PValueImage','ReplaceVoxelValue','SetTimeSpacing','SetTimeSpacingWarp','stack','ThresholdAtMean','TriPlanarView','TruncateImageIntensity'))", op1="path", **options):
        from nipype.interfaces.ants.utils import ImageMath
        at = ImageMath()
        at.inputs.operation = operation
        at.inputs.op1 = op1
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

###############################################################################


class ants_JointFusion:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, target_image=[["path"]], atlas_image=[["path"]], atlas_segmentation_image=["path"], **options):
        from nipype.interfaces.ants.segmentation import JointFusion
        at = JointFusion()
        at.inputs.target_image = target_image
        at.inputs.atlas_image = atlas_image
        at.inputs.atlas_segmentation_image = atlas_segmentation_image
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_label_fusion(self) -> None:
        return self.res.outputs.out_label_fusion

    def out_intensity_fusion(self) -> list[None]:
        return self.res.outputs.out_intensity_fusion

    def out_label_post_prob(self) -> list[None]:
        return self.res.outputs.out_label_post_prob

    def out_atlas_voting_weight(self) -> list[None]:
        return self.res.outputs.out_atlas_voting_weight

###############################################################################


class ants_LabelGeometry:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, label_image="path", intensity_image="path", **options):
        from nipype.interfaces.ants.utils import LabelGeometry
        at = LabelGeometry()
        at.inputs.label_image = label_image
        at.inputs.intensity_image = intensity_image
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class ants_LaplacianThickness:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_wm="path", input_gm="path", **options):
        from nipype.interfaces.ants.segmentation import LaplacianThickness
        at = LaplacianThickness()
        at.inputs.input_wm = input_wm
        at.inputs.input_gm = input_gm
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

###############################################################################


class ants_MeasureImageSimilarity:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, fixed_image="path", moving_image="path", metric="enumerate(('CC','MI','Mattes','MeanSquares','Demons','GC'))", radius_or_number_of_bins=0, sampling_percentage=0.0, **options):
        from nipype.interfaces.ants.registration import MeasureImageSimilarity
        at = MeasureImageSimilarity()
        at.inputs.fixed_image = fixed_image
        at.inputs.moving_image = moving_image
        at.inputs.metric = metric
        at.inputs.radius_or_number_of_bins = radius_or_number_of_bins
        at.inputs.sampling_percentage = sampling_percentage
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def similarity(self) -> float:
        return self.res.outputs.similarity

###############################################################################


class ants_MultiplyImages:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dimension='', first_input="path", second_input="path", output_product_image="path", **options):
        from nipype.interfaces.ants.utils import MultiplyImages
        at = MultiplyImages()
        at.inputs.dimension = dimension
        at.inputs.first_input = first_input
        at.inputs.second_input = second_input
        at.inputs.output_product_image = output_product_image
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_product_image(self) -> None:
        return self.res.outputs.output_product_image

###############################################################################


class ants_N4BiasFieldCorrection:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_image="path", copy_header=True, **options):
        from nipype.interfaces.ants.segmentation import N4BiasFieldCorrection
        at = N4BiasFieldCorrection()
        at.inputs.input_image = input_image
        at.inputs.copy_header = copy_header
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

    def bias_image(self) -> None:
        return self.res.outputs.bias_image

###############################################################################


class ants_Registration:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, fixed_image=["path"], moving_image=["path"], metric="enumerate(('CC','MeanSquares','Demons','GC','MI','Mattes'))", metric_weight=[0.0], transforms="enumerate(('Rigid','Affine','CompositeAffine','Similarity','Translation','BSpline','GaussianDisplacementField','TimeVaryingVelocityField','TimeVaryingBSplineVelocityField','SyN','BSplineSyN','Exponential','BSplineExponential'))", smoothing_sigmas=[[0.0]], shrink_factors=[[0]], **options):
        from nipype.interfaces.ants.registration import Registration
        at = Registration()
        at.inputs.fixed_image = fixed_image
        at.inputs.moving_image = moving_image
        at.inputs.metric = metric
        at.inputs.metric_weight = metric_weight
        at.inputs.transforms = transforms
        at.inputs.smoothing_sigmas = smoothing_sigmas
        at.inputs.shrink_factors = shrink_factors
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def forward_transforms(self) -> list[None]:
        return self.res.outputs.forward_transforms

    def reverse_forward_transforms(self) -> list[None]:
        return self.res.outputs.reverse_forward_transforms

    def reverse_transforms(self) -> list[None]:
        return self.res.outputs.reverse_transforms

    def forward_invert_flags(self) -> list[bool]:
        return self.res.outputs.forward_invert_flags

    def reverse_forward_invert_flags(self) -> list[bool]:
        return self.res.outputs.reverse_forward_invert_flags

    def reverse_invert_flags(self) -> list[bool]:
        return self.res.outputs.reverse_invert_flags

    def composite_transform(self) -> None:
        return self.res.outputs.composite_transform

    def inverse_composite_transform(self) -> None:
        return self.res.outputs.inverse_composite_transform

    def warped_image(self) -> None:
        return self.res.outputs.warped_image

    def inverse_warped_image(self) -> None:
        return self.res.outputs.inverse_warped_image

    def save_state(self) -> None:
        return self.res.outputs.save_state

    def metric_value(self) -> float:
        return self.res.outputs.metric_value

    def elapsed_time(self) -> float:
        return self.res.outputs.elapsed_time

###############################################################################


class ants_RegistrationSynQuick:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, fixed_image=["path"], moving_image=["path"], **options):
        from nipype.interfaces.ants.registration import RegistrationSynQuick
        at = RegistrationSynQuick()
        at.inputs.fixed_image = fixed_image
        at.inputs.moving_image = moving_image
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def warped_image(self) -> None:
        return self.res.outputs.warped_image

    def inverse_warped_image(self) -> None:
        return self.res.outputs.inverse_warped_image

    def out_matrix(self) -> None:
        return self.res.outputs.out_matrix

    def forward_warp_field(self) -> None:
        return self.res.outputs.forward_warp_field

    def inverse_warp_field(self) -> None:
        return self.res.outputs.inverse_warp_field

###############################################################################


class ants_ResampleImageBySpacing:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_image="path", out_spacing=(0,), **options):
        from nipype.interfaces.ants.utils import ResampleImageBySpacing
        at = ResampleImageBySpacing()
        at.inputs.input_image = input_image
        at.inputs.out_spacing = out_spacing
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

###############################################################################


class ants_ThresholdImage:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_image="path", copy_header=True, **options):
        from nipype.interfaces.ants.utils import ThresholdImage
        at = ThresholdImage()
        at.inputs.input_image = input_image
        at.inputs.copy_header = copy_header
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

###############################################################################


class ants_WarpImageMultiTransform:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_image="path", transformation_series=["path"], **options):
        from nipype.interfaces.ants.resampling import WarpImageMultiTransform
        at = WarpImageMultiTransform()
        at.inputs.input_image = input_image
        at.inputs.transformation_series = transformation_series
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

###############################################################################


class ants_WarpTimeSeriesImageMultiTransform:
    """
    Note:
        dependencies: Nipype,ants
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, input_image="path", transformation_series=["path"], **options):
        from nipype.interfaces.ants.resampling import WarpTimeSeriesImageMultiTransform
        at = WarpTimeSeriesImageMultiTransform()
        at.inputs.input_image = input_image
        at.inputs.transformation_series = transformation_series
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

###############################################################################


