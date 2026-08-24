class mrtrix_ConstrainedSphericalDeconvolution:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", response_file="path", **options):
        from nipype.interfaces.mrtrix.tensors import ConstrainedSphericalDeconvolution
        at = ConstrainedSphericalDeconvolution()
        at.inputs.in_file = in_file
        at.inputs.response_file = response_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def spherical_harmonics_image(self) -> None:
        return self.res.outputs.spherical_harmonics_image

###############################################################################


class mrtrix_DWI2SphericalHarmonicsImage:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", encoding_file="path", **options):
        from nipype.interfaces.mrtrix.tensors import DWI2SphericalHarmonicsImage
        at = DWI2SphericalHarmonicsImage()
        at.inputs.in_file = in_file
        at.inputs.encoding_file = encoding_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def spherical_harmonics_image(self) -> None:
        return self.res.outputs.spherical_harmonics_image

###############################################################################


class mrtrix_DWI2Tensor:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file=["path"], **options):
        from nipype.interfaces.mrtrix.preprocess import DWI2Tensor
        at = DWI2Tensor()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tensor(self) -> None:
        return self.res.outputs.tensor

###############################################################################


class mrtrix_DiffusionTensorStreamlineTrack:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, gradient_encoding_file="path", in_file="path", **options):
        from nipype.interfaces.mrtrix.tracking import DiffusionTensorStreamlineTrack
        at = DiffusionTensorStreamlineTrack()
        at.inputs.gradient_encoding_file = gradient_encoding_file
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class mrtrix_Directions2Amplitude:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.tensors import Directions2Amplitude
        at = Directions2Amplitude()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix_Erode:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.preprocess import Erode
        at = Erode()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix_EstimateResponseForSH:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", mask_image="path", encoding_file="path", **options):
        from nipype.interfaces.mrtrix.tensors import EstimateResponseForSH
        at = EstimateResponseForSH()
        at.inputs.in_file = in_file
        at.inputs.mask_image = mask_image
        at.inputs.encoding_file = encoding_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def response(self) -> None:
        return self.res.outputs.response

###############################################################################


class mrtrix_FSL2MRTrix:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, bvec_file="path", bval_file="path", **options):
        from nipype.interfaces.mrtrix.tensors import FSL2MRTrix
        at = FSL2MRTrix()
        at.inputs.bvec_file = bvec_file
        at.inputs.bval_file = bval_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def encoding_file(self) -> None:
        return self.res.outputs.encoding_file

###############################################################################


class mrtrix_FilterTracks:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.tracking import FilterTracks
        at = FilterTracks()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix_FindShPeaks:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", directions_file="path", **options):
        from nipype.interfaces.mrtrix.tensors import FindShPeaks
        at = FindShPeaks()
        at.inputs.in_file = in_file
        at.inputs.directions_file = directions_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix_GenerateDirections:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, num_dirs=0, **options):
        from nipype.interfaces.mrtrix.tensors import GenerateDirections
        at = GenerateDirections()
        at.inputs.num_dirs = num_dirs
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix_GenerateWhiteMatterMask:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", binary_mask="path", encoding_file="path", **options):
        from nipype.interfaces.mrtrix.preprocess import GenerateWhiteMatterMask
        at = GenerateWhiteMatterMask()
        at.inputs.in_file = in_file
        at.inputs.binary_mask = binary_mask
        at.inputs.encoding_file = encoding_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def WMprobabilitymap(self) -> None:
        return self.res.outputs.WMprobabilitymap

###############################################################################


class mrtrix_MRConvert:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.preprocess import MRConvert
        at = MRConvert()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def converted(self) -> None:
        return self.res.outputs.converted

###############################################################################


class mrtrix_MRMultiply:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.mrtrix.preprocess import MRMultiply
        at = MRMultiply()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix_MRTrix2TrackVis:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.convert import MRTrix2TrackVis
        at = MRTrix2TrackVis()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix_MRTrixInfo:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.preprocess import MRTrixInfo
        at = MRTrixInfo()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class mrtrix_MRTrixViewer:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.mrtrix.preprocess import MRTrixViewer
        at = MRTrixViewer()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class mrtrix_MedianFilter3D:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.preprocess import MedianFilter3D
        at = MedianFilter3D()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix_ProbabilisticSphericallyDeconvolutedStreamlineTrack:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.tracking import ProbabilisticSphericallyDeconvolutedStreamlineTrack
        at = ProbabilisticSphericallyDeconvolutedStreamlineTrack()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class mrtrix_SphericallyDeconvolutedStreamlineTrack:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.tracking import SphericallyDeconvolutedStreamlineTrack
        at = SphericallyDeconvolutedStreamlineTrack()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class mrtrix_StreamlineTrack:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.tracking import StreamlineTrack
        at = StreamlineTrack()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class mrtrix_Tensor2ApparentDiffusion:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.preprocess import Tensor2ApparentDiffusion
        at = Tensor2ApparentDiffusion()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def ADC(self) -> None:
        return self.res.outputs.ADC

###############################################################################


class mrtrix_Tensor2FractionalAnisotropy:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.preprocess import Tensor2FractionalAnisotropy
        at = Tensor2FractionalAnisotropy()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def FA(self) -> None:
        return self.res.outputs.FA

###############################################################################


class mrtrix_Tensor2Vector:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.preprocess import Tensor2Vector
        at = Tensor2Vector()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def vector(self) -> None:
        return self.res.outputs.vector

###############################################################################


class mrtrix_Threshold:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.preprocess import Threshold
        at = Threshold()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class mrtrix_Tracks2Prob:
    """
    Note:
        dependencies: Nipype,mrtrix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.mrtrix.tracking import Tracks2Prob
        at = Tracks2Prob()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tract_image(self) -> None:
        return self.res.outputs.tract_image

###############################################################################


