from django.db import models
# Create your models here.
class Venta(models.Model):
    idUsuario = models.IntegerField(db_column='idUsuario')  # Field name made lowercase.
    compraJson = models.TextField(db_column='compraJson')  # Field name made lowercase.
    precio = models.CharField(max_length=20)