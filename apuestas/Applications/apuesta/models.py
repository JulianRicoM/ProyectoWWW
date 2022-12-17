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
    tipo_apuesta = models.ForeignKey(TipoApuesta, on_delete = models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete = models.CASCADE, blank=True, null=True)
