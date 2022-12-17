from django.urls import path
from .views import MatchList, ResultList, MatchDetail, CreateMatch

urlpatterns = [
    path('lista', MatchList),
    path('resultados/', ResultList.as_view()),
    path('<int:id>/', MatchDetail),
    path("", CreateMatch)
]