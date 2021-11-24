from django.shortcuts import render
from .models import Provider

"""
    vistas de proveedor:
"""


class AuxProvider:
    def __init__(self):
        self.provider = Provider()

    def set_provider(self, provider):
        self.provider = provider

    def get_provider(self):
        return self.provider


aux = AuxProvider()


def home_provider(request):
    return render(request, 'provider/home_proveedor.html')


def card_create_provider(request):
    return render(request, 'provider/crear_proveedor.html')


def card_list_provider(request):
    provider = Provider.objects.all()
    return render(request, 'provider/listar_proveedores.html', {'providers': provider})


def card_update_provider(request):
    provider = Provider.objects.all()
    return render(request, 'provider/admin_proveedor.html', {'providers': provider})


def create_provider(request):
    Provider.objects.create(name=request.POST['name'], address=request.POST['address'],
                            phone_number=request.POST['phone'], url=request.POST['url'], nit=request.POST['nit'])
    return card_create_provider(request)


def select_provider(request):
    provider = Provider.objects.get(id_provider=request.GET['id_provider'])
    aux.set_provider(provider)
    return render(request, 'provider/update_proveedores.html', {'provider': provider})


def update_provider(request):
    provider = aux.get_provider()
    provider.name = request.POST['name']
    provider.address = request.POST['address']
    provider.phone_number = request.POST['phone']
    provider.url = request.POST['url']
    provider.nit = request.POST['nit']
    provider.save()
    return card_update_provider(request)


def delete_provider(request):
    provider = Provider.objects.get(id_provider=request.GET['id_provider'])
    provider.delete()
    return card_update_provider(request)

