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
    path("Menu/<int:id>/edit",menuitems_edit,name="Menuitems_edit"),
    path('admin/', admin.site.urls),
]
