class cat12_CAT12SANLMDenoising:
    """
    Note:
        dependencies: Nipype,cat12
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], **options):
        from nipype.interfaces.cat12.preprocess import CAT12SANLMDenoising
        at = CAT12SANLMDenoising()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class cat12_CAT12Segment:
    """
    Note:
        dependencies: Nipype,cat12
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], n_jobs=0, **options):
        from nipype.interfaces.cat12.preprocess import CAT12Segment
        at = CAT12Segment()
        at.inputs.in_files = in_files
        at.inputs.n_jobs = n_jobs
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def label_files(self) -> list[None]:
        return self.res.outputs.label_files

    def label_rois(self) -> None:
        return self.res.outputs.label_rois

    def label_roi(self) -> None:
        return self.res.outputs.label_roi

    def mri_images(self) -> list[None]:
        return self.res.outputs.mri_images

    def gm_modulated_image(self) -> None:
        return self.res.outputs.gm_modulated_image

    def gm_dartel_image(self) -> None:
        return self.res.outputs.gm_dartel_image

    def gm_native_image(self) -> None:
        return self.res.outputs.gm_native_image

    def wm_modulated_image(self) -> None:
        return self.res.outputs.wm_modulated_image

    def wm_dartel_image(self) -> None:
        return self.res.outputs.wm_dartel_image

    def wm_native_image(self) -> None:
        return self.res.outputs.wm_native_image

    def csf_modulated_image(self) -> None:
        return self.res.outputs.csf_modulated_image

    def csf_dartel_image(self) -> None:
        return self.res.outputs.csf_dartel_image

    def csf_native_image(self) -> None:
        return self.res.outputs.csf_native_image

    def bias_corrected_image(self) -> None:
        return self.res.outputs.bias_corrected_image

    def surface_files(self) -> list[None]:
        return self.res.outputs.surface_files

    def rh_central_surface(self) -> None:
        return self.res.outputs.rh_central_surface

    def rh_sphere_surface(self) -> None:
        return self.res.outputs.rh_sphere_surface

    def lh_central_surface(self) -> None:
        return self.res.outputs.lh_central_surface

    def lh_sphere_surface(self) -> None:
        return self.res.outputs.lh_sphere_surface

    def report_files(self) -> list[None]:
        return self.res.outputs.report_files

    def report(self) -> None:
        return self.res.outputs.report

###############################################################################


class cat12_ExtractAdditionalSurfaceParameters:
    """
    Note:
        dependencies: Nipype,cat12
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, left_central_surfaces=["path"], **options):
        from nipype.interfaces.cat12.surface import ExtractAdditionalSurfaceParameters
        at = ExtractAdditionalSurfaceParameters()
        at.inputs.left_central_surfaces = left_central_surfaces
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def lh_extracted_files(self) -> list[None]:
        return self.res.outputs.lh_extracted_files

    def rh_extracted_files(self) -> list[None]:
        return self.res.outputs.rh_extracted_files

    def lh_gyrification(self) -> list[None]:
        return self.res.outputs.lh_gyrification

    def rh_gyrification(self) -> list[None]:
        return self.res.outputs.rh_gyrification

    def lh_gmv(self) -> list[None]:
        return self.res.outputs.lh_gmv

    def rh_gmv(self) -> list[None]:
        return self.res.outputs.rh_gmv

    def lh_area(self) -> list[None]:
        return self.res.outputs.lh_area

    def rh_area(self) -> list[None]:
        return self.res.outputs.rh_area

    def lh_depth(self) -> list[None]:
        return self.res.outputs.lh_depth

    def rh_depth(self) -> list[None]:
        return self.res.outputs.rh_depth

    def lh_fractaldimension(self) -> list[None]:
        return self.res.outputs.lh_fractaldimension

    def rh_fractaldimension(self) -> list[None]:
        return self.res.outputs.rh_fractaldimension

###############################################################################


class cat12_ExtractROIBasedSurfaceMeasures:
    """
    Note:
        dependencies: Nipype,cat12
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, lh_roi_atlas=["path"], lh_surface_measure=["path"], **options):
        from nipype.interfaces.cat12.surface import ExtractROIBasedSurfaceMeasures
        at = ExtractROIBasedSurfaceMeasures()
        at.inputs.lh_roi_atlas = lh_roi_atlas
        at.inputs.lh_surface_measure = lh_surface_measure
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def label_files(self) -> list[None]:
        return self.res.outputs.label_files

###############################################################################


