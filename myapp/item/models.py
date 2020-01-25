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
    # 각 피부 타입에 대한 상품의 점수를 미리 계산하여 점수 필드를 구성
    oily = models.IntegerField()
    dry = models.IntegerField()
    sensitive = models.IntegerField()
    # 이미지의 종류에 따른 주소를 각각 저장
    full = models.CharField(max_length=512)
    thumb = models.CharField(max_length=512)

class Included(models.Model):
    '''
    성분과 상품 사이의 ManyToManyField에 대한 relationship
    '''
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)


