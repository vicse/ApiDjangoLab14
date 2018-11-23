from django.db import models


class Producto(models.Model):
    codigo = models.AutoField(primary_key=True, max_length=100, null=False)
    descripcion = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=50, decimal_places=2)

    class Meta:
        db_table = "productos"