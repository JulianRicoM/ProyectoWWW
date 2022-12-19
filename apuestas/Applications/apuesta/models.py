from django.db import models
from django.utils.translation import gettext as _

from Applications.usuarios.models import BaseModel, Usuarios
from Applications.partidos.models import Partidos

class Estado(models.Model):
    estado_apuesta = models.CharField(verbose_name = _("Estado"), max_length = 30)
    
class TipoApuesta(models.Model):
    tipo_apuesta = models.CharField(verbose_name = _("Apuesta"), max_length = 30)
    puntos = models.IntegerField(verbose_name = _("Puntos"), default=0)
    
class Apuesta(BaseModel):
    usuario = models.ForeignKey(Usuarios, on_delete = models.CASCADE)
    partido = models.ForeignKey(Partidos, on_delete = models.CASCADE)
    goles_equipo_local = models.IntegerField(verbose_name = _("Goles Equipo Local"), default=0)
    goles_equipo_visitante = models.IntegerField(verbose_name = _("Goles Equipo Visitante"), default=0)
    tarjetas_amarillas = models.IntegerField(verbose_name = _("Tarjetas Amarillas"), default=0)
    tarjetas_rojas = models.IntegerField(verbose_name = _("Tarjetas Rojas"), default=0)
    cantidad_goles = models.IntegerField(verbose_name = _("Tarjetas Rojas"), default=0)
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE, blank=True, null=True)
