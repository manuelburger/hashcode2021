
# -----------------------------
#
# Street Class
#
# ------------------------------
class Street():

    def __init__(self, name, start_section, end_section, L) -> None:
        
        self.name = name
        self.L = L
        self.start_section = start_section
        self.end_section = end_section


class Intersection():

    def __init__(self, id) -> None:
        
        self.id = id

        self.incoming_sections = []
        self.outgoing_sections = []

        self.outgoing_streets = []
        self.incoming_streets = []





class Car():

    def __init__(self) -> None:
        pass