from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *


@login_required(login_url='/login/')
def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect('/login/')
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Username or password")
        else:
            login(request,user)
            return redirect('/categories/')

        
    return render(request,"login.html")

def register_view(request):
    if request.method == "POST":
        firstname=request.POST.get("firstname")
        lastname=request.POST.get('lastname')
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,"Username already taken")
            return redirect('/register')
        
        user=User.objects.create(
            first_name=firstname,
            last_name=lastname,
            username=username
        )
        user.set_password(password)
        user.save()
        messages.info(request,"Account created successfully")
        return redirect('/login/')
    return render(request,"register.html")

def category(request):
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        Category.objects.create(
            name=name,
            description=description
    )
        return redirect('/categories/')
    return render(request,"categories_form.html")

def category_list(request):
    C=Category.objects.all()
    context={'queryset':C}
    return render(request,"categories.html",context)    
def category_edit(request,id):
    category=Category.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get("name")
        description=request.POST.get("description")
        category.name=name
        category.description=description
        category.save()
        return redirect('/categories/')
    context={'category':category}
    return render(request,"categories_edit.html",context)

def category_delete(request,id):
    category=Category.objects.get(id=id)
    category.delete()
    return redirect('/categories/')
    
def menuitems(request):
    Menu=MenuItem.objects.all()
    context={'Menu':Menu}
    return render(request,"Menu.html",context)

def menuitems_add(request):
    categories=Category.objects.all()
    context={'queryset':categories}

    if request.method=="POST":
        name=request.POST.get("name")
        category_id=request.POST.get("category")
        price=request.POST.get('price')
        description=request.POST.get("description")
        availability=request.POST.get('is_available') == "on"

        category=Category.objects.get(id=category_id)
        MenuItem.objects.create(
            name=name,
            category=category,
            price=price,
            description=description,
            is_available=availability 
            )
        return redirect('/Menu/')
    return render(request,"menu_form.html",context)

def menuitems_edit(request):
    menu=MenuItem.objects.get(id=id)
    if request.method=="POST":
        name=request.POST.get('name')
        category=request.POST.get("category")
        price=request.POST.get("price")
        description=request.POST.get("description")
        availability=request.POST.get("is_available")
        menu.name=name
        menu.category=category
        menu.price=price
        menu.description=description
        menu.is_available=availability
        menu.save() 
        return redirect('/Menu/')
    context={'menu':menu}
    return render(request,"menu_edit.html",context)
    
    
