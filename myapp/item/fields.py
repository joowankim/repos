from rest_framework import serializers

class IngredientsField(serializers.Field):
    '''
    Item model의 ingredients에 대한 Custom Field
    성분 리스트를 하나의 문자열로 바꿔주기 위해 구현
    '''
    def to_representation(self, value):
        return ','.join([ingredient.name for ingredient in value.all()])