# ------------------------------
#
# Base Algorithm
#
# ------------------------------
from ..data.output import Output


class Algorithm():

    def solve(self, input, parameters) -> Output:
        """
        In:
            - input: Object of class Input
            - parameters: dictionary of parameters for algorithm
        Out:
            - output: Object of class Output

        """
        raise NotImplementedError("Implement solver for Algorithm: {}".format(self.__class__.__name__))


    def getParameters(self):
        """
        Out:
            - params: dictionary of parameters for algorithm
        """
        raise NotImplementedError("Implement solver for Algorithm: {}".format(self.__class__.__name__))

    def getName(self):
        return str(self.__class__.__name__)
