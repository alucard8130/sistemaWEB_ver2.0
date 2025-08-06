from django.db import models
from empleados.models import Empleado


class FondeoCajaChica(models.Model):
    numero_cheque = models.CharField(max_length=50)
    importe_cheque = models.DecimalField(max_digits=10, decimal_places=2)
    empleado_asignado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Cheque {self.numero_cheque} - Saldo: {self.saldo}"


class GastoCajaChica(models.Model):
    fondeo = models.ForeignKey(FondeoCajaChica, on_delete=models.CASCADE)
    descripcion = models.TextField()
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"Gasto {self.descripcion} - Importe: {self.importe}"


class ValeCaja(models.Model):
    fondeo = models.ForeignKey(FondeoCajaChica, on_delete=models.CASCADE)
    descripcion = models.TextField()
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return f"Vale {self.descripcion} - Importe: {self.importe}"
