from math import *
import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

def get_sign(number):
    if number > 0:
        return 1
    else:
        return -1


def generator(string):
    return lambda x : np.vectorize(eval(string))


def iterate(p0, p1, p2, equation, precision, iteration_number):

    h0 = p1 - p0
    h1 = p2 - p1
    fp0 = eval(equation.replace('$', str(p0)))
    fp1 = eval(equation.replace('$', str(p1)))
    fp2 = eval(equation.replace('$', str(p2)))
    sigma0 = (fp1 - fp0) / h0
    sigma1 = (fp2 - fp1) / h1
    a = (sigma1 - sigma0) / (h1 + h0)
    b = a * h1 + sigma1
    c = fp2
    underroot = b**2 - 4 * a * c
    if underroot < 0:
        underroot = complex(b, sqrt(- underroot))
    else:
        underroot = sqrt(underroot)
    p3 = p2 - ((2 * c) / (b + underroot * get_sign(b)))
    fp3 = eval(equation.replace('$', str(p3)))
    error = abs(p3 - p2)
    if not isinstance(p3, complex):
        p3 = round(p3, precision)
        fp3 = round(fp3, precision)
        error = round(error, precision)
    return {
        "h0": h0,
        "h1": h1,
        "sigma0": sigma0,
        "sigma1": sigma1,
        "p0": p0,
        "p1": p1,
        "p2": p2,
        "p3": p3,
        "fp0": fp0,
        "fp1": fp1,
        "fp2": fp2,
        "fp3": fp3,
        "a": a,
        "b": b,
        "c": c,
        "error": error,
        "number": iteration_number
    }


def evaluate(p0, p1, p2, equation, error, iterations, precision):
    iteration_counter = 1
    current_iteration = iterate(
        p0=p0,
        p1=p1,
        p2=p2,
        equation=equation,
        precision=precision,
        iteration_number=iteration_counter
    )
    solution = [current_iteration]
    iteration_counter = 2
    while iteration_counter <= iterations and current_iteration["error"] > error:
        p0 = current_iteration["p1"]
        p1 = current_iteration["p2"]
        p2 = current_iteration["p3"]
        current_iteration = iterate(
            p0=p0,
            p1=p1,
            p2=p2,
            equation=equation,
            precision=precision,
            iteration_number=iteration_counter
        )
        solution.append(current_iteration)
        iteration_counter += 1
    return solution
