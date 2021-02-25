def run(cars, streets, intersections, conf, destination):
    for street in cars[0].route:
        intersections[street.end.id].set_new_schedule([(street.name, 1)])
    return cars, intersections, conf, destination
