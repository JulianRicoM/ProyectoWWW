from django.db import models
from django.utils.translation import gettext as _

from Applications.usuarios.models import BaseModel

# --------------------------------- RESULTADO --------------------------------
class Resultado(models.Model):
    resultado = models.CharField(verbose_name = _("Resultado"), max_length = 30)
    
    def __str__(self):
        return self.resultado

# --------------------------------- PARTIDOS --------------------------------
class Partidos(BaseModel):
    equipo_local = models.CharField(verbose_name = _("Equipo Local"), max_length = 30)
    equipo_visitante = models.CharField(verbose_name = _("Equipo Visitante"), max_length = 30)
    resultado = models.ForeignKey(Resultado, on_delete= models.CASCADE, blank=True, null=True)
    marcador_local =models.IntegerField(verbose_name= _('Marcador equipo local'), blank=True, null=True)
    marcador_visitante =models.IntegerField(verbose_name= _('Marcador equipo visitante'), blank=True, null=True)
    tarjetas_amarillas = models.IntegerField(verbose_name= _('Tarjetas amarillas'), blank=True, null=True)
    tarjetas_rojas = models.IntegerField(verbose_name= _('Tarjetas rojas'), blank=True, null=True)
    goles =  models.IntegerField(verbose_name= _('Total de goles'), blank=True, null=True)
