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
    ingredients = models.TextField()
    ingredient_ids = models.ManyToManyField(
        Ingredient,
        through='Included',
        through_fields=('item', 'ingredient'),
    )
    monthlySales = models.IntegerField()
    oily = models.IntegerField()
    dry = models.IntegerField()
    sensitive = models.IntegerField()

class Included(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)



