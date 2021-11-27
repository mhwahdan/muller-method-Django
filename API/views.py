from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from calculator.muller_method import refactor, evaluate
# Create your views here.


class CalculatorView(APIView):
    def get(self, request, formula, point1, point2, point3, error=None, iterations=None, precision=4):
        try:
            equation = refactor(formula)
            solution = evaluate(
                p0=float(point1),
                p1=float(point2),
                p2=float(point3),
                equation=equation,
                error=float(error),
                iterations=int(iterations),
                precision=int(precision)
            )
        except Exception:
            return Response({
                "status": "fail",
                "data": {},
            },
                status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "status": "success",
            "data": solution,
        },
            status=status.HTTP_200_OK)
