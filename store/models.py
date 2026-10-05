from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Table(models.Model):
    table_number = models.IntegerField()
    capacity = models.IntegerField()

    status = models.CharField(
        max_length=20,
        choices=[
            ("Available", "Available"),
            ("Occupied", "Occupied"),
            ("Reserved", "Reserved"),
        ],
        default="Available",
    )


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=[
            ("Pending", "Pending"),
            ("Preparing", "Preparing"),
            ("Completed", "Completed"),
            ("Cancelled", "Cancelled"),
        ],
        default="Pending",
    )

    created_at = models.DateTimeField(auto_now_add=True)