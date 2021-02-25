import collections

class Street:
    def __init__(self, start, end, name, length):
        self.start = start
        self.end = end
        self.length = length
        self.name = name

class Car:
    def __init__(self, route, destination):
        self.route = route
        self.set_timer(0)
        self.destination = destination

    def set_timer(self, duration):
        self.timer = duration

    def cross_intersection(self):
        if not self.route:
            self.destination.append(self)
        else:
            next_street = self.route.pop(0)
            next_street.end.ends[next_street.name].append(self)
            self.set_timer(next_street.length)

    def tick(self):
        self.timer -= 1

class Schedule():
    def __init__(self, streets):
        self.streets = streets
        self.position = 0

    def __next__(self):
        # This is what jkz was talking about
        #
        # while True:
        #     for street in self.streets:
        #         yield street
        #
        street = self.streets[self.position % len(self.streets)]
        self.position += 1
        return street
    
class Intersection:
    def __init__(self, id):
        self.id = id
        self.ends = collections.defaultdict(list) # a dict of lists of cars, indexed by street name
        self.set_new_schedule()

    def tick(self):
        if self.schedule.streets:
            next_street = next(self.schedule)
            pending_cars = self.ends[next_street]
            if (pending_cars and pending_cars[0].timer <= 0):
                next_car = pending_cars.pop(0)
                next_car.cross_intersection()

    def set_new_schedule(self, streets = []):
        self.schedule = Schedule(streets) # schedule instance

# Return args for run
def parse_lines(lines):
    Config = collections.namedtuple("Config", list("DISCF"))
    config = Config(*map(int, lines.pop(0).strip().split()))

    intersections = {}
    for i in range(0, config.I):
        intersections[i] = Intersection(i)

    streets = {}
    for _ in range(0, config.S):
        start, end, name, length = lines.pop(0).strip().split()
        streets[name] = Street(intersections[int(start)], intersections[int(end)], name, length)

    destination = []
    cars = []
    for _ in range(0, config.C):
        route = [streets[name] for name in lines.pop(0).strip().split()[1:]]
        cars.append(Car(route, destination))

    return cars, streets, intersections, config, destination

# Return solution score
def score(cars, intersections, conf, destination):
    for _ in range(conf.D):
        for i in intersections.values():
            i.tick()
        for c in cars:
            c.tick()
    return sum(conf.F - car.timer for car in destination)

# Return output string for submission
def output(cars, intersections, conf, destination):
    lines = []
    i_with_schedules = [i for i in intersections.values() if i.schedule.streets]
    lines.append(len(i_with_schedules))
    for i in i_with_schedules:
        lines.append(i.id)
        lines.append(len(i.schedule.streets))
        for s in i.schedule.streets:
            lines.append(f"{s.name} {s.duration}")
    return '\n'.join(map(str, lines))
