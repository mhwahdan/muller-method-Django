from cmath import *
#from math import *

def get_sign(number):
    if isinstance(number,complex):
        if number.real > 0:
            return 1
        else:
            return -1
    else:
        if number > 0:
            return 1
        else:
            return -1


def iterate(p0, p1, p2, equation, precision, iteration_number):
    h0 = p1 - p0
    h1 = p2 - p1
    h0 = round(h0.real, precision) + round(h0.imag, precision) * 1j if isinstance(h0, complex) else round(h0, precision)
    h1 = round(h1.real, precision) + round(h1.imag, precision) * 1j if isinstance(h1, complex) else round(h1, precision)
    str_p0 = '(' + str(p0.real) + ('+' if p0.imag > 0 else '-') + str(p0.imag) + 'j)' if isinstance(p0, complex) else str(p0)
    str_p1 = '(' + str(p1.real) + ('+' if p1.imag > 0 else '-') + str(p1.imag) + 'j)' if isinstance(p1, complex) else str(p1)
    str_p2 = '(' + str(p2.real) + ('+' if p2.imag > 0 else '-') + str(p2.imag) + 'j)' if isinstance(p2, complex) else str(p2)
    fp0 = eval(equation.replace('$', str_p0))
    fp1 = eval(equation.replace('$', str_p1))
    fp2 = eval(equation.replace('$', str_p2))
    fp0 = round(fp0.real, precision) + round(p0.imag, precision) * 1j if isinstance(fp0, complex) else round(fp0, precision)
    fp1 = round(fp1.real, precision) + round(p1.imag, precision) * 1j if isinstance(fp1, complex) else round(fp1, precision)
    fp2 = round(fp2.real, precision) + round(p2.imag, precision) * 1j if isinstance(fp2, complex) else round(fp2, precision)
    sigma0 = (fp1 - fp0) / h0
    sigma1 = (fp2 - fp1) / h1
    sigma0 = round(sigma0.real, precision) + round(sigma0.imag, precision) * 1j if isinstance(sigma0, complex) else round(sigma0, precision)
    sigma1 = round(sigma1.real, precision) + round(sigma1.imag, precision) * 1j if isinstance(sigma1, complex) else round(sigma1, precision)
    a = (sigma1 - sigma0) / (h1 + h0)
    b = a * h1 + sigma1
    c = fp2
    a = round(a.real, precision) + round(a.imag, precision) * 1j if isinstance(a, complex) else round(a, precision)
    b = round(b.real, precision) + round(b.imag, precision) * 1j if isinstance(b, complex) else round(b, precision)
    underroot = sqrt(b**2 - 4 * a * c)
    underroot = round(underroot.real, precision) + round(underroot.imag, precision) * 1j if isinstance(underroot, complex) else round(underroot, precision)
    p3 = p2 - ((2 * c) / (b + underroot * get_sign(b)))
    p3 = round(p3.real, precision) + round(p3.imag, precision) * 1j if isinstance(p3, complex) else round(p3, precision)
    str_p3 = '(' + str(p3.real) + ('+' if p3.imag > 0 else '-') + str(p3.imag) + 'j)' if isinstance(p3, complex) else str(p3)
    fp3 = eval(equation.replace('$', str_p3))
    fp3 = round(fp3.real, precision) + round(fp3.imag, precision) * 1j if isinstance(fp3, complex) else round(fp3, precision)
    error = abs(p3 - p2)
    return {
        "h0": h0.real if h0.imag == 0 else h0,
        "h1": h1.real if h1.imag == 0 else h0,
        "sigma0": sigma0.real if sigma0.imag == 0 else sigma0,
        "sigma1": sigma1.real if sigma1.imag == 0 else sigma1,
        "p0": p0.real if p0.imag == 0 else p0,
        "p1": p1.real if p1.imag == 0 else p1,
        "p2": p2.real if p2.imag == 0 else p2,
        "p3": p3.real if p3.imag == 0 else p3,
        "fp0": fp0.real if fp0.imag == 0 else fp0,
        "fp1": fp1.real if fp1.imag == 0 else fp1,
        "fp2": fp2.real if fp2.imag == 0 else fp2,
        "fp3": fp3.real if fp3.imag == 0 else fp3,
        "a": a.real if a.imag == 0 else a,
        "b": b.real if b.imag == 0 else b,
        "c": c.real if c.imag == 0 else c,
        "error": round(error.real, precision),
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
