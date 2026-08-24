class io_BIDSDataGrabber:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, base_dir="path", index_derivatives=True, **options):
        from nipype.interfaces.io import BIDSDataGrabber
        at = BIDSDataGrabber()
        at.inputs.base_dir = base_dir
        at.inputs.index_derivatives = index_derivatives
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class io_BaseInterface:
    """
    Note:
        dependencies: Nipype,io
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


class io_DataFinder:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, root_paths=[''], **options):
        from nipype.interfaces.io import DataFinder
        at = DataFinder()
        at.inputs.root_paths = root_paths
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class io_DataGrabber:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, sort_filelist=True, template='', **options):
        from nipype.interfaces.io import DataGrabber
        at = DataGrabber()
        at.inputs.sort_filelist = sort_filelist
        at.inputs.template = template
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class io_DataSink:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.io import DataSink
        at = DataSink()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> str:
        return self.res.outputs.out_file

###############################################################################


class io_ExportFile:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", out_file="path", **options):
        from nipype.interfaces.io import ExportFile
        at = ExportFile()
        at.inputs.in_file = in_file
        at.inputs.out_file = out_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class io_FreeSurferSource:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, subjects_dir="path", subject_id='', **options):
        from nipype.interfaces.io import FreeSurferSource
        at = FreeSurferSource()
        at.inputs.subjects_dir = subjects_dir
        at.inputs.subject_id = subject_id
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def T1(self) -> None:
        return self.res.outputs.T1

    def aseg(self) -> None:
        return self.res.outputs.aseg

    def brain(self) -> None:
        return self.res.outputs.brain

    def brainmask(self) -> None:
        return self.res.outputs.brainmask

    def filled(self) -> None:
        return self.res.outputs.filled

    def norm(self) -> None:
        return self.res.outputs.norm

    def nu(self) -> None:
        return self.res.outputs.nu

    def orig(self) -> None:
        return self.res.outputs.orig

    def rawavg(self) -> None:
        return self.res.outputs.rawavg

    def ribbon(self) -> list[None]:
        return self.res.outputs.ribbon

    def wm(self) -> None:
        return self.res.outputs.wm

    def wmparc(self) -> None:
        return self.res.outputs.wmparc

    def curv(self) -> list[None]:
        return self.res.outputs.curv

    def avg_curv(self) -> list[None]:
        return self.res.outputs.avg_curv

    def inflated(self) -> list[None]:
        return self.res.outputs.inflated

    def pial(self) -> list[None]:
        return self.res.outputs.pial

    def area_pial(self) -> list[None]:
        return self.res.outputs.area_pial

    def curv_pial(self) -> list[None]:
        return self.res.outputs.curv_pial

    def smoothwm(self) -> list[None]:
        return self.res.outputs.smoothwm

    def sphere(self) -> list[None]:
        return self.res.outputs.sphere

    def sulc(self) -> list[None]:
        return self.res.outputs.sulc

    def thickness(self) -> list[None]:
        return self.res.outputs.thickness

    def volume(self) -> list[None]:
        return self.res.outputs.volume

    def white(self) -> list[None]:
        return self.res.outputs.white

    def jacobian_white(self) -> list[None]:
        return self.res.outputs.jacobian_white

    def graymid(self) -> list[None]:
        return self.res.outputs.graymid

    def label(self) -> list[None]:
        return self.res.outputs.label

    def annot(self) -> list[None]:
        return self.res.outputs.annot

    def aparc_aseg(self) -> list[None]:
        return self.res.outputs.aparc_aseg

    def sphere_reg(self) -> list[None]:
        return self.res.outputs.sphere_reg

    def aseg_stats(self) -> list[None]:
        return self.res.outputs.aseg_stats

    def wmparc_stats(self) -> list[None]:
        return self.res.outputs.wmparc_stats

    def aparc_stats(self) -> list[None]:
        return self.res.outputs.aparc_stats

    def BA_stats(self) -> list[None]:
        return self.res.outputs.BA_stats

    def aparc_a2009s_stats(self) -> list[None]:
        return self.res.outputs.aparc_a2009s_stats

    def curv_stats(self) -> list[None]:
        return self.res.outputs.curv_stats

    def entorhinal_exvivo_stats(self) -> list[None]:
        return self.res.outputs.entorhinal_exvivo_stats

###############################################################################


class io_IOBase:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.io import IOBase
        at = IOBase()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class io_JSONFileGrabber:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.io import JSONFileGrabber
        at = JSONFileGrabber()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class io_JSONFileSink:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.io import JSONFileSink
        at = JSONFileSink()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class io_S3DataGrabber:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, bucket='', sort_filelist=True, template='', **options):
        from nipype.interfaces.io import S3DataGrabber
        at = S3DataGrabber()
        at.inputs.bucket = bucket
        at.inputs.sort_filelist = sort_filelist
        at.inputs.template = template
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class io_SSHDataGrabber:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, hostname='', base_directory='', sort_filelist=True, template='', **options):
        from nipype.interfaces.io import SSHDataGrabber
        at = SSHDataGrabber()
        at.inputs.hostname = hostname
        at.inputs.base_directory = base_directory
        at.inputs.sort_filelist = sort_filelist
        at.inputs.template = template
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class io_SimpleInterface:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.base.core import SimpleInterface
        at = SimpleInterface()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class io_XNATSink:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, project_id='', subject_id='', experiment_id='', **options):
        from nipype.interfaces.io import XNATSink
        at = XNATSink()
        at.inputs.project_id = project_id
        at.inputs.subject_id = subject_id
        at.inputs.experiment_id = experiment_id
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class io_XNATSource:
    """
    Note:
        dependencies: Nipype,io
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, query_template='', **options):
        from nipype.interfaces.io import XNATSource
        at = XNATSource()
        at.inputs.query_template = query_template
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


