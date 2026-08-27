class float_operations_dyn():
    """
    docstring to be completed
    """
    def __init__(self,
                 operation="enumerate(('add', 'sub', 'mul', 'div'))",
                 list_float_in=0.0,
                 **dynamicsInputs):

        self.result = list_float_in
        if operation == 'add':
            for di, vi in dynamicsInputs.items():
                self.result = self.result + vi
        elif operation == 'sub':
            for di, vi in dynamicsInputs.items():
                self.result = self.result - vi
        elif operation == 'mul':
            for di, vi in dynamicsInputs.items():
                self.result = self.result * vi
        elif operation == 'div':
            for di, vi in dynamicsInputs.items():
                self.result = self.result / vi

    def out_result(self) -> float:
        return self.result

#############################################################################


class float_to_list_dyn():
    """
    docstring to be completed
    """
    def __init__(self,
                 float_in=0.0,
                 **dynamicsInputs):

        self.out = [float_in]
        for di in dynamicsInputs:
            self.out.append(dynamicsInputs[di])

    def list_float(self) -> list[float]:
        return self.out

#############################################################################


class float_to_int():
    """
    Allows the conversion of a float number to an integer number.
                   Example  1.1 --> 1

    Args:
        float_in: (float) float number

    Returns:
        outInt: (integer) integer number

    Note:
        GUI: no
    """
    def __init__(self,
                 float_in=0.0):

        self.outint = int(float_in)

    def outInt(self) -> int:
        return self.outint

###############################################################################


class float_to_string():
    """
    Allows the conversion of a floating number to string.
                  Example 1.1 --> '1.1'

    Args:
        float_in: (float) float number

    Returns:
        outString: (string) string of float number

    Note:
        GUI: no
    """
    def __init__(self,
                 float_in=0.0):

        self.outStr = str(float_in)

    def outString(self) -> str:
        return self.outStr
