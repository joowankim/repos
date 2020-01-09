from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Ingredient, Item, Included
from .serializers import ProductsSerializer, ProductDetailSerializer, RecommProductsSerializer
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

@api_view(['GET'])
def products_list(request):
    if request.method == 'GET':
        skin_type = request.GET.get('skin_type')
        category = request.GET.get('category')
        exclude_ingredient = request.GET.get('exclude_ingredient')
        include_ingredient = request.GET.get('include_ingredient')

        kwargs = {}
        exclude = {}
        if category:
            kwargs['category'] = category
        if include_ingredient:
            kwargs['ingredients__contains'] = include_ingredient
        if exclude_ingredient:
            exclude['ingredients__contains'] = exclude_ingredient

        queryset = Item.objects\
            .filter(**kwargs)\
            .exclude(**exclude)\
            .order_by('-'+skin_type, 'price')

        paginator = PageNumberPagination()
        paginator.page_size = 50

        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = ProductsSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, id):
    if request.method == 'GET':
        skin_type = request.GET.get('skin_type')
        product_detail = Item.objects.get(id=id)
        recomms = Item.objects.all().order_by('-'+skin_type, 'price')[:3]

        product_serializer = ProductDetailSerializer(product_detail)
        recomms_serializer = RecommProductsSerializer(recomms, many=True)
        return Response([product_serializer.data] + recomms_serializer.data)