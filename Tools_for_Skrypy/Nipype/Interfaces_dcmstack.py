class dcmstack_BaseInterface:
    """
    Note:
        dependencies: Nipype,dcmstack
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.base.core import BaseInterface
        at = BaseInterface()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class dcmstack_CopyMeta:
    """
    Note:
        dependencies: Nipype,dcmstack
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, src_file="path", dest_file="path", **options):
        from nipype.interfaces.dcmstack import CopyMeta
        at = CopyMeta()
        at.inputs.src_file = src_file
        at.inputs.dest_file = dest_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def dest_file(self) -> None:
        return self.res.outputs.dest_file

###############################################################################


class dcmstack_DcmStack:
    """
    Note:
        dependencies: Nipype,dcmstack
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dicom_files=["path"], **options):
        from nipype.interfaces.dcmstack import DcmStack
        at = DcmStack()
        at.inputs.dicom_files = dicom_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dcmstack_GroupAndStack:
    """
    Note:
        dependencies: Nipype,dcmstack
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, dicom_files=["path"], **options):
        from nipype.interfaces.dcmstack import GroupAndStack
        at = GroupAndStack()
        at.inputs.dicom_files = dicom_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_list(self) -> list[str]:
        return self.res.outputs.out_list

###############################################################################


class dcmstack_LookupMeta:
    """
    Note:
        dependencies: Nipype,dcmstack
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.dcmstack import LookupMeta
        at = LookupMeta()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class dcmstack_MergeNifti:
    """
    Note:
        dependencies: Nipype,dcmstack
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=[''], **options):
        from nipype.interfaces.dcmstack import MergeNifti
        at = MergeNifti()
        at.inputs.in_files = in_files
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class dcmstack_NiftiGeneratorBase:
    """
    Note:
        dependencies: Nipype,dcmstack
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.dcmstack import NiftiGeneratorBase
        at = NiftiGeneratorBase()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class dcmstack_SplitNifti:
    """
    Note:
        dependencies: Nipype,dcmstack
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.dcmstack import SplitNifti
        at = SplitNifti()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_list(self) -> list[None]:
        return self.res.outputs.out_list

###############################################################################


