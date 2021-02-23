# ------------------------------
#
# Basic Algorithm
#
# ------------------------------
import os
import time

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
        
        current_dir = os.getcwd()
        filepath = current_dir + "/output/" + input.name + "_out.txt"
        output = Output(filepath, input.name + "_out")
        # TODO: Implement algorithm and set output properties

        # TODO: remove
        time.sleep(2)

        return output


    def getParameters(self):
        """
        Out:
            - params: dictionary of parameters for algorithm
        """
        return {}

