class camino2trackvis_Camino2Trackvis:
    """
    Note:
        dependencies: Nipype,camino2trackvis
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", data_dims=0, voxel_dims=0.0, voxel_order="path", **options):
        from nipype.interfaces.camino2trackvis.convert import Camino2Trackvis
        at = Camino2Trackvis()
        at.inputs.in_file = in_file
        at.inputs.data_dims = data_dims
        at.inputs.voxel_dims = voxel_dims
        at.inputs.voxel_order = voxel_order
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def trackvis(self) -> None:
        return self.res.outputs.trackvis

###############################################################################


class camino2trackvis_Trackvis2Camino:
    """
    Note:
        dependencies: Nipype,camino2trackvis
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.camino2trackvis.convert import Trackvis2Camino
        at = Trackvis2Camino()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def camino(self) -> None:
        return self.res.outputs.camino

###############################################################################


