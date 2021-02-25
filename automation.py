import os
import importlib

import app

def parse_lines(lines):
    M, T2, T3, T4 = lines[0].strip().split()

    pizzas = []
    for i, line in enumerate(lines[1:]):
        pizzas.append(app.Pizza(i, *line.strip().split()[1:]))
    
    return int(T2), int(T3), int(T4), pizzas

def load_solution(arg):
    if isinstance(arg, str):
        return importlib.import_module('solutions.' + arg).run
    elif callable(arg):
        return arg
    elif hasattr(arg, 'run'):
        return arg.run
    
def load_input(arg):
    if arg in os.listdir('inputs'):
        with open(os.path.join('inputs', arg)) as f:
            return parse_lines(f.readlines())
    elif isinstance(arg, str):
        return parse_lines(arg.split())
    else:
        return arg

def run_run(solution, input):
    run = load_solution(solution)
    args = load_input(input)

    deliveries = run(*args)
    score = app.score_total(deliveries)

    print(score)
    return score, deliveries

def run_run_run(solution):
    inputs = os.listdir('inputs')
    for i in inputs:
        print(i)
        run_run(solution, i)
        print("___________")
        print("\n")

if __name__ == '__main__':
    run('random', 'example')
