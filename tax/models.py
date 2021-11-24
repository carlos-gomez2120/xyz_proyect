from django.db import models
from product.models import PriceProduct

"""
    Modelos relacionados con tax:
     - Tax
     - TaxPriceProduct
"""


class Tax(models.Model):
    id_tax = models.AutoField(primary_key=True)
    tax_value = models.DecimalField(max_digits=5, decimal_places=2)
    tax_name = models.CharField(max_length=200)
    creation_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'tax'


class TaxPriceProduct(models.Model):
    id_tax_price_product = models.AutoField(primary_key=True)
    fk_id_price_product = models.ForeignKey(PriceProduct, models.DO_NOTHING, db_column='fk_id_price_product')
    fk_id_tax = models.ForeignKey(Tax, models.DO_NOTHING, db_column='fk_id_tax')

    class Meta:
        managed = True
        db_table = 'tax_price_product'

