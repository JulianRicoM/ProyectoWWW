from django.urls import path
from .views import home, resultados, apuestas

urlpatterns = [
    path('', home),
    path('home', home),
    path('apuestas', apuestas),
    path('resultados', resultados),
]