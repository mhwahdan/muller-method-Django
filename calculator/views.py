from django.shortcuts import render

from calculator.muller_method import evaluate, refactor


# Create your views here.


def index(request):
    return render(request, 'calculator/index.html')


def calculate(request):
    equation = refactor(request.GET['formula'])
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
