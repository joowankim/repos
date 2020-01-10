from django.db import models

class Ingredient(models.Model):
    name = models.CharField(primary_key=True, max_length=200)
    oily = models.IntegerField()
    dry = models.IntegerField()
    sensitive = models.IntegerField()

    def __unicode__(self):
        return '{}'.format(self.name)

class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    gender = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='Included',
        through_fields=('item', 'ingredient'),
        related_name='ingredients'
    )
    monthlySales = models.IntegerField()
    oily = models.IntegerField()
    dry = models.IntegerField()
    sensitive = models.IntegerField()
    full = models.CharField(max_length=512)
    thumb = models.CharField(max_length=512)

class Included(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)


