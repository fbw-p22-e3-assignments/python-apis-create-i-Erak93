from django.db import models

# Create your models here.


class Product(models.Model):
    product_name=models.CharField(max_length=200)
    product_id=models.AutoField(primary_key=True)
    product_category=models.CharField(max_length=200)
    product_description=models.CharField(max_length=2000)
    product_image_url=models.CharField(max_length=500)
    product_prize=models.IntegerField