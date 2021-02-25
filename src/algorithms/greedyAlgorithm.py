# ------------------------------
#
# Basic Algorithm
#
# ------------------------------
import os
import time
import random

from .algorithm import Algorithm
from ..data.output import Output


class GreedyAlgorithm(Algorithm):

    def solve(self, input, parameters) -> Output:
        """
        In:
            - input: Object of class Input
            - parameters: dictionary of parameters for algorithm
        Out:
            - output: Object of class Output

        """

        DURATION_MULT = 4
        
        current_dir = os.getcwd()
        filepath = current_dir + "/output/" + input.name + "_out.txt"
        output = Output(filepath, input.name + "_out")
        
        d = input.sim_duration
        cars = input.cars

        # Get random car
        car = random.choice(cars)

        # Set 
        for inter, street in zip(car.intersection_path[1:], car.street_path):

            if inter not in output.intersections:
                output.no_intersections = output.no_intersections + 1
                output.intersections.add(inter)

                inter.schedule.set_street_to_front(street)
                inter.schedule.set_duration_street(street, DURATION_MULT * len(inter.incoming_streets))

        return output


    def getParameters(self):
        """
        Out:
            - params: dictionary of parameters for algorithm
        """
        return {}

