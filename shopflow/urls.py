"""
URL configuration for shopflow project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from store.views import *

urlpatterns = [
    path('',login_view,name='login'),
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register_view'),
    path('categories/add/',category,name="category"),
    path('categories/',category_list,name="categories"),
    path('categories/<int:id>/edit/',category_edit,name="category_edit"),
    path('categories/<int:id>/delete/',category_delete,name='category_delete'),
    path('Menu/',menuitems,name="Menuitems"),
    path('Menu/add/',menuitems_add,name="Menuitems_add"),
    path("Menu/<int:id>/edit/",menuitems_edit,name="Menuitems_edit"),
    path("Menu/<int:id>/delete/",menuitems_delete,name="Menuitems_delete"),
    path("customers/",customer_list,name="customer_List"),
    path("customers/add/",add_customer,name="add_customer"),
    path("customers/<int:id>/edit/",edit_customer,name="edit_customer"),
    path("customers/<int:id>/delete/",delete_customer,name="delete_customer"),
    path("table/",table_list,name="table_list"),
    path("table/add/",add_table,name="add_table"),
    path('table/<int:id>/edit/',edit_table,name="edit_table"),
    path("table/<int:id>/delete/",delete_table,name="delete_table"),
    path("order/",order_list,name="order_list"),
    path('order/add/',add_order,name="add_order"),
    path('admin/', admin.site.urls),
]
