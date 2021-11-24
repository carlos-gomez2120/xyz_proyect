"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from _curses_panel import panel
from importlib.resources import path

from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from login.views import Login, LogoutUsuario
from .views import *
from provider.views import *
from product.views import *
from persons.views import *
from ticket.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_login, name='redirect login'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(LogoutUsuario), name='logout'),
    path('select_type/', login_required(select_type), name='select user'),
    path('admin_xyz/', login_required(index_admin), name='index admin'),
    path('cajero_xyz/', login_required(index_cajero), name='index cajero'),
    # path's cashier
    path('sell/card_select_admin/', login_required(card_sell), name='card select admin'),
    path('sell/search_admin/', login_required(search_admin), name='search admin'),
    path('sell/select_client/', login_required(chosee_client), name='select client'),
    path('sell/btn_create_client/', login_required(btn_create_clint), name='btn create client'),
    path('sell/create_client/', login_required(create_client), name='create client'),
    path('sell/search_client/', login_required(search_client), name='search client'),
    path('sell/btn_select_products/', login_required(btn_select_products), name='select products'),
    path('sell/add_product/', login_required(add_product_to_ticket), name='add product'),
    path('sell/remove_product/', login_required(delete_product_selected), name='delete product selected'),
    path('sell/reload_ticket/', login_required(ticket_creating), name='reload ticket'),
    path('sell/search_product/', login_required(search_product), name='search product'),
    path('sell/generate_product/', login_required(btn_create_ticket), name='generate ticket'),
    # path's providers
    path('provider/', login_required(home_provider), name='home provider'),
    path('provider/card_create/', login_required(card_create_provider), name='card create provider'),
    path('provider/card_list/', login_required(card_list_provider), name='card list provider'),
    path('provider/card_update/', login_required(card_update_provider), name='card update provider'),
    path('provider/create/', login_required(create_provider), name='create provider'),
    path('provider/make_update/', login_required(select_provider), name='make update provider'),
    path('provider/update/', login_required(update_provider), name='update provider'),
    path('provider/deletel/', login_required(delete_provider), name='delete provider'),
    # path's product
    path('product/', login_required(home_product), name='home product'),
    path('product/card_create/', login_required(card_create_product), name='card create product'),
    path('product/card_list/', login_required(card_list_product), name='card list product'),
    path('product/card_update/', login_required(card_update_product), name='card update product'),
    path('product/create_type/', login_required(create_product_type), name='create product type'),
    path('product/create/', login_required(create_product), name='create product'),
    path('product/make_update/', login_required(select_product), name='make update product'),
    path('product/update_type/', login_required(update_product_type), name='update product type'),
    path('product/update/', login_required(update_product), name='update product'),
    path('product/delete/', login_required(delete_product), name='delete product'),
    # path's person
    path('employees/', login_required(home_employee), name='home employee'),
    path('employee/card_create/', login_required(card_create_employee), name='card create employee'),
    path('employee/card_list/', login_required(card_list_employee), name='card list employee'),
    path('employee/card_update/', login_required(card_update_employee), name='card update employee'),
    path('employee/create_employee/', login_required(create_employee), name='create employee'),
    path('employee/delete/', login_required(delete_employee), name='delete employee'),
]
