# ------------------------------
#
# Output Class
#
# ------------------------------



class Output():

    # TODO: add fields according to output data

    def __init__(self, filepath, name):
        self.file = open(filepath, "w")
        self.name = name

        # Class fields
        self.no_intersections = 0
        self.intersections = set()

    def write(self):
        """
        Parse Input File and Store in local data structure
        In:
            - input: Object of class Input
            - parameters: dictionary of parameters for algorithm
        """

        # No of intersections for which we set a schedule
        self.file.write("{}\n".format(self.no_intersections))

        # Output each schedule
        for inter in self.intersections:

            sum_duration = 0
            for d in inter.schedule.durations.values():
                sum_duration = sum_duration + d

            if not sum_duration > 0:
                print("WARNING")

            schedule = []
            for street in inter.schedule.order:

                d = inter.schedule.durations[street]
                if d > 0:
                    schedule.append((street.name, d))

            if len(schedule) > 0:
                self.file.write("{}\n".format(inter.id)) # Print ID of intersection
                self.file.write("{}\n".format(len(schedule))) # Print number of schedules
                for s in schedule:
                    self.file.write("{} {}\n".format(s[0], s[1])) # Print for each street name and duration


        self.file.close()