from django.db import models
from provider.models import Provider

"""modelos relacionados con productos:
    - ProductType
    - Product
    - ProductProvider
    - PriceProduct
"""


class ProductType(models.Model):
    id_product_type = models.AutoField(primary_key=True)
    product_type_name = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'product_type'


class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45)
    fk_id_product_type = models.ForeignKey('ProductType', models.DO_NOTHING, db_column='fk_id_product_type')

    class Meta:
        managed = True
        db_table = 'product'


class ProductProvider(models.Model):
    id_product_provider = models.AutoField(primary_key=True)
    stock = models.IntegerField()
    bar_code = models.CharField(max_length=45)
    fk_id_product = models.ForeignKey(Product, models.DO_NOTHING, db_column='fk_id_product')
    fk_id_provider = models.ForeignKey(Provider, models.DO_NOTHING, db_column='fk_id_provider')

    class Meta:
        managed = True
        db_table = 'product_provider'


class PriceProduct(models.Model):
    id_price_product = models.AutoField(primary_key=True)
    sale_price = models.DecimalField(max_digits=13, decimal_places=2)
    shop_price = models.DecimalField(max_digits=13, decimal_places=2)
    start_date = models.DateField()
    user_update = models.CharField(max_length=40)
    date_update = models.DateField()
    fk_id_product_provider = models.ForeignKey('ProductProvider', models.DO_NOTHING, db_column='fk_id_product_provider')

    class Meta:
        managed = True
        db_table = 'price_product'




