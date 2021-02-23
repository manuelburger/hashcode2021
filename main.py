#!/usr/bin/env python3
# ------------------------------
#
# Main Program
#
# ------------------------------
import os
import time
import sys
from dask import delayed

from src.data.input import Input
from src.data.output import Output
from src.scoring.score import Score
from src.algorithms import *

FILES = ["dummy", "dummy2"]


def run_algorithm(algo, file, parameter={}):

    start_time = time.time()

    current_dir = os.getcwd()
    filepath = current_dir + "/input/" + file + ".txt"

    input = Input(filepath, file)
    input.parse()

    output = algo.solve(input, parameter)
    output.write()

    score = Score(output)

    end_time = time.time()

    print("{:<15}".format(algo.getName()) \
        + " executed input: " + "{:<10}".format(file) \
        + " in {:.2f}s".format(end_time - start_time) \
        + " | Score: " + "{:<5}".format(score.score) \
        + " | Params: " + str(parameter))


    return score.score


if __name__ == "__main__":

    print("-------------------------")
    print("      HashCode 2021      ")
    print("-------------------------")
    start_time_program = time.time()

    scores = []
    for f in FILES:
        res = delayed(run_algorithm)(BasicAlgorithm(), f)
        scores.append(res)

    total_scores = delayed(sum)(scores)
    total_scores = total_scores.compute() # Set num_workers=# to limit worker processes
    print("Total scores: ", total_scores)


    end_time_program = time.time()
    print("Whole execution took:", end_time_program - start_time_program)