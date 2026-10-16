from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from decimal import Decimal


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

def menuitems_edit(request,id):
    menu=MenuItem.objects.get(id=id)
    categories=Category.objects.all()
    context={'menu':menu,'queryset':categories}

    if request.method=="POST":
        name=request.POST.get('name')
        category_id=request.POST.get("category")
        price=request.POST.get("price")
        description=request.POST.get("description")
        availability=request.POST.get("is_available") == "on"   
        category=Category.objects.get(id=category_id)
        menu.name=name
        menu.category=category
        menu.price=price
        menu.description=description
        menu.is_available=availability
        menu.save() 
        return redirect('/Menu/')
    return render(request,"menu_edit.html",context)
    
def menuitems_delete(request,id):
    Menu=MenuItem.objects.get(id=id)
    Menu.delete()
    return redirect('/Menu/')

def customer_list(request):
    customers=Customer.objects.all()
    context={'customers':customers}
    return render(request,"customer.html",context)

def add_customer(request):
    customer=Customer.objects.all()
    
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        Customer.objects.create(
            name=name,
            email=email,
            phone=phone,
            address=address,   
            )
        return redirect('/customers/')
    return render(request,"customer_form.html")

def edit_customer(request,id):
    customer=Customer.objects.get(id=id)
    context={"customer":customer}
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        address=request.POST.get("address")
        customer.name=name
        customer.email=email
        customer.phone=phone
        customer.address=address
        customer.save()
        return redirect('/customers/')
    return render(request,"customer_edit.html",context)

def delete_customer(request,id):
    C=Customer.objects.get(id=id)
    C.delete()
    return redirect('/customers/')

def table_list(request):
    table=Table.objects.all()
    context={'table':table}
    return render(request,"table.html",context)

def add_table(request):
    table=Table.objects.all()
    if request.method == "POST":
        table_number=request.POST.get("table_number")
        capacity=request.POST.get("capacity")
        status=request.POST.get("status")
        Table.objects.create(
            table_number=table_number,
            capacity=capacity,
            status=status
        )
        return redirect("/table/")
    return render(request,"table_form.html")
def edit_table(request,id):
    table=Table.objects.get(id=id)
    context={'table':table}
    if request.method == "POST":
        table_number=request.POST.get("table_number")
        capacity=request.POST.get("capacity")
        status=request.POST.get("status")
        table.table_number=table_number
        table.capacity=capacity
        table.status=status
        table.save()
        return redirect('/table/')
    return render(request,"table_edit.html",context)

def delete_table(request,id):
    table=Table.objects.get(id=id)
    table.delete()
    return redirect('/table/')

def order_list(request):
    order=Order.objects.all()
    context={'order':order}
    return render(request,"order.html",context)

def add_order(request):
    customers=Customer.objects.all()
    tables=Table.objects.all()
    menus=MenuItem.objects.all()
    context={'customers':customers,'tables':tables,'menus':menus}
    if request.method == "POST":
        customer_id=request.POST.get("customer")
        table_id=request.POST.get("table")
        menu_ids=request.POST.getlist("menu_item")
        quantities=request.POST.getlist("quantity")
        status=request.POST.get("status")
        customer=Customer.objects.get(id=customer_id)
        table=Table.objects.get(id=table_id)




        total=Decimal("0.00")
        order=Order.objects.create(
            customer=customer,
            table=table,
            total=total,
            status=status,     
        )
        for menu_id,qty in zip(menu_ids,quantities):
            menu_item=MenuItem.objects.get(id=menu_id)
            quantity=int(qty)

            if quantity<=0:
                order.delete()
                messages.error(request,"Quantity must be greater than zero")
                return render(request,"order_form.html",context)
            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=quantity,
            )
            subtotal=menu_item.price*quantity
            total+=subtotal
        order.total=total
        order.save()
        return redirect('/order/')
    return render(request,"order_form.html",context)
def edit_order(request, id):
    order = Order.objects.get(id=id)

    customers = Customer.objects.all()
    tables = Table.objects.all()
    menus = MenuItem.objects.all()
    items = order.orderitem_set.all()

    context = {
        'order': order,
        'items': items,
        'customers': customers,
        'tables': tables,
        'menus': menus,
    }

    if request.method == "POST":
        customer_id = request.POST.get("customer")
        table_id = request.POST.get("table")
        status = request.POST.get("status")

        menu_ids = request.POST.getlist("menu_item")
        quantities = request.POST.getlist("quantity")

        if not menu_ids or len(menu_ids) != len(quantities):
            messages.error(request, "Please select menu items and quantities.")
            return render(request, "order_edit.html", context)

        selected_items = []
        total = Decimal("0.00")

        # Validate items and calculate the total first
        for menu_id, qty in zip(menu_ids, quantities):
            try:
                menu_item = MenuItem.objects.get(id=menu_id)
                quantity = int(qty)
            except (MenuItem.DoesNotExist, ValueError):
                messages.error(request, "Invalid menu item or quantity.")
                return render(request, "order_edit.html", context)

            if quantity <= 0:
                messages.error(
                    request,
                    "Quantity must be greater than zero."
                )
                return render(request, "order_edit.html", context)

            selected_items.append((menu_item, quantity))

            subtotal = menu_item.price * quantity
            total += subtotal

        # Update the existing order
        order.customer = Customer.objects.get(id=customer_id)
        order.table = Table.objects.get(id=table_id)
        order.status = status
        order.total = total
        order.save()

        # Replace the old order items with the submitted items
        order.orderitem_set.all().delete()

        for menu_item, quantity in selected_items:
            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=quantity,
            )

        messages.success(request, "Order updated successfully.")
        return redirect('/order/')

    return render(request, "order_edit.html", context)