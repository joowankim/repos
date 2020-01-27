from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from django.db.models import Count

from .models import Item
from .serializers import ProductsSerializer, ProductDetailSerializer, RecommProductsSerializer


def empty_view():
    '''
    skin_type을 제대로 입력하지 않은 경우 404에러를 보내기 위한 함수
    :return: status 404
    '''
    content = {'please type right <skin_type> on URL': 'nothing to see here',
               'skin types': 'oily, dry, sensitive'}
    return Response(content, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def products_list(request):
    if request.method == 'GET':
        skin_type = request.GET.get('skin_type')
        if not skin_type or not skin_type in ['oily', 'dry', 'sensitive']:
            return empty_view()
        category = request.GET.get('category')
        exclude_ingredient = request.GET.get('exclude_ingredient')
        include_ingredient = request.GET.get('include_ingredient')

        kwargs = {}     # filter의 조건 ( 카테고리, 필수 포함 성분들 )
        exclude = {}    # exclude의 조건 ( 배제 대상 성분들 )
        having = 1      # include_ingredient의 개수
        if category:
            kwargs['category'] = category
        if include_ingredient:
            kwargs['ingredients__in'] = list(include_ingredient.split(','))
            having = len(kwargs['ingredients__in'])
        if exclude_ingredient:
            exclude['ingredients__in'] = list(exclude_ingredient.split(','))

        queryset = Item.objects\
            .filter(**kwargs)\
            .exclude(**exclude)\
            .order_by('-'+skin_type, 'price')\
            .annotate(count=Count('id'))\
            .filter(count=having)   # 같은 id의 개수가 필수 성분 개수와 같을 때, include_ingredient 조건 충족

        paginator = PageNumberPagination()  # pagination
        paginator.page_size = 50            # 50개마다

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
        if not skin_type or not skin_type in ['oily', 'dry', 'sensitive']:
            return empty_view()
        product_detail = Item.objects.get(id=id)
        recomms = Item.objects.filter(category=product_detail.category).order_by('-'+skin_type, 'price')[:3]

        product_serializer = ProductDetailSerializer(product_detail)        # 검색한 상품의 정보
        recomms_serializer = RecommProductsSerializer(recomms, many=True)   # 추천된 상품 3개의 정보
        return Response([product_serializer.data] + recomms_serializer.data)