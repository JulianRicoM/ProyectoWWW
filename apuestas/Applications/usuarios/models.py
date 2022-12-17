from django.db import models
from django.utils.translation import gettext as _

# --------------------------------- BASEMODEL ---------------------------------
class BaseModel(models.Model):
    
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# --------------------------------- USUARIO --------------------------------
class Usuarios(BaseModel):
    nombre = models.CharField(verbose_name = _("Nombre"), max_length = 30)
    documento = models.CharField(verbose_name = _("Documento"), max_length = 30, unique=True)
    puntos = models.IntegerField(verbose_name = _('Puntos'))
