from django.shortcuts import render
from .models import *

"""
    Funciones relacionadas a la gestion de tax en la aplicacion
"""


def list_tax():
    tax = Tax.objects.all()
    return tax


def get_tax(id_tax):
    tax = Tax.objects.get(id_tax=id_tax)
    return tax


def create_tax_price(fk_price_product, fk_tax):
    TaxPriceProduct.objects.create(fk_tax=fk_tax, fk_price_product=fk_price_product)


