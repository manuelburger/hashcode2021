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

        DURATION_MULT = 1
        
        current_dir = os.getcwd()
        filepath = current_dir + "/output/" + input.name + "_out.txt"
        output = Output(filepath, input.name + "_out")
        
        d = input.sim_duration
        cars = input.cars

        print("Sim duration:", d)
        print("Cars:", input.num_cars)

        # Get random car

        # print("Guide car:", car, car.street_path)

        # Set 
        for i in range(0, 100):

            car = random.choice(cars)
            
            for inter, street in zip(car.intersection_path[1:], car.street_path):

                if inter not in output.intersections:
                    output.no_intersections = output.no_intersections + 1
                    output.intersections.add(inter)

                    # print("Set schedule of street", street, " inter ", inter)
                    # print("Available streets", inter.incoming_streets)
                    inter.schedule.set_street_to_front(street)
                    inter.schedule.set_duration_street(street, int(DURATION_MULT * len(inter.incoming_streets)), d)


        # Set remaining schedules according to default scheduling
        for id, inter in zip(input.intersections.keys(), input.intersections.values()):
            if inter not in output.intersections:

                sum_duration = 0
                for d in inter.schedule.durations.values():
                    sum_duration = sum_duration + d

                if sum_duration > 0: 
                    output.no_intersections = output.no_intersections + 1
                    output.intersections.add(inter)

        return output


    def getParameters(self):
        """
        Out:
            - params: dictionary of parameters for algorithm
        """
        return {}

