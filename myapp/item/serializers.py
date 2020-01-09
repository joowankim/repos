from rest_framework import serializers
from .models import Ingredient, Item, Included
#
# class IngredientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ingredient
#         fields = '__all__'
#
# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Item
#         fields = '__all__'
#
# class IncludedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Included
#         fields = '__all__'

# class ProductsSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     imgUrl = serializers.CharField(max_length=512)
#     name = serializers.CharField(max_length=256)
#     price = serializers.IntegerField()
#     ingredients = serializers.CharField(max_length=512)
#     monthlySales = serializers.IntegerField()

class ProductsSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField('get_imgUrl')
    class Meta:
        model = Item
        fields = ('id', 'imgUrl', 'name', 'price', 'ingredients', 'monthlySales')
    def get_imgUrl(self, obj):
        return obj.image

class ProductDetailSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField('get_imgUrl')
    class Meta:
        model = Item
        fields = ('id', 'imgUrl', 'name', 'price', 'gender', 'category', 'ingredients', 'monthlySales')
    def get_imgUrl(self, obj):
        return obj.image

class RecommProductsSerializer(serializers.ModelSerializer):
    imgUrl = serializers.SerializerMethodField('get_imgUrl')
    class Meta:
        model = Item
        fields = ('id', 'imgUrl', 'name', 'price')
    def get_imgUrl(self, obj):
        return obj.thumb