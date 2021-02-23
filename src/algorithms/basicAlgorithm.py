# ------------------------------
#
# Basic Algorithm
#
# ------------------------------
from .algorithm import Algorithm
from ..data.output import Output


class BasicAlgorithm(Algorithm):

    def solve(self, input, parameters) -> Output:
        """
        In:
            - input: Object of class Input
            - parameters: dictionary of parameters for algorithm
        Out:
            - output: Object of class Output

        """
        
        output = Output()
        # TODO: Implement algorithm and set output properties


        return output


    def getParameters(self):
        """
        Out:
            - params: dictionary of parameters for algorithm
        """
        return {}

