# ------------------------------
#
# Input Class
#
# ------------------------------


from src.data.objects import Car, Street, Intersection, Schedule
class Input():

    # TODO: add fields according to input data

    def __init__(self, filepath, name):
        self.file = open(filepath, "r")
        self.name = name

        self.streets = {}  # name to street obj
        self.intersections = {}  # id to instersection obj
        self.name_to_intersection = {}  # name to intersection obj tuple
        self.cars = []

    def parse(self):
        streets = {} #name to street obj
        intersections = {} #id to instersection obj
        name_to_intersection = {} #name to intersection obj tuple
        cars = []
        """
        Parse Input File and Store in local data structure
        In:
            - input: Object of class Input
            - parameters: dictionary of parameters for algorithm
        """
        # raise NotImplementedError("Implement Input Parser")

        if not self.file.mode == 'r':
            raise IOError("File should be opened in read-only mode")
        line = self.file.readline()
        sim_duration, num_intersections, num_streets, num_cars, points = list(map(int, line.strip(" ").split(" ")))

        for c in range(0, num_streets):
            line = self.file.readline()
            start, end, name, L = line.strip(" ").split(" ")
            start_idx, end_idx = int(start), int(end)

            if start_idx not in intersections.keys():
                intersections[start_idx] = Intersection(start_idx)
            if end_idx not in intersections.keys():
                intersections[end_idx] = Intersection(end_idx)

            start_section = intersections[start_idx]
            end_section = intersections[end_idx]
            start_section.outgoing_sections.add(intersections[end_idx])
            end_section.incoming_sections.add(intersections[start_idx])

            street = Street(name, start_section, end_section,  int(L))
            streets[name] = street
            name_to_intersection[name] = (start_section, end_section)

            start_section.outgoing_streets.add(street)
            end_section.incoming_sections.add(street)
            print(start, end, name, L)

        for c in range(0, num_cars):
            line = self.file.readline()
            car_list = line.strip("\n").strip(" ").split(" ")
            car = Car(c)
            car.street_path = [streets[street_name] for street_name in car_list[1:]]
            car.intersection_path = [name_to_intersection[street_name][0] for street_name in car_list[1:]]
            car.intersection_path.append(name_to_intersection[car_list[-1]][-1])
            car.total_streets = int(car_list[0])
            cars.append(car)
            print(car)

        #set default scheduler

        for id, intersec in zip(intersections.keys(), intersections.values()):
            intersec.schedule = Schedule(intersec, list(intersec.incoming_streets))

        print([[intersection.id for intersection in car.intersection_path] for car in cars])
        self.intersections = intersections
        self.name_to_intersection = name_to_intersection
        self.streets = streets
        self.cars = cars
        self.sim_duration, self.num_intersections, self.num_streets, self.num_cars, self.points = sim_duration, num_intersections, num_streets, num_cars, points

