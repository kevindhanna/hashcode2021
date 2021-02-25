import collections

class Street:
    def __init__(self, start, end, name, length):
        self.start = start
        self.end = end
        self.length = length
        self.name = name

class Car:
    def __init__(self, id, route):
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

# Return args for run
def parse_lines(lines):
    return tuple()

# Return solution score
def score(result):
    return 1

# Return output string for submission
def output(result):
    return str(result)
