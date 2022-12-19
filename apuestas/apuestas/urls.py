
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('Applications.usuarios.url')),
    path('uplay/', include('uplay.url')),
    path('partidos/', include('Applications.partidos.url')),
    path('apuestas/', include('Applications.apuesta.url')),
]
