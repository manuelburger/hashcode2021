# ------------------------------
#
# Input Class
#
# ------------------------------



class Input():

    # TODO: add fields according to input data

    def __init__(self, filepath, name):
        self.file = open(filepath, "r")
        self.name = name

    def parse(self):
        """
        Parse Input File and Store in local data structure
        In:
            - input: Object of class Input
            - parameters: dictionary of parameters for algorithm
        """
        # raise NotImplementedError("Implement Input Parser")

        if not self.file.mode == 'r':
            raise IOError("File should be opened in read-only mode")