from django.shortcuts import render
from calculator.muller_method import evaluate

# Create your views here.
blacklist = ['c', 'l', 's', 't', '\u03C0', '\u03C4', 'e', '$']

substitution = {
    '!': 'factorial',
    '\u03C0': 'pi',
    '\u03C4': 'tau',
    'l': 'log10',
    'z': 'log',
}


def index(request):
    return render(request, 'calculator/index.html')


def calculate(request):
    equation = list(request.GET["formula"].lower().replace('log', 'l').replace('ln', 'z').replace('x', '$'))
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
    equation = ''.join(equation).replace('^', '**')
    try:
        solution = evaluate(
            p0=float(request.GET["point1"]),
            p1=float(request.GET["point2"]),
            p2=float(request.GET["point3"]),
            equation=equation,
            error=float(request.GET["error"]),
            iterations=int(request.GET["iterations"]),
            precision=int(request.GET["precision"])
        )
    except ZeroDivisionError:
        solution = {}
    context = {
        "solution": solution,
        "equation": request.GET["formula"].lower(),
        "Answer": solution[len(solution) - 1]["p3"] if solution != {} else None,
        "Error": solution[len(solution) - 1]["error"] if solution != {} else None,
        "number": len(solution),
        "has_solution": solution != {}
    }
    return render(
        request=request,
        template_name='calculator/Answer.html',
        context=context
    )
