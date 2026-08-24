class niftyreg_RegAladin:
    """
    Note:
        dependencies: Nipype,niftyreg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, ref_file="path", flo_file="path", **options):
        from nipype.interfaces.niftyreg.reg import RegAladin
        at = RegAladin()
        at.inputs.ref_file = ref_file
        at.inputs.flo_file = flo_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def aff_file(self) -> None:
        return self.res.outputs.aff_file

    def res_file(self) -> None:
        return self.res.outputs.res_file

    def avg_output(self) -> str:
        return self.res.outputs.avg_output

###############################################################################


class niftyreg_RegAverage:
    """
    Note:
        dependencies: Nipype,niftyreg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.niftyreg.regutils import RegAverage
        at = RegAverage()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyreg_RegF3D:
    """
    Note:
        dependencies: Nipype,niftyreg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, ref_file="path", flo_file="path", **options):
        from nipype.interfaces.niftyreg.reg import RegF3D
        at = RegF3D()
        at.inputs.ref_file = ref_file
        at.inputs.flo_file = flo_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def cpp_file(self) -> None:
        return self.res.outputs.cpp_file

    def res_file(self) -> None:
        return self.res.outputs.res_file

    def invcpp_file(self) -> None:
        return self.res.outputs.invcpp_file

    def invres_file(self) -> None:
        return self.res.outputs.invres_file

    def avg_output(self) -> str:
        return self.res.outputs.avg_output

###############################################################################


class niftyreg_RegJacobian:
    """
    Note:
        dependencies: Nipype,niftyreg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, trans_file="path", **options):
        from nipype.interfaces.niftyreg.regutils import RegJacobian
        at = RegJacobian()
        at.inputs.trans_file = trans_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyreg_RegMeasure:
    """
    Note:
        dependencies: Nipype,niftyreg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, ref_file="path", flo_file="path", measure_type="enumerate(('ncc','lncc','nmi','ssd'))", **options):
        from nipype.interfaces.niftyreg.regutils import RegMeasure
        at = RegMeasure()
        at.inputs.ref_file = ref_file
        at.inputs.flo_file = flo_file
        at.inputs.measure_type = measure_type
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyreg_RegResample:
    """
    Note:
        dependencies: Nipype,niftyreg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, ref_file="path", flo_file="path", **options):
        from nipype.interfaces.niftyreg.regutils import RegResample
        at = RegResample()
        at.inputs.ref_file = ref_file
        at.inputs.flo_file = flo_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyreg_RegTools:
    """
    Note:
        dependencies: Nipype,niftyreg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.niftyreg.regutils import RegTools
        at = RegTools()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class niftyreg_RegTransform:
    """
    Note:
        dependencies: Nipype,niftyreg
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.niftyreg.regutils import RegTransform
        at = RegTransform()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


