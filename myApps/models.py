import uuid

from django.db import models


def gen_unique_path(instance, filename):
    ext = filename.split('.')[-1]
    newfilename = f'{uuid.uuid4()}.{ext}'
    return f'products/{newfilename}'


# Create your models here.
# MVT-- model view template

CATEGORIES = [
    ('Breakfast', 'Breakfast'),
    ('Lunch', 'Lunch'),
    ('Dinner', 'Dinner'),

]


class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    for_sale = models.BooleanField(default=True)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    pic = models.ImageField(upload_to=gen_unique_path, default='products/default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

# run migrations
# python manage.py makemigrations
# python manage.py migrate

# python manage.py createsuperuser
# Pyalo 123123
