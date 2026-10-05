from store.models import *
from faker import Faker
fake=Faker()
for i in range(10): 
    Customer.objects.create(
        name=fake.name(),
        email=fake.email(),
        phone=str(fake.random_number(digits=10, fix_len=True)),
        address=fake.street_address()
    )
