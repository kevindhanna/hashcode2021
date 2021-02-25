import collections

class Street:
    def __init__(self, start, end, name, length):
        self.start = start
        self.end = end
        self.length = length
        self.name = name

class Car:
    def __init__(self, route):
        self.route = route
        self.set_timer(0)

    def set_timer(duration):
        self.timer = duration

    def tick():
        self.timer -= 1

class Intersection(self):
    def __init__(self, id):
        self.id = id
        self.ends = collections.defaultdict(list) # a dict of lists of cars, indexed by street name

    def tick():
        # get green light from schedule, pop car if timer is <= 0
        # update and tick all cars

    def set_schedule(schedule):
        self.schedule = schedule # schedule instance

class Schedule():
    def __init__(self, [(street, count), (street2, count)]):
        self.streets = [street] * count + [street2] * count

    def tick():
        # magical generator to spit out self.streets

def global_tick(cars, streets, intersections):

def run(cars, streets, intersections, duration, score):

def parse_file(name):
    # intersections = {id => Intersection}
    # streets = {name => Street}
    # cars = [Car]
    with open(name, 'r') as f:
        Config = collections.namedtuple("Config", list("DISCF"))
        config = Config(*f.readline().strip().split())

        intersections = {}
        intersections[-1] = Intersection(-1)
        for i in range(0, config.I):
            intersections[i] = Intersection(i)

        streets = {}
        for s in range(0, config.S):
            start, end, name, length = f.readline().strip().split()
            streets[name] = Street(intersections[start], intersections[end], name, length)

        for c in range(0, config.C):
            route = [streets[name] for name in f.readline().strip().split()[1:]]
            cars.append(Car(route))

        return cars, streets, intersections, config

# Return args for run
def parse_lines(lines):
    return tuple()

# Return solution score
def score(result):
    return 1

# Return output string for submission
def output(result):
    return str(result)
