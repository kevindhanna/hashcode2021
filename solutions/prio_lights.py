import collections
from . import cycle

def run(*args):
    cars, streets, intersections, conf, destination = cycle.run(*args)

    startpositions = collections.Counter()
    for car in cars:
        startpositions[car.route[0].name] += 1

    for i in intersections:
        if (i.ends):
            s = sorted([(startpositions[street],street) for street in i.ends])
            bestest = s[-1][1]
            pos = [name for name, count in i.schedule.streets].index(bestest)
            i.schedule.streets = i.schedule.streets[pos:] + i.schedule.streets[:pos]

    return cars, streets, intersections, conf, destination

