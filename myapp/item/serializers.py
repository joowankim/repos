from rest_framework import serializers
from .models import Ingredient, Item, Included
from .fields import IngredientsField

class ProductsSerializer(serializers.ModelSerializer):
    '''
    상품 목록에 대한 Serializer
    full_size 이미지의 주소에 대한 이름을 'imgUrl'로 교체
    ingredients의 출력을 문자열로 재구성
    '''
    imgUrl = serializers.SerializerMethodField('get_imgUrl')
    ingredients = IngredientsField()
    class Meta:
        model = Item
        fields = ('id', 'imgUrl', 'name', 'price', 'ingredients', 'monthlySales')
    def get_imgUrl(self, obj):
        return obj.full

class ProductDetailSerializer(serializers.ModelSerializer):
    '''
    검색된 상품에 대한 Serializer
    full_size 이미지의 주소에 대한 이름을 'imgUrl'로 교체
    ingredients의 출력을 문자열로 재구성
    '''
    imgUrl = serializers.SerializerMethodField('get_imgUrl')
    ingredients = IngredientsField()
    class Meta:
        model = Item
        fields = ('id', 'imgUrl', 'name', 'price', 'gender', 'category', 'ingredients', 'monthlySales')
    def get_imgUrl(self, obj):
        return obj.full

class RecommProductsSerializer(serializers.ModelSerializer):
    '''
    추천 상품에 대한 Serializer
    thumbnail 이미지의 주소에 대한 이름을 'imgUrl'로 교체
    '''
    imgUrl = serializers.SerializerMethodField('get_imgUrl')
    class Meta:
        model = Item
        fields = ('id', 'imgUrl', 'name', 'price')
    def get_imgUrl(self, obj):
        return obj.thumb