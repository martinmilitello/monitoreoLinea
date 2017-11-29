from django.db import models
from django.utils import timezone

# Importar el Modelo Cuentacajas o sea la base de datos MySQL
# from monitoreoLinea.APPS.MonitoreoDatos.models import Cuentacajas

# Create your models here.

class Cuentacajas(models.Model):
    now = timezone.datetime.now()

    Fecha = models.DateField()
    Hora=models.CharField(max_length=2)
    Mat_Caja = models.CharField(max_length=4)
    cant = models.IntegerField(default=12345)
    zona = models.IntegerField(default=125)
    revend = models.IntegerField(default=1400222)
    HoraAct=models.TimeField(default = now)

    class Cuentacajas:
        list_display = ('Fecha', 'Hora', 'Mat_Caja','Cant','zona','revend','HoraAct')
        list_filter = ('zona', 'HoraAct')
        ordering = ('-HoraAct',)
        search_fields = ('zona',)


    def cajas_acumu(self):
        CantCajas = str(self.cant)
        return CantCajas
    def __str__(self):
        return self.cajas_acumu()

    def mitiempo(self):
        Tiemponow = str(self.HoraAct)
        return Tiemponow
    def __str__(self):
        return self.mitiempo()

    def __unicode__(self):
        return self.HoraAct


