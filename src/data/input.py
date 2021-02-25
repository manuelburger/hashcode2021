# ------------------------------
#
# Input Class
#
# ------------------------------


from src.data.objects import Car, Street, Intersection
class Input():

    # TODO: add fields according to input data

    def __init__(self, filepath, name):
        self.file = open(filepath, "r")
        self.name = name

    def parse(self):
        streets = {}
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
            streets[name] = Street(name, int(start), int(end), int(L))
            print(start, end, name, L)

        for c in range(0, num_cars):
            line = self.file.readline()
            car_list = line.strip("\n").strip(" ").split(" ")
            car = Car()
            car.street_path = [streets[street_name] for street_name in car_list[1:]]
            car.total_streets = int(car_list[0])
            cars.append(car)
            print(car)
        print(cars)
