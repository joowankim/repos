from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Ingredient, Item, Included
from .serializers import ProductsSerializer
# from .serializers import IngredientSerializer, ItemSerializer, IncludedSerializer
#
# @api_view(['GET', 'POST'])
# def ingredient_list(request):
#     if request.method == 'GET':
#         queryset = Ingredient.objects.all()
#         serializer = IngredientSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = IngredientSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATE)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def ingredient_detail(request, pk):
#     try:
#         ingredient = Ingredient.objects.get(pk=pk)
#     except Ingredient.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         # print(ingredient)
#         # print(type(ingredient))
#         serializer = IngredientSerializer(ingredient)
#         # print(serializer.data)
#         serializer.data["name"] = 'ssss'
#         # print(serializer.data)
#         # print(type(serializer.data))
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = IngredientSerializer(ingredient, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         ingredient.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        queryset = Item.objects.all()
        # print(queryset.query)
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def product_detail(request):
    if request.method == 'GET':
        queryset = Item.object.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)