def run(cars, streets, intersections, conf, destination):
    for s in streets.values():
        i = s.end
        i.set_new_schedule([(s.name, 1)] + i.schedule.streets)

    return cars, intersections, conf, destination
