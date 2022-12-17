from django.urls import path
from .views import EstatusList, BetTypeList, BetList, BetDetail, CreateBet

urlpatterns = [
    path('lista', BetList),
    path('estatus/', EstatusList.as_view()),
    path('tipoapuestas/', BetTypeList.as_view()),
    path('<int:id>/', BetDetail),
    path("", CreateBet)
]