from django.shortcuts import render
from datetime import datetime
from .models import *
from tax.views import *

"""
    vistas de productos
"""


class AuxProduct:
    def __init__(self):
        self.product = Product()
        self.product_provider = ProductProvider()
        self.product_type = ProductType()

    def set_product_type(self, product_type):
        self.product_type = product_type

    def set_product(self, product):
        self.product = product

    def set_product_provider(self, product_provider):
        self.product_provider = product_provider

    def get_product_type(self):
        return self.product_type

    def get_product(self):
        return self.product

    def get_product_provider(self):
        return self.product_provider


aux = AuxProduct()


def home_product(request):
    return render(request, 'product/home-producto.html')


def card_create_product(request):
    product_type = ProductType.objects.all()
    providers = Provider.objects.all()
    tax = list_tax()
    return render(request, 'product/crear_productos.html',
                  {'productsTypes': product_type, 'providers': providers, 'taxs': tax})


def card_list_product(request):
    products = ProductProvider.objects.all().select_related('fk_id_product', 'fk_id_provider')
    return render(request, 'product/listar_productos.html', {'products': products})


def card_update_product(request):
    products = ProductProvider.objects.all().select_related('fk_id_product', 'fk_id_provider')
    return render(request, 'product/admin_producto.html', {'products': products})


def create_product_type(request):
    ProductType.objects.create(product_type_name=request.POST['nameTypeProduct'])
    return card_create_product(request)


def create_product(request):
    product_type = ProductType.objects.get(id_product_type=request.POST['productType'])
    product = Product.objects.create(product_name=request.POST['nameProduct'], fk_id_product_type=product_type)
    provider = Provider.objects.get(id_provider=request.POST['provider'])
    product_provider = ProductProvider.objects.create(stock=request.POST['stock'], bar_code=request.POST['barCode'],
                                                      fk_id_provider=provider, fk_id_product=product)
    create_price_product(request, product_provider)


def create_price_product(request, product_provider):
    date = datetime.now()
    price_product = PriceProduct.objects.create(sale_price=request.POST['sale_price'],
                                                shop_price=request.POST['shop_price'],
                                                start_date=date, user_update=request.POST['username'],
                                                fk_id_product_provider=product_provider)
    tax = get_tax(request.POST['tax'])
    create_tax_price(price_product, tax)
    return card_create_product(request)


def select_product(request):
    product_provider = ProductProvider.objects.get(id_product_provider=request.GET['id_product_provider'])
    product_types = ProductType.objects.all()
    providers = Provider.objects.all()
    product = product_provider.fk_id_product
    product_type = product_provider.fk_id_product.fk_id_product_type
    aux.set_product(product)
    aux.set_product_provider(product_provider)
    aux.set_product_type(product_type)
    return render(request, 'product/update_producto.html',
                  {"product_provider": product_provider, "productsTypes": product_types, "providers": providers})


def update_product_type(request):
    product_type = aux.get_product_type()
    product_type.product_type_name = request.POST['nameTypeProduct']
    product_type.save()
    return card_update_product(request)


def update_product(request):
    product = aux.get_product()
    product_provider = aux.get_product_provider()
    product.product_name = request.POST['nameProduct']
    product.fk_id_product_type = ProductType.objects.get(id_product_type=request.POST['productType'])
    product.save()
    product_provider.stock = request.POST['stock']
    product_provider.bar_code = request.POST['barCode']
    product_provider.fk_id_provider = Provider.objects.get(id_provider=request.POST['provider'])
    product_provider.fk_id_product = product
    product_provider.save()
    return card_update_product(request)


def delete_product(request):
    product_provider = ProductProvider.objects.get(id_product_provider=request.GET['id_product_provider'])
    product_provider.delete()
    product = Product.objects.get(id_product=request.GET['id_product'])
    product.delete()
    return card_update_product(request)
