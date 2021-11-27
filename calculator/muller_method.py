from cmath import *

blacklist = ['c', 'l', 's', 't', '\u03C0', '\u03C4', 'e', '$']

substitution = {
    '!': 'factorial',
    '\u03C0': 'pi',
    '\u03C4': 'tau',
    'l': 'log10',
    'z': 'log',
}


def get_sign(number):
    if isinstance(number, complex):
        if number.real > 0:
            return 1
        else:
            return -1
    else:
        if number > 0:
            return 1
        else:
            return -1


def iterate(p0: complex, p1: complex, p2: complex, equation, precision: int, iteration_number: int):
    h0 = p1 - p0
    h1 = p2 - p1
    h0, h1 = [round(x.real, precision) + round(x.imag, precision) * 1j for x in [h0, h1]]
    str_p0, str_p1, str_p2 = ['(' + str(x.real) + ('+' if x.imag > 0 else '-') + str(x.imag) + 'j)'
                              for x in [p0, p1, p2]]
    fp0, fp1, fp2 = [eval(equation.replace('$', x)) for x in [str_p0, str_p1, str_p2]]
    fp0, fp1, fp2 = [round(x.real, precision) + round(x.imag, precision) * 1j for x in [fp0, fp1, fp2]]
    sigma0 = (fp1 - fp0) / h0
    sigma1 = (fp2 - fp1) / h1
    sigma0, sigma1 = [round(x.real, precision) + round(x.imag, precision) * 1j for x in [sigma0, sigma1]]
    a = (sigma1 - sigma0) / (h1 + h0)
    b = a * h1 + sigma1
    c = fp2
    a, b = [round(x.real, precision) + round(x.imag, precision) * 1j for x in [a, b]]
    z = sqrt(b ** 2 - 4 * a * c)
    z = round(z.real, precision) + round(z.imag, precision) * 1j
    p3 = p2 - ((2 * c) / (b + z * get_sign(b)))
    p3 = round(p3.real, precision) + round(p3.imag, precision) * 1j
    str_p3 = '(' + str(p3.real) + ('+' if p3.imag > 0 else '-') + str(p3.imag) + 'j)'
    fp3 = eval(equation.replace('$', str_p3))
    fp3 = round(fp3.real, precision) + round(fp3.imag, precision) * 1j
    error = round(sqrt((p3.real - p2.real) ** 2 + (p3.imag - p2.imag) ** 2).real, precision)
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
        "error": error,
        "number": iteration_number
    }


def refactor(equation):
    equation = list(equation.lower().replace('log', 'l').replace('ln', 'z').replace('x', '$'))
    for i in range(0, len(equation)):
        if i != 0 and equation[i] in blacklist and equation[i - 1] != '*' and (
                equation[i - 1].isnumeric() or equation[i - 1] == ')'):
            equation.insert(i, '*')
        if equation[i] == '!' and equation[i + 1] != '(':
            equation.insert(i + 1, '(')
            counter = i + 2
            while equation[counter].isnumeric() or equation[counter] != ')':
                counter += 1
            equation.insert(counter, ')')
    for i in range(0, len(equation)):
        if equation[i] in substitution.keys():
            equation[i] = substitution[equation[i]]
    for i in range(1, len(equation)):
        if equation[i] in substitution.values() and (equation[i - 1] in substitution.values()
                                                     or equation[i - 1] == 'e'):
            equation.insert(i, '*')
    return ''.join(equation).replace('^', '**')


def evaluate(p0: complex, p1: complex, p2: complex, equation, error: float, iterations: int, precision: int):
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
