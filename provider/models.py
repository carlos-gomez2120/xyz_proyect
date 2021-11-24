from django.db import models

""" Modelo relacionado con Provider:
     -Provider
     Nota: este modele esta importado en la app product
"""


class Provider(models.Model):
    id_provider = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=45)
    url = models.CharField(max_length=45, blank=True, null=True)
    nit = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'provider'
