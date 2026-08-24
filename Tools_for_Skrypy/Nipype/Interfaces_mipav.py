class mipav_JistBrainMgdmSegmentation:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import JistBrainMgdmSegmentation
        at = JistBrainMgdmSegmentation()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outSegmented(self) -> None:
        return self.res.outputs.outSegmented

    def outLevelset(self) -> None:
        return self.res.outputs.outLevelset

    def outPosterior2(self) -> None:
        return self.res.outputs.outPosterior2

    def outPosterior3(self) -> None:
        return self.res.outputs.outPosterior3

###############################################################################


class mipav_JistBrainMp2rageDuraEstimation:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import JistBrainMp2rageDuraEstimation
        at = JistBrainMp2rageDuraEstimation()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outDura(self) -> None:
        return self.res.outputs.outDura

###############################################################################


class mipav_JistBrainMp2rageSkullStripping:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import JistBrainMp2rageSkullStripping
        at = JistBrainMp2rageSkullStripping()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outBrain(self) -> None:
        return self.res.outputs.outBrain

    def outMasked(self) -> None:
        return self.res.outputs.outMasked

    def outMasked2(self) -> None:
        return self.res.outputs.outMasked2

    def outMasked3(self) -> None:
        return self.res.outputs.outMasked3

###############################################################################


class mipav_JistBrainPartialVolumeFilter:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import JistBrainPartialVolumeFilter
        at = JistBrainPartialVolumeFilter()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outPartial(self) -> None:
        return self.res.outputs.outPartial

###############################################################################


class mipav_JistCortexSurfaceMeshInflation:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import JistCortexSurfaceMeshInflation
        at = JistCortexSurfaceMeshInflation()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outOriginal(self) -> None:
        return self.res.outputs.outOriginal

    def outInflated(self) -> None:
        return self.res.outputs.outInflated

###############################################################################


class mipav_JistIntensityMp2rageMasking:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import JistIntensityMp2rageMasking
        at = JistIntensityMp2rageMasking()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outSignal(self) -> None:
        return self.res.outputs.outSignal

    def outSignal2(self) -> None:
        return self.res.outputs.outSignal2

    def outMasked(self) -> None:
        return self.res.outputs.outMasked

    def outMasked2(self) -> None:
        return self.res.outputs.outMasked2

###############################################################################


class mipav_JistLaminarProfileCalculator:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import JistLaminarProfileCalculator
        at = JistLaminarProfileCalculator()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outResult(self) -> None:
        return self.res.outputs.outResult

###############################################################################


class mipav_JistLaminarProfileGeometry:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import JistLaminarProfileGeometry
        at = JistLaminarProfileGeometry()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outResult(self) -> None:
        return self.res.outputs.outResult

###############################################################################


class mipav_JistLaminarProfileSampling:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import JistLaminarProfileSampling
        at = JistLaminarProfileSampling()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outProfilemapped(self) -> None:
        return self.res.outputs.outProfilemapped

    def outProfile2(self) -> None:
        return self.res.outputs.outProfile2

###############################################################################


class mipav_JistLaminarROIAveraging:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import JistLaminarROIAveraging
        at = JistLaminarROIAveraging()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outROI3(self) -> None:
        return self.res.outputs.outROI3

###############################################################################


class mipav_JistLaminarVolumetricLayering:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import JistLaminarVolumetricLayering
        at = JistLaminarVolumetricLayering()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outContinuous(self) -> None:
        return self.res.outputs.outContinuous

    def outDiscrete(self) -> None:
        return self.res.outputs.outDiscrete

    def outLayer(self) -> None:
        return self.res.outputs.outLayer

###############################################################################


class mipav_MedicAlgorithmImageCalculator:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import MedicAlgorithmImageCalculator
        at = MedicAlgorithmImageCalculator()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outResult(self) -> None:
        return self.res.outputs.outResult

###############################################################################


class mipav_MedicAlgorithmLesionToads:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import MedicAlgorithmLesionToads
        at = MedicAlgorithmLesionToads()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outHard(self) -> None:
        return self.res.outputs.outHard

    def outHard2(self) -> None:
        return self.res.outputs.outHard2

    def outInhomogeneity(self) -> None:
        return self.res.outputs.outInhomogeneity

    def outMembership(self) -> None:
        return self.res.outputs.outMembership

    def outLesion(self) -> None:
        return self.res.outputs.outLesion

    def outSulcal(self) -> None:
        return self.res.outputs.outSulcal

    def outCortical(self) -> None:
        return self.res.outputs.outCortical

    def outFilled(self) -> None:
        return self.res.outputs.outFilled

    def outWM(self) -> None:
        return self.res.outputs.outWM

###############################################################################


class mipav_MedicAlgorithmMipavReorient:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import MedicAlgorithmMipavReorient
        at = MedicAlgorithmMipavReorient()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class mipav_MedicAlgorithmN3:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import MedicAlgorithmN3
        at = MedicAlgorithmN3()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outInhomogeneity(self) -> None:
        return self.res.outputs.outInhomogeneity

    def outInhomogeneity2(self) -> None:
        return self.res.outputs.outInhomogeneity2

###############################################################################


class mipav_MedicAlgorithmSPECTRE2010:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import MedicAlgorithmSPECTRE2010
        at = MedicAlgorithmSPECTRE2010()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outOriginal(self) -> None:
        return self.res.outputs.outOriginal

    def outStripped(self) -> None:
        return self.res.outputs.outStripped

    def outMask(self) -> None:
        return self.res.outputs.outMask

    def outPrior(self) -> None:
        return self.res.outputs.outPrior

    def outFANTASM(self) -> None:
        return self.res.outputs.outFANTASM

    def outd0(self) -> None:
        return self.res.outputs.outd0

    def outMidsagittal(self) -> None:
        return self.res.outputs.outMidsagittal

    def outSplitHalves(self) -> None:
        return self.res.outputs.outSplitHalves

    def outSegmentation(self) -> None:
        return self.res.outputs.outSegmentation

###############################################################################


class mipav_MedicAlgorithmThresholdToBinaryMask:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import MedicAlgorithmThresholdToBinaryMask
        at = MedicAlgorithmThresholdToBinaryMask()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class mipav_RandomVol:
    """
    Note:
        dependencies: Nipype,mipav
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.mipav.developer import RandomVol
        at = RandomVol()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def outRand1(self) -> None:
        return self.res.outputs.outRand1

###############################################################################


