class workbench_CiftiSmooth:
    """
    Note:
        dependencies: Nipype,workbench
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", sigma_surf=0.0, sigma_vol=0.0, direction="enumerate(('ROW','COLUMN'))", left_surf="path", right_surf="path", **options):
        from nipype.interfaces.workbench.cifti import CiftiSmooth
        at = CiftiSmooth()
        at.inputs.in_file = in_file
        at.inputs.sigma_surf = sigma_surf
        at.inputs.sigma_vol = sigma_vol
        at.inputs.direction = direction
        at.inputs.left_surf = left_surf
        at.inputs.right_surf = right_surf
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class workbench_MetricResample:
    """
    Note:
        dependencies: Nipype,workbench
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", current_sphere="path", new_sphere="path", method="enumerate(('ADAP_BARY_AREA','BARYCENTRIC'))", **options):
        from nipype.interfaces.workbench.metric import MetricResample
        at = MetricResample()
        at.inputs.in_file = in_file
        at.inputs.current_sphere = current_sphere
        at.inputs.new_sphere = new_sphere
        at.inputs.method = method
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

    def roi_file(self) -> None:
        return self.res.outputs.roi_file

###############################################################################


