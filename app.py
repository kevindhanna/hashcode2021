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
        street = self.streets[self.position % len(self.streets)]
        self.position += 1
        return street
    
class Intersection:
    def __init__(self, id):
        self.id = id
        self.ends = collections.defaultdict(list) # a dict of lists of cars, indexed by street name
        self.set_new_schedule()

    def tick(self):
        next_street = next(self.schedule)
        pending_cars = self.ends[next_street]
        if (pending_cars and pending_cars[0].timer <= 0):
            next_car = pending_cars.pop(0)
            next_car.cross_intersection()

    def set_new_schedule(self, streets = []):
        self.schedule = Schedule(streets) # schedule instance

def run(cars, streets, intersections, duration, score):
    pass

# Return args for run
def parse_lines(lines):
    Config = collections.namedtuple("Config", list("DISCF"))
    config = Config(next(lines).strip().split())

    intersections = {}
    for i in range(0, config.I):
        intersections[i] = Intersection(i)

    streets = {}
    for _ in range(0, config.S):
        start, end, name, length = next(lines).strip().split()
        streets[name] = Street(intersections[start], intersections[end], name, length)

    destination = []
    cars = []
    for _ in range(0, config.C):
        route = [streets[name] for name in next(lines).strip().split()[1:]]
        cars.append(Car(route, destination))

    return tuple(cars, streets, intersections, config)

# Return solution score
def score(result):
    return 1

# Return output string for submission
def output(result):
    return str(result)
