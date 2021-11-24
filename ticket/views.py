from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
from datetime import datetime
from .models import *
from persons.models import PersonPersonType, Person
from tax.models import TaxPriceProduct


class AuxTicket:
    def __init__(self):
        self.products_in_ticket = []
        self.list_products = []
        self.client = Person()
        self.admin = Person()
        self.ticket = Ticket()

    def set_products_in_ticket(self, products_in_ticket):
        self.products_in_ticket = products_in_ticket

    def get_products_in_ticket(self):
        return self.products_in_ticket

    def set_list_products(self, list_product):
        self.list_products = list_product

    def get_list_products(self):
        return self.list_products

    def set_client(self, id_client):
        self.client = Person.objects.get(id_person__exact=id_client)

    def get_client(self):
        return self.client

    def set_admin(self, id_admin):
        self.admin = Person.objects.get(id_person__exact=id_admin)

    def get_admin(self):
        return self.admin

    def set_ticket(self, ticket):
        self.ticket = ticket

    def get_ticket(self):
        return self.ticket

    def add_product(self, product):
        self.products_in_ticket.append(product)

    def remove_product(self, product):
        self.products_in_ticket.remove(product)

    def clean_list(self):
        result = {}
        aux = []
        for product in self.products_in_ticket:
            if product not in aux:
                aux.append(product)
                result.setdefault(product, 1)
            else:
                result[product] += 1

        return result

    def payment_and_update_stock(self, update):
        payment = 0
        for product in update:
            price_product = product.fk_id_tax_price_product.fk_id_price_product.sale_price * product.fk_id_tax_price_product.fk_id_tax.tax_value
            payment += price_product
            new_stock = product.fk_id_tax_price_product.fk_id_price_product.fk_id_product_provider.stock - product.amount
            product.fk_id_tax_price_product.fk_id_price_product.fk_id_product_provider.stock = new_stock
            product.fk_id_tax_price_product.fk_id_price_product.fk_id_product_provider.save()
        return payment


aux_ticket = AuxTicket()


def card_sell(request):
    persons = Person.objects.filter(personpersontype__fk_id_person_type__person_type_name__exact='administrador')
    return render(request, 'sales/select_administrator.html', {'persons': persons})


def chosee_client(request):
    aux_ticket.set_admin(request.GET['id_admin'])
    persons = Person.objects.filter(personpersontype__fk_id_person_type__person_type_name__exact='cliente')
    return render(request, 'sales/client.html', {'persons': persons})


def btn_select_products(request):
    product = TaxPriceProduct.objects.all()
    aux_ticket.set_client(request.GET['id_client'])
    aux_ticket.set_list_products(product)
    return HttpResponseRedirect('/sell/reload_ticket/')


def add_product_to_ticket(request):
    aux_ticket.add_product(TaxPriceProduct.objects.get(id_tax_price_product=request.GET['product']))
    return HttpResponseRedirect('/sell/reload_ticket/')


def ticket_creating(request):
    selected_products = aux_ticket.get_products_in_ticket()
    list_products = aux_ticket.get_list_products()
    return render(request, 'sales/select_products.html',
                  {'products': list_products, 'selected_products': selected_products})


def search_product(request):
    product = TaxPriceProduct.objects.filter(
        fk_id_price_product__fk_id_product_provider__bar_code__contains=request.POST['bar_code'])
    return render(request, 'sales/select_products.html',
                  {'products': product, 'selected_products': aux_ticket.get_products_in_ticket()})


def delete_product_selected(request):
    aux_ticket.remove_product(TaxPriceProduct.objects.get(id_tax_price_product=request.GET['product']))
    return HttpResponseRedirect('/sell/reload_ticket/')


def btn_create_ticket(request):
    date = datetime.now()
    client = aux_ticket.get_client()
    user = Person.objects.get(person_name=request.GET['username'])
    ticket = Ticket.objects.create(ticket_date=date, fk_id_person_customer=client, fk_id_person_cashier=user)
    aux_ticket.set_ticket(ticket)
    return create_ticket_detail(request)


def create_ticket_detail(request):
    ticket = aux_ticket.get_ticket()
    admin = aux_ticket.get_admin()
    products = aux_ticket.clean_list()
    for product in products:
        TicketDetail.objects.create(amount=products[product], fk_id_ticket=ticket, fk_id_tax_price_product=product,
                                    fk_id_person_administrator=admin)
    for_payment = TicketDetail.objects.filter(fk_id_ticket=ticket)
    payment = aux_ticket.payment_and_update_stock(for_payment)
    ticket.half_payment = payment
    ticket.save()
    return render(request, 'sales/ticket.html', {'ticket': ticket, 'products': for_payment})
