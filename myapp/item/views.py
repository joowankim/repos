from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Item
from .serializers import ProductsSerializer, ProductDetailSerializer, RecommProductsSerializer

def empty_view():
    content = {'please type <skin_type> on URL': 'nothing to see here'}
    return Response(content, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def products_list(request):
    if request.method == 'GET':
        skin_type = request.GET.get('skin_type')
        if not skin_type:
            return empty_view()
        category = request.GET.get('category')
        exclude_ingredient = request.GET.get('exclude_ingredient')
        include_ingredient = request.GET.get('include_ingredient')

        kwargs = {}
        exclude = {}
        if category:
            kwargs['category'] = category
        if include_ingredient:
            kwargs['ingredients__name'] = include_ingredient
        if exclude_ingredient:
            exclude['ingredients__name'] = exclude_ingredient

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
        if not skin_type:
            return empty_view()
        product_detail = Item.objects.get(id=id)
        recomms = Item.objects.filter(category=product_detail.category).order_by('-'+skin_type, 'price')[:3]

        product_serializer = ProductDetailSerializer(product_detail)
        recomms_serializer = RecommProductsSerializer(recomms, many=True)
        return Response([product_serializer.data] + recomms_serializer.data)