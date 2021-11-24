from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from .models import *
from ticket.views import card_sell

"""
    vistas de personas
"""


class AuxEmployee:
    def __init__(self):
        self.Employee = PersonPersonType()
        self.user = User()

    def set_employee(self, employee):
        self.Employee = employee

    def set_user(self, user):
        self.user = user

    def get_employee(self):
        return self.Employee

    def get_user(self):
        return self.user


aux = AuxEmployee()


def home_employee(request):
    return render(request, 'persons/home_persona.html')


def card_create_employee(request):
    person_type = PersonType.objects.exclude(person_type_name='cliente')
    return render(request, 'persons/crear_persona.html', {'person_types': person_type})


def card_list_employee(request):
    persons = PersonPersonType.objects.exclude(fk_id_person_type__person_type_name='cliente')
    return render(request, 'persons/listar_personas.html', {'persons': persons})


def card_update_employee(request):
    persons = PersonPersonType.objects.exclude(fk_id_person_type__person_type_name='cliente')
    return render(request, 'persons/admin_person.html', {'persons': persons})


def create_employee(request):
    person = Person.objects.create(person_name=request.POST['name'], person_last_name=request.POST['last_name'],
                                   person_address=request.POST['person_address'], person_dni=request.POST['dni'],
                                   person_phone=request.POST['phone'])
    person_type = PersonType.objects.get(id_person_type=request.POST['person_type'])
    PersonPersonType.objects.create(fk_id_person=person, fk_id_person_type=person_type)
    user = User.objects.create(username=request.POST['Username'], email=request.POST['Username'] + '@xyz.com',
                               first_name=request.POST['name'], last_name=request.POST['last_name'])
    user.set_password(request.POST['password'])
    user.save()

    if person_type.person_type_name == 'administrador':
        my_group = Group.objects.get(name='admin')
        my_group.user_set.add(user)
        my_group.save()
    else:
        my_group = Group.objects.get(name='cashier')
        my_group.user_set.add(user)
        my_group.save()
    return card_create_employee(request)


def delete_employee(request):
    employee = PersonPersonType.objects.get(fk_id_person=request.GET['id_person'])
    user = User.objects.get(first_name=employee.fk_id_person.person_name)
    regaux = employee.fk_id_person
    employee.delete()
    regaux.delete()
    user.delete()
    return card_update_employee(request)


def btn_create_clint(request):
    return render(request, 'sales/crear_cliente.html')


def create_client(request):
    person = Person.objects.create(person_name=request.POST['name'], person_last_name=request.POST['last_name'],
                                   person_address=request.POST['person_address'], person_dni=request.POST['dni'],
                                   person_phone=request.POST['phone'])
    person_type = PersonType.objects.get(person_type_name__exact='cliente')
    PersonPersonType.objects.create(fk_id_person=person, fk_id_person_type=person_type)
    return HttpResponseRedirect('/sell/card_select_client/')


def search_client(request):
    persons = Person.objects.filter(personpersontype__fk_id_person_type__person_type_name__exact='cliente',
                                    person_dni__contains=request.POST['id_number'])
    return render(request, 'sales/client.html', {'persons': persons})


def search_admin(request):
    persons = Person.objects.filter(personpersontype__fk_id_person_type__person_type_name__exact='administrador',
                                    person_dni__contains=request.POST['id_number'])
    return render(request, 'sales/select_administrator.html', {'persons': persons})
