class brainsuite_BDP:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputDiffusionData="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import BDP
        at = BDP()
        at.inputs.inputDiffusionData = inputDiffusionData
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class brainsuite_Bfc:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputMRIFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Bfc
        at = Bfc()
        at.inputs.inputMRIFile = inputMRIFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputMRIVolume(self) -> None:
        return self.res.outputs.outputMRIVolume

    def outputBiasField(self) -> None:
        return self.res.outputs.outputBiasField

    def outputMaskedBiasField(self) -> None:
        return self.res.outputs.outputMaskedBiasField

    def correctionScheduleFile(self) -> None:
        return self.res.outputs.correctionScheduleFile

###############################################################################


class brainsuite_Bse:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputMRIFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Bse
        at = Bse()
        at.inputs.inputMRIFile = inputMRIFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputMRIVolume(self) -> None:
        return self.res.outputs.outputMRIVolume

    def outputMaskFile(self) -> None:
        return self.res.outputs.outputMaskFile

    def outputDiffusionFilter(self) -> None:
        return self.res.outputs.outputDiffusionFilter

    def outputEdgeMap(self) -> None:
        return self.res.outputs.outputEdgeMap

    def outputDetailedBrainMask(self) -> None:
        return self.res.outputs.outputDetailedBrainMask

    def outputCortexFile(self) -> None:
        return self.res.outputs.outputCortexFile

###############################################################################


class brainsuite_Cerebro:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputMRIFile="path", inputAtlasMRIFile="path", inputAtlasLabelFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Cerebro
        at = Cerebro()
        at.inputs.inputMRIFile = inputMRIFile
        at.inputs.inputAtlasMRIFile = inputAtlasMRIFile
        at.inputs.inputAtlasLabelFile = inputAtlasLabelFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputCerebrumMaskFile(self) -> None:
        return self.res.outputs.outputCerebrumMaskFile

    def outputLabelVolumeFile(self) -> None:
        return self.res.outputs.outputLabelVolumeFile

    def outputAffineTransformFile(self) -> None:
        return self.res.outputs.outputAffineTransformFile

    def outputWarpTransformFile(self) -> None:
        return self.res.outputs.outputWarpTransformFile

###############################################################################


class brainsuite_Cortex:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputHemisphereLabelFile="path", inputTissueFractionFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Cortex
        at = Cortex()
        at.inputs.inputHemisphereLabelFile = inputHemisphereLabelFile
        at.inputs.inputTissueFractionFile = inputTissueFractionFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputCerebrumMask(self) -> None:
        return self.res.outputs.outputCerebrumMask

###############################################################################


class brainsuite_Dewisp:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputMaskFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Dewisp
        at = Dewisp()
        at.inputs.inputMaskFile = inputMaskFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputMaskFile(self) -> None:
        return self.res.outputs.outputMaskFile

###############################################################################


class brainsuite_Dfs:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputVolumeFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Dfs
        at = Dfs()
        at.inputs.inputVolumeFile = inputVolumeFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputSurfaceFile(self) -> None:
        return self.res.outputs.outputSurfaceFile

###############################################################################


class brainsuite_Hemisplit:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputSurfaceFile="path", inputHemisphereLabelFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Hemisplit
        at = Hemisplit()
        at.inputs.inputSurfaceFile = inputSurfaceFile
        at.inputs.inputHemisphereLabelFile = inputHemisphereLabelFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputLeftHemisphere(self) -> None:
        return self.res.outputs.outputLeftHemisphere

    def outputRightHemisphere(self) -> None:
        return self.res.outputs.outputRightHemisphere

    def outputLeftPialHemisphere(self) -> None:
        return self.res.outputs.outputLeftPialHemisphere

    def outputRightPialHemisphere(self) -> None:
        return self.res.outputs.outputRightPialHemisphere

###############################################################################


class brainsuite_Pialmesh:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputSurfaceFile="path", inputTissueFractionFile="path", inputMaskFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Pialmesh
        at = Pialmesh()
        at.inputs.inputSurfaceFile = inputSurfaceFile
        at.inputs.inputTissueFractionFile = inputTissueFractionFile
        at.inputs.inputMaskFile = inputMaskFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputSurfaceFile(self) -> None:
        return self.res.outputs.outputSurfaceFile

###############################################################################


class brainsuite_Pvc:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputMRIFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Pvc
        at = Pvc()
        at.inputs.inputMRIFile = inputMRIFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputLabelFile(self) -> None:
        return self.res.outputs.outputLabelFile

    def outputTissueFractionFile(self) -> None:
        return self.res.outputs.outputTissueFractionFile

###############################################################################


class brainsuite_SVReg:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subjectFilePrefix='', **options):
        from nipype.interfaces.brainsuite.brainsuite import SVReg
        at = SVReg()
        at.inputs.subjectFilePrefix = subjectFilePrefix
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class brainsuite_Scrubmask:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputMaskFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Scrubmask
        at = Scrubmask()
        at.inputs.inputMaskFile = inputMaskFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputMaskFile(self) -> None:
        return self.res.outputs.outputMaskFile

###############################################################################


class brainsuite_Skullfinder:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputMRIFile="path", inputMaskFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Skullfinder
        at = Skullfinder()
        at.inputs.inputMRIFile = inputMRIFile
        at.inputs.inputMaskFile = inputMaskFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputLabelFile(self) -> None:
        return self.res.outputs.outputLabelFile

###############################################################################


class brainsuite_Tca:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inputMaskFile="path", **options):
        from nipype.interfaces.brainsuite.brainsuite import Tca
        at = Tca()
        at.inputs.inputMaskFile = inputMaskFile
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outputMaskFile(self) -> None:
        return self.res.outputs.outputMaskFile

###############################################################################


class brainsuite_ThicknessPVC:
    """
    Note:
        dependencies: Nipype,brainsuite
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subjectFilePrefix='', **options):
        from nipype.interfaces.brainsuite.brainsuite import ThicknessPVC
        at = ThicknessPVC()
        at.inputs.subjectFilePrefix = subjectFilePrefix
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


