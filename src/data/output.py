# ------------------------------
#
# Output Class
#
# ------------------------------



class Output():

    # TODO: add fields according to output data

    def __init__(self, filepath, name):
        self.file = open(filepath, "w+")
        self.name = name

    def write():
        """
        Parse Input File and Store in local data structure
        In:
            - input: Object of class Input
            - parameters: dictionary of parameters for algorithm
        """
        raise NotImplementedError("Implement Output write method")