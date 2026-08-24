class semtools_BRAINSABC:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.segmentation.specialized import BRAINSABC
        at = BRAINSABC()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def saveState(self) -> None:
        return self.res.outputs.saveState

    def outputDir(self) -> None:
        return self.res.outputs.outputDir

    def atlasToSubjectTransform(self) -> None:
        return self.res.outputs.atlasToSubjectTransform

    def atlasToSubjectInitialTransform(self) -> None:
        return self.res.outputs.atlasToSubjectInitialTransform

    def outputVolumes(self) -> list[None]:
        return self.res.outputs.outputVolumes

    def outputLabels(self) -> None:
        return self.res.outputs.outputLabels

    def outputDirtyLabels(self) -> None:
        return self.res.outputs.outputDirtyLabels

    def implicitOutputs(self) -> list[None]:
        return self.res.outputs.implicitOutputs

###############################################################################


class semtools_BRAINSAlignMSP:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSAlignMSP
        at = BRAINSAlignMSP()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def OutputresampleMSP(self) -> None:
        return self.res.outputs.OutputresampleMSP

    def resultsDir(self) -> None:
        return self.res.outputs.resultsDir

###############################################################################


class semtools_BRAINSClipInferior:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSClipInferior
        at = BRAINSClipInferior()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_BRAINSConstellationDetector:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.segmentation.specialized import BRAINSConstellationDetector
        at = BRAINSConstellationDetector()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

    def outputResampledVolume(self) -> None:
        return self.res.outputs.outputResampledVolume

    def outputTransform(self) -> None:
        return self.res.outputs.outputTransform

    def outputLandmarksInInputSpace(self) -> None:
        return self.res.outputs.outputLandmarksInInputSpace

    def outputLandmarksInACPCAlignedSpace(self) -> None:
        return self.res.outputs.outputLandmarksInACPCAlignedSpace

    def outputMRML(self) -> None:
        return self.res.outputs.outputMRML

    def outputVerificationScript(self) -> None:
        return self.res.outputs.outputVerificationScript

    def outputUntransformedClippedVolume(self) -> None:
        return self.res.outputs.outputUntransformedClippedVolume

    def writeBranded2DImage(self) -> None:
        return self.res.outputs.writeBranded2DImage

    def resultsDir(self) -> None:
        return self.res.outputs.resultsDir

###############################################################################


class semtools_BRAINSConstellationModeler:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSConstellationModeler
        at = BRAINSConstellationModeler()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputModel(self) -> None:
        return self.res.outputs.outputModel

    def resultsDir(self) -> None:
        return self.res.outputs.resultsDir

###############################################################################


class semtools_BRAINSCreateLabelMapFromProbabilityMaps:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.segmentation.specialized import BRAINSCreateLabelMapFromProbabilityMaps
        at = BRAINSCreateLabelMapFromProbabilityMaps()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def dirtyLabelVolume(self) -> None:
        return self.res.outputs.dirtyLabelVolume

    def cleanLabelVolume(self) -> None:
        return self.res.outputs.cleanLabelVolume

###############################################################################


class semtools_BRAINSCut:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.segmentation.specialized import BRAINSCut
        at = BRAINSCut()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_BRAINSDemonWarp:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.registration.specialized import BRAINSDemonWarp
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


class semtools_BRAINSEyeDetector:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSEyeDetector
        at = BRAINSEyeDetector()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_BRAINSFit:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.registration.brainsfit import BRAINSFit
        at = BRAINSFit()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def linearTransform(self) -> None:
        return self.res.outputs.linearTransform

    def bsplineTransform(self) -> None:
        return self.res.outputs.bsplineTransform

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

    def logFileReport(self) -> None:
        return self.res.outputs.logFileReport

###############################################################################


class semtools_BRAINSInitializedControlPoints:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSInitializedControlPoints
        at = BRAINSInitializedControlPoints()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_BRAINSLandmarkInitializer:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSLandmarkInitializer
        at = BRAINSLandmarkInitializer()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputTransformFilename(self) -> None:
        return self.res.outputs.outputTransformFilename

###############################################################################


class semtools_BRAINSLinearModelerEPCA:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSLinearModelerEPCA
        at = BRAINSLinearModelerEPCA()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_BRAINSLmkTransform:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSLmkTransform
        at = BRAINSLmkTransform()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputAffineTransform(self) -> None:
        return self.res.outputs.outputAffineTransform

    def outputResampledVolume(self) -> None:
        return self.res.outputs.outputResampledVolume

###############################################################################


class semtools_BRAINSMultiSTAPLE:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.segmentation.specialized import BRAINSMultiSTAPLE
        at = BRAINSMultiSTAPLE()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputMultiSTAPLE(self) -> None:
        return self.res.outputs.outputMultiSTAPLE

    def outputConfusionMatrix(self) -> None:
        return self.res.outputs.outputConfusionMatrix

###############################################################################


class semtools_BRAINSMush:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSMush
        at = BRAINSMush()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputWeightsFile(self) -> None:
        return self.res.outputs.outputWeightsFile

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

    def outputMask(self) -> None:
        return self.res.outputs.outputMask

###############################################################################


class semtools_BRAINSPosteriorToContinuousClass:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.brains.classify import BRAINSPosteriorToContinuousClass
        at = BRAINSPosteriorToContinuousClass()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_BRAINSROIAuto:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.segmentation.specialized import BRAINSROIAuto
        at = BRAINSROIAuto()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputROIMaskVolume(self) -> None:
        return self.res.outputs.outputROIMaskVolume

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_BRAINSResample:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.registration.brainsresample import BRAINSResample
        at = BRAINSResample()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_BRAINSResize:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.registration.brainsresize import BRAINSResize
        at = BRAINSResize()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_BRAINSSnapShotWriter:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSSnapShotWriter
        at = BRAINSSnapShotWriter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputFilename(self) -> None:
        return self.res.outputs.outputFilename

###############################################################################


class semtools_BRAINSTalairach:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.brains.segmentation import BRAINSTalairach
        at = BRAINSTalairach()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputBox(self) -> None:
        return self.res.outputs.outputBox

    def outputGrid(self) -> None:
        return self.res.outputs.outputGrid

###############################################################################


class semtools_BRAINSTalairachMask:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.brains.segmentation import BRAINSTalairachMask
        at = BRAINSTalairachMask()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_BRAINSTransformConvert:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSTransformConvert
        at = BRAINSTransformConvert()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def displacementVolume(self) -> None:
        return self.res.outputs.displacementVolume

    def outputTransform(self) -> None:
        return self.res.outputs.outputTransform

###############################################################################


class semtools_BRAINSTransformFromFiducials:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.registration.specialized import BRAINSTransformFromFiducials
        at = BRAINSTransformFromFiducials()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def saveTransform(self) -> None:
        return self.res.outputs.saveTransform

###############################################################################


class semtools_BRAINSTrimForegroundInDirection:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import BRAINSTrimForegroundInDirection
        at = BRAINSTrimForegroundInDirection()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_BinaryMaskEditorBasedOnLandmarks:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.segmentation.specialized import BinaryMaskEditorBasedOnLandmarks
        at = BinaryMaskEditorBasedOnLandmarks()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputBinaryVolume(self) -> None:
        return self.res.outputs.outputBinaryVolume

###############################################################################


class semtools_CannyEdge:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import CannyEdge
        at = CannyEdge()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_CannySegmentationLevelSetImageFilter:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import CannySegmentationLevelSetImageFilter
        at = CannySegmentationLevelSetImageFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

    def outputSpeedVolume(self) -> None:
        return self.res.outputs.outputSpeedVolume

###############################################################################


class semtools_CleanUpOverlapLabels:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import CleanUpOverlapLabels
        at = CleanUpOverlapLabels()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputBinaryVolumes(self) -> list[None]:
        return self.res.outputs.outputBinaryVolumes

###############################################################################


class semtools_DWICompare:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.converters import DWICompare
        at = DWICompare()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_DWIConvert:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.diffusion import DWIConvert
        at = DWIConvert()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

    def outputBValues(self) -> None:
        return self.res.outputs.outputBValues

    def outputBVectors(self) -> None:
        return self.res.outputs.outputBVectors

    def outputDirectory(self) -> None:
        return self.res.outputs.outputDirectory

    def gradientVectorFile(self) -> None:
        return self.res.outputs.gradientVectorFile

###############################################################################


class semtools_DWISimpleCompare:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.converters import DWISimpleCompare
        at = DWISimpleCompare()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_DilateImage:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import DilateImage
        at = DilateImage()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_DilateMask:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import DilateMask
        at = DilateMask()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_DistanceMaps:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import DistanceMaps
        at = DistanceMaps()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_DumpBinaryTrainingVectors:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import DumpBinaryTrainingVectors
        at = DumpBinaryTrainingVectors()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_ESLR:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.segmentation.specialized import ESLR
        at = ESLR()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_ErodeImage:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import ErodeImage
        at = ErodeImage()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_FlippedDifference:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import FlippedDifference
        at = FlippedDifference()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_GenerateAverageLmkFile:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.testing.generateaveragelmkfile import GenerateAverageLmkFile
        at = GenerateAverageLmkFile()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputLandmarkFile(self) -> None:
        return self.res.outputs.outputLandmarkFile

###############################################################################


class semtools_GenerateBrainClippedImage:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import GenerateBrainClippedImage
        at = GenerateBrainClippedImage()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputFileName(self) -> None:
        return self.res.outputs.outputFileName

###############################################################################


class semtools_GenerateCsfClippedFromClassifiedImage:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.featurecreator import GenerateCsfClippedFromClassifiedImage
        at = GenerateCsfClippedFromClassifiedImage()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_GenerateEdgeMapImage:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.brains.utilities import GenerateEdgeMapImage
        at = GenerateEdgeMapImage()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputEdgeMap(self) -> None:
        return self.res.outputs.outputEdgeMap

    def outputMaximumGradientImage(self) -> None:
        return self.res.outputs.outputMaximumGradientImage

###############################################################################


class semtools_GenerateLabelMapFromProbabilityMap:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import GenerateLabelMapFromProbabilityMap
        at = GenerateLabelMapFromProbabilityMap()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputLabelVolume(self) -> None:
        return self.res.outputs.outputLabelVolume

###############################################################################


class semtools_GeneratePurePlugMask:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.brains.utilities import GeneratePurePlugMask
        at = GeneratePurePlugMask()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputMaskFile(self) -> None:
        return self.res.outputs.outputMaskFile

###############################################################################


class semtools_GenerateSummedGradientImage:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import GenerateSummedGradientImage
        at = GenerateSummedGradientImage()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputFileName(self) -> None:
        return self.res.outputs.outputFileName

###############################################################################


class semtools_GenerateTestImage:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import GenerateTestImage
        at = GenerateTestImage()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_GradientAnisotropicDiffusionImageFilter:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import GradientAnisotropicDiffusionImageFilter
        at = GradientAnisotropicDiffusionImageFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_HammerAttributeCreator:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import HammerAttributeCreator
        at = HammerAttributeCreator()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_HistogramMatchingFilter:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.brains.utilities import HistogramMatchingFilter
        at = HistogramMatchingFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_ImageRegionPlotter:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import ImageRegionPlotter
        at = ImageRegionPlotter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_JointHistogram:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import JointHistogram
        at = JointHistogram()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_LandmarksCompare:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.testing.landmarkscompare import LandmarksCompare
        at = LandmarksCompare()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_NeighborhoodMean:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import NeighborhoodMean
        at = NeighborhoodMean()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_NeighborhoodMedian:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import NeighborhoodMedian
        at = NeighborhoodMedian()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_STAPLEAnalysis:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import STAPLEAnalysis
        at = STAPLEAnalysis()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_ShuffleVectorsModule:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import ShuffleVectorsModule
        at = ShuffleVectorsModule()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVectorFileBaseName(self) -> None:
        return self.res.outputs.outputVectorFileBaseName

###############################################################################


class semtools_SimilarityIndex:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.brains.segmentation import SimilarityIndex
        at = SimilarityIndex()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_SphericalCoordinateGeneration:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.testing.featuredetection import SphericalCoordinateGeneration
        at = SphericalCoordinateGeneration()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_TextureFromNoiseImageFilter:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import TextureFromNoiseImageFilter
        at = TextureFromNoiseImageFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_TextureMeasureFilter:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.featuredetection import TextureMeasureFilter
        at = TextureMeasureFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputFilename(self) -> None:
        return self.res.outputs.outputFilename

###############################################################################


class semtools_UKFTractography:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.tractography.ukftractography import UKFTractography
        at = UKFTractography()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracts(self) -> None:
        return self.res.outputs.tracts

    def tractsWithSecondTensor(self) -> None:
        return self.res.outputs.tractsWithSecondTensor

###############################################################################


class semtools_UnbiasedNonLocalMeans:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.filtering.denoising import UnbiasedNonLocalMeans
        at = UnbiasedNonLocalMeans()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_VBRAINSDemonWarp:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.registration.specialized import VBRAINSDemonWarp
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


class semtools_compareTractInclusion:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import compareTractInclusion
        at = compareTractInclusion()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_dtiaverage:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.diffusion import dtiaverage
        at = dtiaverage()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tensor_output(self) -> None:
        return self.res.outputs.tensor_output

###############################################################################


class semtools_dtiestim:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.diffusion import dtiestim
        at = dtiestim()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tensor_output(self) -> None:
        return self.res.outputs.tensor_output

    def B0(self) -> None:
        return self.res.outputs.B0

    def idwi(self) -> None:
        return self.res.outputs.idwi

    def B0_mask_output(self) -> None:
        return self.res.outputs.B0_mask_output

###############################################################################


class semtools_dtiprocess:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.diffusion import dtiprocess
        at = dtiprocess()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def fa_output(self) -> None:
        return self.res.outputs.fa_output

    def md_output(self) -> None:
        return self.res.outputs.md_output

    def fa_gradient_output(self) -> None:
        return self.res.outputs.fa_gradient_output

    def fa_gradmag_output(self) -> None:
        return self.res.outputs.fa_gradmag_output

    def color_fa_output(self) -> None:
        return self.res.outputs.color_fa_output

    def principal_eigenvector_output(self) -> None:
        return self.res.outputs.principal_eigenvector_output

    def negative_eigenvector_output(self) -> None:
        return self.res.outputs.negative_eigenvector_output

    def frobenius_norm_output(self) -> None:
        return self.res.outputs.frobenius_norm_output

    def lambda1_output(self) -> None:
        return self.res.outputs.lambda1_output

    def lambda2_output(self) -> None:
        return self.res.outputs.lambda2_output

    def lambda3_output(self) -> None:
        return self.res.outputs.lambda3_output

    def RD_output(self) -> None:
        return self.res.outputs.RD_output

    def rot_output(self) -> None:
        return self.res.outputs.rot_output

    def outmask(self) -> None:
        return self.res.outputs.outmask

    def deformation_output(self) -> None:
        return self.res.outputs.deformation_output

###############################################################################


class semtools_extractNrrdVectorIndex:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import extractNrrdVectorIndex
        at = extractNrrdVectorIndex()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_fiberprocess:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.tractography.fiberprocess import fiberprocess
        at = fiberprocess()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def fiber_output(self) -> None:
        return self.res.outputs.fiber_output

    def voxelize(self) -> None:
        return self.res.outputs.voxelize

###############################################################################


class semtools_fiberstats:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.tractography.commandlineonly import fiberstats
        at = fiberstats()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class semtools_fibertrack:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.tractography.fibertrack import fibertrack
        at = fibertrack()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_fiber_file(self) -> None:
        return self.res.outputs.output_fiber_file

###############################################################################


class semtools_gtractAnisotropyMap:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractAnisotropyMap
        at = gtractAnisotropyMap()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractAverageBvalues:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractAverageBvalues
        at = gtractAverageBvalues()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractClipAnisotropy:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractClipAnisotropy
        at = gtractClipAnisotropy()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractCoRegAnatomy:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractCoRegAnatomy
        at = gtractCoRegAnatomy()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputTransformName(self) -> None:
        return self.res.outputs.outputTransformName

###############################################################################


class semtools_gtractConcatDwi:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractConcatDwi
        at = gtractConcatDwi()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractCopyImageOrientation:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractCopyImageOrientation
        at = gtractCopyImageOrientation()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractCoregBvalues:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractCoregBvalues
        at = gtractCoregBvalues()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

    def outputTransform(self) -> None:
        return self.res.outputs.outputTransform

###############################################################################


class semtools_gtractCostFastMarching:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractCostFastMarching
        at = gtractCostFastMarching()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputCostVolume(self) -> None:
        return self.res.outputs.outputCostVolume

    def outputSpeedVolume(self) -> None:
        return self.res.outputs.outputSpeedVolume

###############################################################################


class semtools_gtractCreateGuideFiber:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractCreateGuideFiber
        at = gtractCreateGuideFiber()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputFiber(self) -> None:
        return self.res.outputs.outputFiber

###############################################################################


class semtools_gtractFastMarchingTracking:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractFastMarchingTracking
        at = gtractFastMarchingTracking()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputTract(self) -> None:
        return self.res.outputs.outputTract

###############################################################################


class semtools_gtractFiberTracking:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractFiberTracking
        at = gtractFiberTracking()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputTract(self) -> None:
        return self.res.outputs.outputTract

###############################################################################


class semtools_gtractImageConformity:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractImageConformity
        at = gtractImageConformity()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractInvertBSplineTransform:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractInvertBSplineTransform
        at = gtractInvertBSplineTransform()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputTransform(self) -> None:
        return self.res.outputs.outputTransform

###############################################################################


class semtools_gtractInvertDisplacementField:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractInvertDisplacementField
        at = gtractInvertDisplacementField()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractInvertRigidTransform:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractInvertRigidTransform
        at = gtractInvertRigidTransform()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputTransform(self) -> None:
        return self.res.outputs.outputTransform

###############################################################################


class semtools_gtractResampleAnisotropy:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractResampleAnisotropy
        at = gtractResampleAnisotropy()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractResampleB0:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractResampleB0
        at = gtractResampleB0()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractResampleCodeImage:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractResampleCodeImage
        at = gtractResampleCodeImage()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractResampleDWIInPlace:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractResampleDWIInPlace
        at = gtractResampleDWIInPlace()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputResampledB0(self) -> None:
        return self.res.outputs.outputResampledB0

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractResampleFibers:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractResampleFibers
        at = gtractResampleFibers()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputTract(self) -> None:
        return self.res.outputs.outputTract

###############################################################################


class semtools_gtractTensor:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractTensor
        at = gtractTensor()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputVolume(self) -> None:
        return self.res.outputs.outputVolume

###############################################################################


class semtools_gtractTransformToDisplacementField:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.gtract import gtractTransformToDisplacementField
        at = gtractTransformToDisplacementField()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputDeformationFieldVolume(self) -> None:
        return self.res.outputs.outputDeformationFieldVolume

###############################################################################


class semtools_insertMidACPCpoint:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import insertMidACPCpoint
        at = insertMidACPCpoint()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputLandmarkFile(self) -> None:
        return self.res.outputs.outputLandmarkFile

###############################################################################


class semtools_landmarksConstellationAligner:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import landmarksConstellationAligner
        at = landmarksConstellationAligner()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputLandmarksPaired(self) -> None:
        return self.res.outputs.outputLandmarksPaired

###############################################################################


class semtools_landmarksConstellationWeights:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.utilities.brains import landmarksConstellationWeights
        at = landmarksConstellationWeights()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputWeightsList(self) -> None:
        return self.res.outputs.outputWeightsList

###############################################################################


class semtools_maxcurvature:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.diffusion.maxcurvature import maxcurvature
        at = maxcurvature()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output(self) -> None:
        return self.res.outputs.output

###############################################################################


class semtools_scalartransform:
    """
    Note:
        dependencies: Nipype,semtools
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.semtools.legacy.registration import scalartransform
        at = scalartransform()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_image(self) -> None:
        return self.res.outputs.output_image

    def transformation(self) -> None:
        return self.res.outputs.transformation

###############################################################################


