class matlab_MatlabCommand:
    """
    Note:
        dependencies: Nipype,matlab
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, script='', **options):
        from nipype.interfaces.matlab import MatlabCommand
        at = MatlabCommand()
        at.inputs.script = script
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


