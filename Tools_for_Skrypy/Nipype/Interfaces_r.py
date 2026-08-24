class r_RCommand:
    """
    Note:
        dependencies: Nipype,r
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, script='', **options):
        from nipype.interfaces.r import RCommand
        at = RCommand()
        at.inputs.script = script
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


