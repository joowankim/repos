from rest_framework import serializers
from .models import Ingredient, Item, Included

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class IncludedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Included
        fields = '__all__'