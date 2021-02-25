
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
        self.count = 0

    def __str__(self) -> str:
        return "Street: {}".format(self.name)


class Intersection():

    def __init__(self, id) -> None:
        
        self.id = id

        self.incoming_sections = set()
        self.outgoing_sections = set()

        self.outgoing_streets = set()
        self.incoming_streets = set()


        self.schedule = None

    def set_schedule(schedule):
        self.schedule = schedule

    def __str__(self) -> str:
        return "Inter: {}".format(self.id)


class Schedule():

    def __init__(self, intersection, streets) -> None:

        self.intersection = intersection
        
        self.durations = {}
        self.order = streets
        for street in streets:
            self.durations[street] = 1

    def set_street_to_front(street):

        if street in self.order:

            new_order = [street]
            for s in self.order:
                if not street == s:
                    new_order.append(s)

            if len(new_order) == len(self.order):
                self.order = new_order
            else:
                print("WARNING: new order different length from old order in schedule")

        else:
            print("WARNING: tried to set non-existent street on schedule")


    def set_duration_street(street, duration):
        self.durations[street] = duration


    def __str__(self) -> str:
        
        out = ""
        for s in self.order:
            out = out + (s, self.durations[s])




class Car():

    def __init__(self, id) -> None:

        self.id = id
        
        self.total_streets = 0

        self.street_path = []
        self.intersection_path = []


    def __str__(self) -> str:
        return "Car: {}".format(self.id)