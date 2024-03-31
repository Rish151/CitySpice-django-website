import datetime
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=30 , unique=True)
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=400)
    product_category = models.CharField(max_length=100)
    product_img = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    # images stored in media/images folder
    def __str__(self):
        return self.product_id
    # now Go at admin.py for registration of product

class Contact_Query(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.CharField(max_length=400)
    date_time = models.DateTimeField(("Date"), default=datetime.datetime.today)
    def __str__(self):
        return self.email
    
