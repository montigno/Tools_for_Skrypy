class camino_AnalyzeHeader:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", datatype="enumerate(('byte','char','[u]short','[u]int','float','complex','double'))", **options):
        from nipype.interfaces.camino.convert import AnalyzeHeader
        at = AnalyzeHeader()
        at.inputs.in_file = in_file
        at.inputs.datatype = datatype
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def header(self) -> None:
        return self.res.outputs.header

###############################################################################


class camino_ComputeEigensystem:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.camino.dti import ComputeEigensystem
        at = ComputeEigensystem()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def eigen(self) -> None:
        return self.res.outputs.eigen

###############################################################################


class camino_ComputeFractionalAnisotropy:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.camino.dti import ComputeFractionalAnisotropy
        at = ComputeFractionalAnisotropy()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def fa(self) -> None:
        return self.res.outputs.fa

###############################################################################


class camino_ComputeMeanDiffusivity:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.camino.dti import ComputeMeanDiffusivity
        at = ComputeMeanDiffusivity()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def md(self) -> None:
        return self.res.outputs.md

###############################################################################


class camino_ComputeTensorTrace:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.camino.dti import ComputeTensorTrace
        at = ComputeTensorTrace()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def trace(self) -> None:
        return self.res.outputs.trace

###############################################################################


class camino_Conmat:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", target_file="path", **options):
        from nipype.interfaces.camino.connectivity import Conmat
        at = Conmat()
        at.inputs.in_file = in_file
        at.inputs.target_file = target_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def conmat_sc(self) -> None:
        return self.res.outputs.conmat_sc

    def conmat_ts(self) -> None:
        return self.res.outputs.conmat_ts

###############################################################################


class camino_DT2NIfTI:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", header_file="path", **options):
        from nipype.interfaces.camino.convert import DT2NIfTI
        at = DT2NIfTI()
        at.inputs.in_file = in_file
        at.inputs.header_file = header_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def dt(self) -> None:
        return self.res.outputs.dt

    def exitcode(self) -> None:
        return self.res.outputs.exitcode

    def lns0(self) -> None:
        return self.res.outputs.lns0

###############################################################################


class camino_DTIFit:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", scheme_file="path", **options):
        from nipype.interfaces.camino.dti import DTIFit
        at = DTIFit()
        at.inputs.in_file = in_file
        at.inputs.scheme_file = scheme_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tensor_fitted(self) -> None:
        return self.res.outputs.tensor_fitted

###############################################################################


class camino_DTLUTGen:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, scheme_file="path", **options):
        from nipype.interfaces.camino.dti import DTLUTGen
        at = DTLUTGen()
        at.inputs.scheme_file = scheme_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def dtLUT(self) -> None:
        return self.res.outputs.dtLUT

###############################################################################


class camino_DTMetric:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, eigen_data="path", metric="enumerate(('fa','md','rd','l1','l2','l3','tr','ra','2dfa','cl','cp','cs'))", **options):
        from nipype.interfaces.camino.dti import DTMetric
        at = DTMetric()
        at.inputs.eigen_data = eigen_data
        at.inputs.metric = metric
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def metric_stats(self) -> None:
        return self.res.outputs.metric_stats

###############################################################################


class camino_FSL2Scheme:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, bvec_file="path", bval_file="path", **options):
        from nipype.interfaces.camino.convert import FSL2Scheme
        at = FSL2Scheme()
        at.inputs.bvec_file = bvec_file
        at.inputs.bval_file = bval_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def scheme(self) -> None:
        return self.res.outputs.scheme

###############################################################################


class camino_Image2Voxel:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.camino.convert import Image2Voxel
        at = Image2Voxel()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def voxel_order(self) -> None:
        return self.res.outputs.voxel_order

###############################################################################


class camino_ImageStats:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_files=["path"], stat="enumerate(('min','max','mean','median','sum','std','var'))", output_root="path", **options):
        from nipype.interfaces.camino.utils import ImageStats
        at = ImageStats()
        at.inputs.in_files = in_files
        at.inputs.stat = stat
        at.inputs.output_root = output_root
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class camino_LinRecon:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", scheme_file="path", qball_mat="path", **options):
        from nipype.interfaces.camino.odf import LinRecon
        at = LinRecon()
        at.inputs.in_file = in_file
        at.inputs.scheme_file = scheme_file
        at.inputs.qball_mat = qball_mat
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def recon_data(self) -> None:
        return self.res.outputs.recon_data

###############################################################################


class camino_MESD:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", inverter="enumerate(('SPIKE','PAS'))", inverter_param=0.0, scheme_file="path", **options):
        from nipype.interfaces.camino.odf import MESD
        at = MESD()
        at.inputs.in_file = in_file
        at.inputs.inverter = inverter
        at.inputs.inverter_param = inverter_param
        at.inputs.scheme_file = scheme_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def mesd_data(self) -> None:
        return self.res.outputs.mesd_data

###############################################################################


class camino_ModelFit:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, model="enumerate(('dt','restore','algdt','nldt_pos','nldt','ldt_wtd','adc','ball_stick','cylcyl dt','cylcyl restore','cylcyl algdt','cylcyl nldt_pos','cylcyl nldt','cylcyl ldt_wtd','cylcyl adc','cylcyl ball_stick','cylcyl_eq dt','cylcyl_eq restore','cylcyl_eq algdt','cylcyl_eq nldt_pos','cylcyl_eq nldt','cylcyl_eq ldt_wtd','cylcyl_eq adc','cylcyl_eq ball_stick','pospos dt','pospos restore','pospos algdt','pospos nldt_pos','pospos nldt','pospos ldt_wtd','pospos adc','pospos ball_stick','pospos_eq dt','pospos_eq restore','pospos_eq algdt','pospos_eq nldt_pos','pospos_eq nldt','pospos_eq ldt_wtd','pospos_eq adc','pospos_eq ball_stick','poscyl dt','poscyl restore','poscyl algdt','poscyl nldt_pos','poscyl nldt','poscyl ldt_wtd','poscyl adc','poscyl ball_stick','poscyl_eq dt','poscyl_eq restore','poscyl_eq algdt','poscyl_eq nldt_pos','poscyl_eq nldt','poscyl_eq ldt_wtd','poscyl_eq adc','poscyl_eq ball_stick','cylcylcyl dt','cylcylcyl restore','cylcylcyl algdt','cylcylcyl nldt_pos','cylcylcyl nldt','cylcylcyl ldt_wtd','cylcylcyl adc','cylcylcyl ball_stick','cylcylcyl_eq dt','cylcylcyl_eq restore','cylcylcyl_eq algdt','cylcylcyl_eq nldt_pos','cylcylcyl_eq nldt','cylcylcyl_eq ldt_wtd','cylcylcyl_eq adc','cylcylcyl_eq ball_stick','pospospos dt','pospospos restore','pospospos algdt','pospospos nldt_pos','pospospos nldt','pospospos ldt_wtd','pospospos adc','pospospos ball_stick','pospospos_eq dt','pospospos_eq restore','pospospos_eq algdt','pospospos_eq nldt_pos','pospospos_eq nldt','pospospos_eq ldt_wtd','pospospos_eq adc','pospospos_eq ball_stick','posposcyl dt','posposcyl restore','posposcyl algdt','posposcyl nldt_pos','posposcyl nldt','posposcyl ldt_wtd','posposcyl adc','posposcyl ball_stick','posposcyl_eq dt','posposcyl_eq restore','posposcyl_eq algdt','posposcyl_eq nldt_pos','posposcyl_eq nldt','posposcyl_eq ldt_wtd','posposcyl_eq adc','posposcyl_eq ball_stick','poscylcyl dt','poscylcyl restore','poscylcyl algdt','poscylcyl nldt_pos','poscylcyl nldt','poscylcyl ldt_wtd','poscylcyl adc','poscylcyl ball_stick','poscylcyl_eq dt','poscylcyl_eq restore','poscylcyl_eq algdt','poscylcyl_eq nldt_pos','poscylcyl_eq nldt','poscylcyl_eq ldt_wtd','poscylcyl_eq adc','poscylcyl_eq ball_stick'))", in_file="path", scheme_file="path", **options):
        from nipype.interfaces.camino.dti import ModelFit
        at = ModelFit()
        at.inputs.model = model
        at.inputs.in_file = in_file
        at.inputs.scheme_file = scheme_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def fitted_data(self) -> None:
        return self.res.outputs.fitted_data

###############################################################################


class camino_NIfTIDT2Camino:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.camino.convert import NIfTIDT2Camino
        at = NIfTIDT2Camino()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class camino_PicoPDFs:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", luts=["path"], **options):
        from nipype.interfaces.camino.dti import PicoPDFs
        at = PicoPDFs()
        at.inputs.in_file = in_file
        at.inputs.luts = luts
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def pdfs(self) -> None:
        return self.res.outputs.pdfs

###############################################################################


class camino_ProcStreamlines:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.camino.convert import ProcStreamlines
        at = ProcStreamlines()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def proc(self) -> None:
        return self.res.outputs.proc

    def outputroot_files(self) -> list[None]:
        return self.res.outputs.outputroot_files

###############################################################################


class camino_QBallMX:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, scheme_file="path", **options):
        from nipype.interfaces.camino.odf import QBallMX
        at = QBallMX()
        at.inputs.scheme_file = scheme_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def qmat(self) -> None:
        return self.res.outputs.qmat

###############################################################################


class camino_SFLUTGen:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", info_file="path", **options):
        from nipype.interfaces.camino.calib import SFLUTGen
        at = SFLUTGen()
        at.inputs.in_file = in_file
        at.inputs.info_file = info_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def lut_one_fibre(self) -> None:
        return self.res.outputs.lut_one_fibre

    def lut_two_fibres(self) -> None:
        return self.res.outputs.lut_two_fibres

###############################################################################


class camino_SFPICOCalibData:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, scheme_file="path", info_file="path", **options):
        from nipype.interfaces.camino.calib import SFPICOCalibData
        at = SFPICOCalibData()
        at.inputs.scheme_file = scheme_file
        at.inputs.info_file = info_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def PICOCalib(self) -> None:
        return self.res.outputs.PICOCalib

    def calib_info(self) -> None:
        return self.res.outputs.calib_info

###############################################################################


class camino_SFPeaks:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", inputmodel="enumerate(('sh','maxent','rbf'))", **options):
        from nipype.interfaces.camino.odf import SFPeaks
        at = SFPeaks()
        at.inputs.in_file = in_file
        at.inputs.inputmodel = inputmodel
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def peaks(self) -> None:
        return self.res.outputs.peaks

###############################################################################


class camino_Shredder:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.camino.convert import Shredder
        at = Shredder()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def shredded(self) -> None:
        return self.res.outputs.shredded

###############################################################################


class camino_Track:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.camino.dti import Track
        at = Track()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class camino_TrackBallStick:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.camino.dti import TrackBallStick
        at = TrackBallStick()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class camino_TrackBayesDirac:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, scheme_file="path", **options):
        from nipype.interfaces.camino.dti import TrackBayesDirac
        at = TrackBayesDirac()
        at.inputs.scheme_file = scheme_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class camino_TrackBedpostxDeter:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, bedpostxdir="path", **options):
        from nipype.interfaces.camino.dti import TrackBedpostxDeter
        at = TrackBedpostxDeter()
        at.inputs.bedpostxdir = bedpostxdir
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class camino_TrackBedpostxProba:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, bedpostxdir="path", **options):
        from nipype.interfaces.camino.dti import TrackBedpostxProba
        at = TrackBedpostxProba()
        at.inputs.bedpostxdir = bedpostxdir
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class camino_TrackBootstrap:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, scheme_file="path", bsdatafiles=["path"], **options):
        from nipype.interfaces.camino.dti import TrackBootstrap
        at = TrackBootstrap()
        at.inputs.scheme_file = scheme_file
        at.inputs.bsdatafiles = bsdatafiles
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class camino_TrackDT:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.camino.dti import TrackDT
        at = TrackDT()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class camino_TrackPICo:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.camino.dti import TrackPICo
        at = TrackPICo()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def tracked(self) -> None:
        return self.res.outputs.tracked

###############################################################################


class camino_TractShredder:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.camino.convert import TractShredder
        at = TractShredder()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def shredded(self) -> None:
        return self.res.outputs.shredded

###############################################################################


class camino_VtkStreamlines:
    """
    Note:
        dependencies: Nipype,camino
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.camino.convert import VtkStreamlines
        at = VtkStreamlines()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def vtk(self) -> None:
        return self.res.outputs.vtk

###############################################################################


