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


def round_complex(number: complex, precision: int):
    return round(number.real, precision) + round(number.imag, precision) * 1j


def complex_tostring(number: complex):
    return '(' + str(number.real) + ('+' if number.imag > 0 else '-') + str(number.imag) + 'j)'


def adjust_complex(number: complex):
    return number.real if number.imag == 0 else number


def iterate(p0: complex, p1: complex, p2: complex, equation, precision: int, iteration_number: int):
    h0 = p1 - p0
    h1 = p2 - p1
    h0 = round_complex(h0, precision)
    h1 = round_complex(h1, precision)
    fp0, fp1, fp2 = [
        eval(equation.replace('$', complex_tostring(x))) for x in [p0, p1, p2]
    ]
    fp0 = round_complex(fp0, precision)
    fp1 = round_complex(fp1, precision)
    fp2 = round_complex(fp2, precision)
    sigma0 = (fp1 - fp0) / h0
    sigma1 = (fp2 - fp1) / h1
    sigma0 = round_complex(sigma0, precision)
    sigma1 = round_complex(sigma1, precision)
    a = (sigma1 - sigma0) / (h1 + h0)
    b = a * h1 + sigma1
    c = fp2
    a = round_complex(a, precision)
    b = round_complex(b, precision)
    z = sqrt(b ** 2 - 4 * a * c)
    z = round_complex(z, precision)
    p3 = p2 - ((2 * c) / (b + z * get_sign(b)))
    p3 = round_complex(p3, precision)
    fp3 = eval(equation.replace('$', complex_tostring(p3)))
    fp3 = round_complex(fp3, precision)
    error = round(
        sqrt((p3.real - p2.real) ** 2 + (p3.imag - p2.imag) ** 2).real,
        precision
    )
    return {
        "h0": adjust_complex(h0),
        "h1": adjust_complex(h1),
        "sigma0": adjust_complex(sigma0),
        "sigma1": adjust_complex(sigma1),
        "p0": adjust_complex(p0),
        "p1": adjust_complex(p1),
        "p2": adjust_complex(p2),
        "p3": adjust_complex(p3),
        "fp0": adjust_complex(fp0),
        "fp1": adjust_complex(fp1),
        "fp2": adjust_complex(fp2),
        "fp3": adjust_complex(fp3),
        "a": adjust_complex(a),
        "b": adjust_complex(b),
        "c": adjust_complex(c),
        "error": error,
        "number": iteration_number
    }


def refactor(equation):
    equation = list(equation.lower().replace('log', 'l').replace('ln', 'z').replace('arc', 'a').replace('x', '$'))
    i = 0
    while i < len(equation):
        if i != 0 and (equation[i] in blacklist) and (equation[i - 1] != '*'):
            if equation[i - 1].isnumeric() or equation[i - 1] == ')':
                equation.insert(i, '*')
        if equation[i] == '!' and equation[i + 1] != '(':
            equation.insert(i + 1, '(')
            counter = i + 2
            while equation[counter].isnumeric() or equation[counter] != ')':
                counter += 1
            equation.insert(counter, ')')
        i += 1
    for i in range(0, len(equation)):
        if equation[i] in substitution.keys():
            equation[i] = substitution[equation[i]]
    i = 0
    while i < len(equation):
        if equation[i] in substitution.values() and (equation[i - 1] in substitution.values()
                                                     or equation[i - 1] == 'e'):
            equation.insert(i, '*')
        i += 1
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
    while iteration_counter <= iterations and current_iteration['error'] > error:
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
    return solution, current_iteration['error']
