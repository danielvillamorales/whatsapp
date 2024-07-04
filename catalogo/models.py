from django.db import models


# Create your models here.
class WpReferenciasdisponibles(models.Model):
    referenciaunica = models.CharField(max_length=53, blank=True, null=True)
    referencia = models.CharField(max_length=11, blank=True, null=True)
    codcolor = models.CharField(max_length=2, blank=True, null=True)
    consecutivo = models.IntegerField()
    desc_referencia = models.CharField(max_length=50, blank=True, null=True)
    descgrupo = models.CharField(max_length=50, blank=True, null=True)
    descsubgrupo = models.CharField(max_length=50, blank=True, null=True)
    grupo = models.CharField(max_length=2, blank=True, null=True)
    subgrupo = models.CharField(max_length=5, blank=True, null=True)
    tiquete = models.DecimalField(
        max_digits=28, decimal_places=2, blank=True, null=True
    )
    composicion = models.CharField(max_length=50, blank=True, null=True)
    colormp = models.CharField(max_length=50, blank=True, null=True)
    diseño = models.CharField(max_length=50, blank=True, null=True)
    concepto = models.CharField(max_length=50, blank=True, null=True)
    coleccion = models.CharField(max_length=150, blank=True, null=True)
    tallas = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "wp_referenciasdisponibles"


class WpFotosCatalago(models.Model):
    referenciaunica = models.CharField(max_length=53, blank=True, null=True)
    ruta = models.CharField(max_length=1000, blank=True, null=True)


class WpDisponibles(models.Model):
    bodega = models.CharField(max_length=9, blank=True, null=True)
    referenciaunica = models.CharField(max_length=53, blank=True, null=True)
    referencia = models.CharField(max_length=11, blank=True, null=True)
    codcolor = models.CharField(max_length=2, blank=True, null=True)
    consecutivo = models.IntegerField()
    desc_referencia = models.CharField(max_length=50, blank=True, null=True)
    descgrupo = models.CharField(max_length=50, blank=True, null=True)
    descsubgrupo = models.CharField(max_length=50, blank=True, null=True)
    grupo = models.CharField(max_length=2, blank=True, null=True)
    subgrupo = models.CharField(max_length=5, blank=True, null=True)
    tiquete = models.DecimalField(
        max_digits=28, decimal_places=2, blank=True, null=True
    )
    composicion = models.CharField(max_length=50, blank=True, null=True)
    colormp = models.CharField(max_length=50, blank=True, null=True)
    diseño = models.CharField(max_length=50, blank=True, null=True)
    concepto = models.CharField(max_length=50, blank=True, null=True)
    tallas = models.CharField(max_length=4000, blank=True, null=True)
    silueta = models.CharField(max_length=100, blank=True, null=True)
    coleccion = models.CharField(max_length=150, blank=True, null=True)
    ruta = models.CharField(max_length=1000, blank=True, null=True)
    color = models.CharField(max_length=500, blank=True, null=True)
    observacion = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "wp_disponibles"
