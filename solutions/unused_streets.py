from collections import Counter
from . import cycle

def run(cars, streets, intersections, conf, destination):
    # Remove unused streets
    every = set(streets)
    used = set([street.name for car in cars for street in car.route])
    unused = every - used
    for name in unused:
        del streets[name]

    counter = Counter()
    for car in cars:
        counter += Counter(s.name for s in car.route)

    for i in intersections:
        if not i.ends:
            continue
        total_weight = sum(counter[name] for name in i.ends)
        smallest_count = min(counter[name] for name in i.ends)
        smallest_proportion = (1.0 * smallest_count / total_weight)
        schedule = []
        for name in i.ends:
            proportion = (1.0 * counter[name] / total_weight)
            duration = int(proportion / smallest_proportion)
            schedule.append((name, duration))
        i.set_new_schedule(schedule)

    return cycle.run(cars, streets, intersections, conf, destination)
    # return cars, intersections, conf, destination
