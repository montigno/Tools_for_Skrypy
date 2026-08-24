class mne_WatershedBEM:
    """
    Note:
        dependencies: Nipype,mne
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subject_id='', subjects_dir="path", **options):
        from nipype.interfaces.mne.base import WatershedBEM
        at = WatershedBEM()
        at.inputs.subject_id = subject_id
        at.inputs.subjects_dir = subjects_dir
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mesh_files(self) -> list[None]:
        return self.res.outputs.mesh_files

    def brain_surface(self) -> None:
        return self.res.outputs.brain_surface

    def inner_skull_surface(self) -> None:
        return self.res.outputs.inner_skull_surface

    def outer_skull_surface(self) -> None:
        return self.res.outputs.outer_skull_surface

    def outer_skin_surface(self) -> None:
        return self.res.outputs.outer_skin_surface

    def fif_file(self) -> None:
        return self.res.outputs.fif_file

    def cor_files(self) -> list[None]:
        return self.res.outputs.cor_files

###############################################################################


