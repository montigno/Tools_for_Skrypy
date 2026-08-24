class elastix_AnalyzeWarp:
    """
    Note:
        dependencies: Nipype,elastix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, transform_file="path", output_path="path", **options):
        from nipype.interfaces.elastix.registration import AnalyzeWarp
        at = AnalyzeWarp()
        at.inputs.transform_file = transform_file
        at.inputs.output_path = output_path
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def disp_field(self) -> None:
        return self.res.outputs.disp_field

    def jacdet_map(self) -> None:
        return self.res.outputs.jacdet_map

    def jacmat_map(self) -> None:
        return self.res.outputs.jacmat_map

###############################################################################


class elastix_ApplyWarp:
    """
    Note:
        dependencies: Nipype,elastix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, transform_file="path", moving_image="path", output_path="path", **options):
        from nipype.interfaces.elastix.registration import ApplyWarp
        at = ApplyWarp()
        at.inputs.transform_file = transform_file
        at.inputs.moving_image = moving_image
        at.inputs.output_path = output_path
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def warped_file(self) -> None:
        return self.res.outputs.warped_file

###############################################################################


class elastix_EditTransform:
    """
    Note:
        dependencies: Nipype,elastix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, transform_file="path", **options):
        from nipype.interfaces.elastix.utils import EditTransform
        at = EditTransform()
        at.inputs.transform_file = transform_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def output_file(self) -> None:
        return self.res.outputs.output_file

###############################################################################


class elastix_PointsWarp:
    """
    Note:
        dependencies: Nipype,elastix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, points_file="path", transform_file="path", output_path="path", **options):
        from nipype.interfaces.elastix.registration import PointsWarp
        at = PointsWarp()
        at.inputs.points_file = points_file
        at.inputs.transform_file = transform_file
        at.inputs.output_path = output_path
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def warped_file(self) -> None:
        return self.res.outputs.warped_file

###############################################################################


class elastix_Registration:
    """
    Note:
        dependencies: Nipype,elastix
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, fixed_image="path", moving_image="path", parameters=["path"], output_path="path", **options):
        from nipype.interfaces.elastix.registration import Registration
        at = Registration()
        at.inputs.fixed_image = fixed_image
        at.inputs.moving_image = moving_image
        at.inputs.parameters = parameters
        at.inputs.output_path = output_path
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def transform(self) -> list[None]:
        return self.res.outputs.transform

    def warped_file(self) -> None:
        return self.res.outputs.warped_file

    def warped_files(self) -> list[None]:
        return self.res.outputs.warped_files

    def warped_files_flags(self) -> list[bool]:
        return self.res.outputs.warped_files_flags

###############################################################################


