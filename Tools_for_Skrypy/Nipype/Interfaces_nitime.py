class nitime_CoherenceAnalyzer:
    """
    Note:
        dependencies: Nipype,nitime
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.nitime.analysis import CoherenceAnalyzer
        at = CoherenceAnalyzer()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def coherence_array(self) -> str:
        return self.res.outputs.coherence_array

    def timedelay_array(self) -> str:
        return self.res.outputs.timedelay_array

    def coherence_csv(self) -> None:
        return self.res.outputs.coherence_csv

    def timedelay_csv(self) -> None:
        return self.res.outputs.timedelay_csv

    def coherence_fig(self) -> None:
        return self.res.outputs.coherence_fig

    def timedelay_fig(self) -> None:
        return self.res.outputs.timedelay_fig

###############################################################################


