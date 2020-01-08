from django.db import models

# Create your models here.
# class Item(models.Model):
#     name = models.CharField(max_length=32)
#     quantity = models.IntegerField()

class Ingredient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    oily = models.IntegerField()
    dry = models.IntegerField()
    sensitive = models.IntegerField()

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    imageId = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    gender = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=512)
    ingredient_ids = models.ManyToManyField(
        Ingredient,
        through='Included',
        through_fields=('item', 'ingredient'),
    )
    monthlySales = models.IntegerField()
    oily = models.IntegerField()
    dry = models.IntegerField()
    sensitive = models.IntegerField()
    image = models.CharField(max_length=512)
    thumb = models.CharField(max_length=512)

class Included(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)


