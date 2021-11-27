from django.urls import path
from API import views

base_str = 'muller_method/<str:formula>/<str:point1>/<str:point2>/<str:point3>'

urlpatterns = [
    path(base_str,
         views.CalculatorView.as_view()),
    path(base_str + '/<str:error>',
         views.CalculatorView.as_view()),
    path(base_str + '/<str:error>/<str:iterations>',
         views.CalculatorView.as_view()),
    path(base_str + '/<str:error>/<str:iterations>/<int:precision>',
         views.CalculatorView.as_view())
]
