# ------------------------------
#
# Score Class
#
# ------------------------------
from ..data.output import Output


class Score():



    def __init__(self, output):
        """
        Computes a score based on the output given
        """

        # TODO: implement score computation based on output
        self.score = hash(self) % 100


        # raise NotImplementedError("Score initializationn not implemented")