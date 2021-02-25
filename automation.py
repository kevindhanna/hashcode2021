import pathlib
import os
import sys
import importlib
import datetime
import json

import app

ROOT = os.path.dirname(__file__)

def ls(dir):
    for f in os.listdir(dir):
        if f.startswith('__'):
            continue
        yield f

def module_name(s):
    return s[:-len('.py')] if s.endswith('.py') else s

def input_name(s):
    return s[:-len('.in')] if s.endswith('.in') else s

def load_solution(arg):
    '''
    Pass in one of:
    - the name of a module in ./solutions
    - a function
    '''
    if isinstance(arg, str):
        return importlib.import_module('solutions.' + module_name(arg)).run
    elif callable(arg):
        return arg
    else:
        raise ValueError(f"Invalid value for solution: {arg}")
    
def load_input(arg):
    '''
    Pass in one of:
    - the name of a file in ./inputs
    - the path to a file
    - a tuple of arguments to be passed to run
    '''
    inputs_dir = os.path.join(ROOT, 'inputs')
    if arg in ls(inputs_dir):
        with open(os.path.join(inputs_dir, arg)) as f:
            return app.parse_lines(f.readlines())
    elif isinstance(arg, str):
        return app.parse_lines(arg.split())
    else:
        return arg

def store_run(solution, input, score, output):
    results_dir = os.path.join(ROOT, "results")
    pathlib.Path(results_dir).mkdir(exist_ok=True)
    file_name = '-'.join([
        str(datetime.datetime.now()).split('.')[0].replace(' ', '-').replace(':', '-'),
        module_name(str(solution)),
        input_name(str(input)),
        str(score),
    ])
    file_path = os.path.join(results_dir, file_name)
    with open(file_path + '.out', 'x') as f:
        f.write(output)

def run_run(solution, input):
    run = load_solution(solution)
    args = load_input(input)

    result = run(*args)
    score = app.score(*result)
    output = app.output(*result)
    print(score)
    store_run(solution, input, score, output)

    return score, result

def run_run_run(solution):
    inputs = ls(os.path.join(ROOT, 'inputs'))
    for i in inputs:
        print(f"** {i}")
        run_run(solution, i)


def run_run_run_run():
    solutions = ls(os.path.join(ROOT, 'solutions'))
    for s in solutions:
        if s == '__init__.py':
            continue
        print(f"* {s}")
        run_run_run(s)

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0 or len(args) >= 3 or {'-h', '--help'} & set(args):
        print("""
Usage:
        
Run a specific solution for a specific input

    automation.py [SOLUTION] [INPUT] 

Run a specific solution for all inputs:

    automation.py [SOLUTION]

Run all solutions for all inputs:

    automation.py --all

SOLUTION should be the name of a module in ./solutions with a run() function
INPUT should be the name of a file in ./inputs
""")
    elif len(args) == 2:
        run_run(*args)
    elif len(args) == 1:
        if args[0] == '--all':
            run_run_run_run()
        else:
            run_run_run(*args)