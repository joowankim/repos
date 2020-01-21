from rest_framework import serializers

class IngredientsField(serializers.Field):
    def to_representation(self, value):
        return ','.join([ingredient.name for ingredient in value.all()])