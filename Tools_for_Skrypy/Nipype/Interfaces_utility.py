class utility_AssertEqual:
    """
    Note:
        dependencies: Nipype,utility
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.utility.base import AssertEqual
        at = AssertEqual()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class utility_CSVReader:
    """
    Note:
        dependencies: Nipype,utility
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", **options):
        from nipype.interfaces.utility.csv import CSVReader
        at = CSVReader()
        at.inputs.in_file = in_file
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


class utility_Merge:
    """
    Note:
        dependencies: Nipype,utility
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.utility.base import Merge
        at = Merge()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out(self) -> list[str]:
        return self.res.outputs.out

###############################################################################


class utility_Rename:
    """
    Note:
        dependencies: Nipype,utility
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, in_file="path", format_string='', **options):
        from nipype.interfaces.utility.base import Rename
        at = Rename()
        at.inputs.in_file = in_file
        at.inputs.format_string = format_string
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out_file(self) -> None:
        return self.res.outputs.out_file

###############################################################################


class utility_Select:
    """
    Note:
        dependencies: Nipype,utility
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, **options):
        from nipype.interfaces.utility.base import Select
        at = Select()
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

    def out(self) -> list[str]:
        return self.res.outputs.out

###############################################################################


class utility_Split:
    """
    Note:
        dependencies: Nipype,utility
        GUI: no
        link_web: (click Ctrl + U)
    """
    def __init__(self, inlist=[''], splits=[0], **options):
        from nipype.interfaces.utility.base import Split
        at = Split()
        at.inputs.inlist = inlist
        at.inputs.splits = splits
        for ef in options:
            setattr(at.inputs, ef, options[ef])
        self.res = at.run()

###############################################################################


