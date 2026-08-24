class slicer_ACPCTransform:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.registration.specialized import ACPCTransform
        at = ACPCTransform()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputTransform(self) -> None:
        return self.res.outputs.outputTransform

###############################################################################


class slicer_AddScalarVolumes:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.arithmetic import AddScalarVolumes
        at = AddScalarVolumes()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_AffineRegistration:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.legacy.registration import AffineRegistration
        at = AffineRegistration()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputtransform(self) -> None:
        return self.res.outputs.outputtransform

    def resampledmovingfilename(self) -> None:
        return self.res.outputs.resampledmovingfilename

###############################################################################


class slicer_BRAINSDemonWarp:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.registration.specialized import BRAINSDemonWarp
        at = BRAINSDemonWarp()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

    def outputDisplacementFieldVolume(self) -> None:
        return self.res.outputs.outputDisplacementFieldVolume

    def outputCheckerboardVolume(self) -> None:
        return self.res.outputs.outputCheckerboardVolume

###############################################################################


class slicer_BRAINSFit:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.registration.brainsfit import BRAINSFit
        at = BRAINSFit()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def bsplineTransform(self) -> None:
        return self.res.outputs.bsplineTransform

    def linearTransform(self) -> None:
        return self.res.outputs.linearTransform

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

    def outputFixedVolumeROI(self) -> None:
        return self.res.outputs.outputFixedVolumeROI

    def outputMovingVolumeROI(self) -> None:
        return self.res.outputs.outputMovingVolumeROI

    def strippedOutputTransform(self) -> None:
        return self.res.outputs.strippedOutputTransform

    def outputTransform(self) -> None:
        return self.res.outputs.outputTransform

###############################################################################


class slicer_BRAINSROIAuto:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.segmentation.specialized import BRAINSROIAuto
        at = BRAINSROIAuto()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputROIMaskVolume(self) -> None:
        return self.res.outputs.outputROIMaskVolume

    def outputClippedVolumeROI(self) -> None:
        return self.res.outputs.outputClippedVolumeROI

###############################################################################


class slicer_BRAINSResample:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.registration.brainsresample import BRAINSResample
        at = BRAINSResample()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_BSplineDeformableRegistration:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.legacy.registration import BSplineDeformableRegistration
        at = BSplineDeformableRegistration()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputtransform(self) -> None:
        return self.res.outputs.outputtransform

    def outputwarp(self) -> None:
        return self.res.outputs.outputwarp

    def resampledmovingfilename(self) -> None:
        return self.res.outputs.resampledmovingfilename

###############################################################################


class slicer_BSplineToDeformationField:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.legacy.converters import BSplineToDeformationField
        at = BSplineToDeformationField()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def defImage(self) -> None:
        return self.res.outputs.defImage

###############################################################################


class slicer_CastScalarVolume:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.arithmetic import CastScalarVolume
        at = CastScalarVolume()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def OutputVolume(self) -> None:
        return self.res.outputs.OutputVolume

###############################################################################


class slicer_CheckerBoardFilter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.checkerboardfilter import CheckerBoardFilter
        at = CheckerBoardFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_CurvatureAnisotropicDiffusion:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.denoising import CurvatureAnisotropicDiffusion
        at = CurvatureAnisotropicDiffusion()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_DTIexport:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.diffusion.diffusion import DTIexport
        at = DTIexport()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputFile(self) -> None:
        return self.res.outputs.outputFile

###############################################################################


class slicer_DTIimport:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.diffusion.diffusion import DTIimport
        at = DTIimport()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputTensor(self) -> None:
        return self.res.outputs.outputTensor

###############################################################################


class slicer_DWIJointRicianLMMSEFilter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.diffusion.diffusion import DWIJointRicianLMMSEFilter
        at = DWIJointRicianLMMSEFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_DWIRicianLMMSEFilter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.diffusion.diffusion import DWIRicianLMMSEFilter
        at = DWIRicianLMMSEFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_DWIToDTIEstimation:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.diffusion.diffusion import DWIToDTIEstimation
        at = DWIToDTIEstimation()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputTensor(self) -> None:
        return self.res.outputs.outputTensor

    def outputBaseline(self) -> None:
        return self.res.outputs.outputBaseline

###############################################################################


class slicer_DWIUnbiasedNonLocalMeansFilter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.legacy.diffusion.denoising import DWIUnbiasedNonLocalMeansFilter
        at = DWIUnbiasedNonLocalMeansFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_DicomToNrrdConverter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.converters import DicomToNrrdConverter
        at = DicomToNrrdConverter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputDirectory(self) -> None:
        return self.res.outputs.outputDirectory

###############################################################################


class slicer_DiffusionTensorScalarMeasurements:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.diffusion.diffusion import DiffusionTensorScalarMeasurements
        at = DiffusionTensorScalarMeasurements()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputScalar(self) -> None:
        return self.res.outputs.outputScalar

###############################################################################


class slicer_DiffusionWeightedVolumeMasking:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.diffusion.diffusion import DiffusionWeightedVolumeMasking
        at = DiffusionWeightedVolumeMasking()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputBaseline(self) -> None:
        return self.res.outputs.outputBaseline

    def thresholdMask(self) -> None:
        return self.res.outputs.thresholdMask

###############################################################################


class slicer_EMSegmentCommandLine:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.segmentation.specialized import EMSegmentCommandLine
        at = EMSegmentCommandLine()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def resultVolumeFileName(self) -> None:
        return self.res.outputs.resultVolumeFileName

    def generateEmptyMRMLSceneAndQuit(self) -> None:
        return self.res.outputs.generateEmptyMRMLSceneAndQuit

    def resultMRMLSceneFileName(self) -> None:
        return self.res.outputs.resultMRMLSceneFileName

###############################################################################


class slicer_EMSegmentTransformToNewFormat:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.utilities import EMSegmentTransformToNewFormat
        at = EMSegmentTransformToNewFormat()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputMRMLFileName(self) -> None:
        return self.res.outputs.outputMRMLFileName

###############################################################################


class slicer_ExpertAutomatedRegistration:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.legacy.registration import ExpertAutomatedRegistration
        at = ExpertAutomatedRegistration()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def resampledImage(self) -> None:
        return self.res.outputs.resampledImage

    def saveTransform(self) -> None:
        return self.res.outputs.saveTransform

###############################################################################


class slicer_ExtractSkeleton:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.extractskeleton import ExtractSkeleton
        at = ExtractSkeleton()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def OutputImageFileName(self) -> None:
        return self.res.outputs.OutputImageFileName

###############################################################################


class slicer_FiducialRegistration:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.registration.specialized import FiducialRegistration
        at = FiducialRegistration()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def saveTransform(self) -> None:
        return self.res.outputs.saveTransform

###############################################################################


class slicer_GaussianBlurImageFilter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.denoising import GaussianBlurImageFilter
        at = GaussianBlurImageFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_GradientAnisotropicDiffusion:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.denoising import GradientAnisotropicDiffusion
        at = GradientAnisotropicDiffusion()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_GrayscaleFillHoleImageFilter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.morphology import GrayscaleFillHoleImageFilter
        at = GrayscaleFillHoleImageFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_GrayscaleGrindPeakImageFilter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.morphology import GrayscaleGrindPeakImageFilter
        at = GrayscaleGrindPeakImageFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_GrayscaleModelMaker:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.surface import GrayscaleModelMaker
        at = GrayscaleModelMaker()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def OutputGeometry(self) -> None:
        return self.res.outputs.OutputGeometry

###############################################################################


class slicer_HistogramMatching:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.histogrammatching import HistogramMatching
        at = HistogramMatching()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_ImageLabelCombine:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.imagelabelcombine import ImageLabelCombine
        at = ImageLabelCombine()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def OutputLabelMap(self) -> None:
        return self.res.outputs.OutputLabelMap

###############################################################################


class slicer_IntensityDifferenceMetric:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.quantification.changequantification import IntensityDifferenceMetric
        at = IntensityDifferenceMetric()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

    def reportFileName(self) -> None:
        return self.res.outputs.reportFileName

###############################################################################


class slicer_LabelMapSmoothing:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.surface import LabelMapSmoothing
        at = LabelMapSmoothing()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_LinearRegistration:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.legacy.registration import LinearRegistration
        at = LinearRegistration()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputtransform(self) -> None:
        return self.res.outputs.outputtransform

    def resampledmovingfilename(self) -> None:
        return self.res.outputs.resampledmovingfilename

###############################################################################


class slicer_MaskScalarVolume:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.arithmetic import MaskScalarVolume
        at = MaskScalarVolume()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def OutputVolume(self) -> None:
        return self.res.outputs.OutputVolume

###############################################################################


class slicer_MedianImageFilter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.denoising import MedianImageFilter
        at = MedianImageFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_MergeModels:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.surface import MergeModels
        at = MergeModels()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def ModelOutput(self) -> None:
        return self.res.outputs.ModelOutput

###############################################################################


class slicer_ModelMaker:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.surface import ModelMaker
        at = ModelMaker()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def modelSceneFile(self) -> list[None]:
        return self.res.outputs.modelSceneFile

###############################################################################


class slicer_ModelToLabelMap:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.surface import ModelToLabelMap
        at = ModelToLabelMap()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def OutputVolume(self) -> None:
        return self.res.outputs.OutputVolume

###############################################################################


class slicer_MultiResolutionAffineRegistration:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.legacy.registration import MultiResolutionAffineRegistration
        at = MultiResolutionAffineRegistration()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def resampledImage(self) -> None:
        return self.res.outputs.resampledImage

    def saveTransform(self) -> None:
        return self.res.outputs.saveTransform

###############################################################################


class slicer_MultiplyScalarVolumes:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.arithmetic import MultiplyScalarVolumes
        at = MultiplyScalarVolumes()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_N4ITKBiasFieldCorrection:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.n4itkbiasfieldcorrection import N4ITKBiasFieldCorrection
        at = N4ITKBiasFieldCorrection()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputimage(self) -> None:
        return self.res.outputs.outputimage

    def outputbiasfield(self) -> None:
        return self.res.outputs.outputbiasfield

###############################################################################


class slicer_OrientScalarVolume:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.converters import OrientScalarVolume
        at = OrientScalarVolume()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_OtsuThresholdImageFilter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.legacy.filtering import OtsuThresholdImageFilter
        at = OtsuThresholdImageFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_OtsuThresholdSegmentation:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.legacy.segmentation import OtsuThresholdSegmentation
        at = OtsuThresholdSegmentation()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_PETStandardUptakeValueComputation:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.quantification.petstandarduptakevaluecomputation import PETStandardUptakeValueComputation
        at = PETStandardUptakeValueComputation()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def csvFile(self) -> None:
        return self.res.outputs.csvFile

###############################################################################


class slicer_ProbeVolumeWithModel:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.surface import ProbeVolumeWithModel
        at = ProbeVolumeWithModel()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def OutputModel(self) -> None:
        return self.res.outputs.OutputModel

###############################################################################


class slicer_ResampleDTIVolume:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.diffusion.diffusion import ResampleDTIVolume
        at = ResampleDTIVolume()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_ResampleScalarVectorDWIVolume:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.resamplescalarvectordwivolume import ResampleScalarVectorDWIVolume
        at = ResampleScalarVectorDWIVolume()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_ResampleScalarVolume:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.legacy.filtering import ResampleScalarVolume
        at = ResampleScalarVolume()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def OutputVolume(self) -> None:
        return self.res.outputs.OutputVolume

###############################################################################


class slicer_RigidRegistration:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.legacy.registration import RigidRegistration
        at = RigidRegistration()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputtransform(self) -> None:
        return self.res.outputs.outputtransform

    def resampledmovingfilename(self) -> None:
        return self.res.outputs.resampledmovingfilename

###############################################################################


class slicer_RobustStatisticsSegmenter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.segmentation.specialized import RobustStatisticsSegmenter
        at = RobustStatisticsSegmenter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def segmentedImageFileName(self) -> None:
        return self.res.outputs.segmentedImageFileName

###############################################################################


class slicer_SimpleRegionGrowingSegmentation:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.segmentation.simpleregiongrowingsegmentation import SimpleRegionGrowingSegmentation
        at = SimpleRegionGrowingSegmentation()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_SubtractScalarVolumes:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.arithmetic import SubtractScalarVolumes
        at = SubtractScalarVolumes()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class slicer_ThresholdScalarVolume:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.thresholdscalarvolume import ThresholdScalarVolume
        at = ThresholdScalarVolume()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def OutputVolume(self) -> None:
        return self.res.outputs.OutputVolume

###############################################################################


class slicer_TractographyLabelMapSeeding:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.diffusion.diffusion import TractographyLabelMapSeeding
        at = TractographyLabelMapSeeding()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def OutputFibers(self) -> None:
        return self.res.outputs.OutputFibers

    def outputdirectory(self) -> None:
        return self.res.outputs.outputdirectory

###############################################################################


class slicer_VBRAINSDemonWarp:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.registration.specialized import VBRAINSDemonWarp
        at = VBRAINSDemonWarp()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

    def outputDisplacementFieldVolume(self) -> None:
        return self.res.outputs.outputDisplacementFieldVolume

    def outputCheckerboardVolume(self) -> None:
        return self.res.outputs.outputCheckerboardVolume

###############################################################################


class slicer_VotingBinaryHoleFillingImageFilter:
    """
    Note:
        dependencies: Nipype,slicer
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.slicer.filtering.votingbinaryholefillingimagefilter import VotingBinaryHoleFillingImageFilter
        at = VotingBinaryHoleFillingImageFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


