from django.db import models

# Create your models here.
# class Item(models.Model):
#     name = models.CharField(max_length=32)
#     quantity = models.IntegerField()

class Ingredient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    oily = models.IntegerField()
    dry = models.IntegerField()
    sensitive = models.IntegerField()

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    imageId = models.TextField()
    name = models.TextField()
    price = models.IntegerField()
    gender = models.TextField()
    category = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    monthlySales = models.IntegerField()



