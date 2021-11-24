from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User


def index_admin(request):
    user = User.objects.get(username=request.GET['user_name'])
    if user.groups.filter(name='admin').exists():
        return render(request, 'index-admin.html')
    else:
        return select_type(request)


def index_cajero(request):
    user = User.objects.get(username=request.GET['user_name'])
    if user.groups.filter(name='cashier').exists():
        return render(request, 'index-cajero.html')
    else:
        return select_type(request)


def redirect_login(request):
    return HttpResponseRedirect('/accounts/login/')


def select_type(request):
    return render(request, 'type_user.html')
