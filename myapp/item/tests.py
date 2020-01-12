from django.test import TestCase
from .models import Item
from .serializers import ProductsSerializer, ProductDetailSerializer, RecommProductsSerializer

class ProductListTest(TestCase):
    '''
        skin_type, category, page, exclude_ingredient, include_ingredient
    '''
    fixtures = ['item-data-refined.json', 'ingredient-data-refined.json']

    def test_no_skin_type(self):
        response = self.client.get('/products?page=2&include_ingredient=screw')
        self.assertNotEqual(response.status_code, 200)

    def test_no_category(self):
        response = self.client.get('/products?skin_type=oily&page=2')
        self.assertEqual(response.status_code, 200)

    def test_no_page(self):
        response = self.client.get('/products?skin_type=oily&category=suncare')
        self.assertEqual(response.status_code, 200)

    def test_no_include_ingredient(self):
        response = self.client.get(
            '/products?skin_type=oily&category=suncare&exclude_ingredient=aspect&page=2')
        self.assertEqual(response.status_code, 200)

    def test_no_exclude_ingredient(self):
        response = self.client.get(
            '/products?skin_type=oily&category=suncare&include_ingredient=aspect')
        self.assertEqual(response.status_code, 200)

    def test_page_count(self):
        response = self.client.get('/products?skin_type=oily')
        self.assertLessEqual(len(response.data['results']), 50)

    def test_products_keys(self):
        response = self.client.get('/products?skin_type=oily')
        answer = ['id', 'imgUrl', 'name', 'price', 'ingredients', 'monthlySales']
        self.assertListEqual(list(response.data['results'][0].keys()), answer)

    def test_products_order(self):
        response = self.client.get('/products?skin_type=oily')
        products = Item.objects.all().order_by('-oily', 'price')[:50]
        serializer = ProductsSerializer(products, many=True)
        for i in range(50):
            self.assertDictEqual(response.data['results'][i], serializer.data[i])

class ProductDetailTest(TestCase):
    '''
        id, skin_type
    '''
    fixtures = ['item-data-refined.json', 'ingredient-data-refined.json']

    def test_no_skin_type(self):
        response = self.client.get('/products/7?')
        self.assertNotEqual(response.status_code, 200)

    def test_no_id(self):
        response = self.client.get('/product/?skin_type=oily')
        self.assertNotEqual(response.status_code, 200)

    def test_product_detail(self):
        response = self.client.get('/product/7?skin_type=oily')
        answer = {
			"id": 7,
			"imgUrl": "https://grepp-programmers-challenges.s3.ap-northeast-2.amazonaws.com/2020-birdview/image/9e576c8f-0d49-4a02-a942-24263dbf86eb",
			"name": "오메가 옐로우 쉐이빙 브러쉬 [80265]",
			"price": 11180,
			"gender": "male",
			"category": "basemakeup",
			"ingredients": sorted([
				"sock",
				"faith",
				"coma",
				"performance",
				"automatic"
			]),
			"monthlySales": 1483
		}
        response.data[0]['ingredients'] = sorted(response.data[0]['ingredients'].split(','))
        self.assertDictEqual(response.data[0], answer)

    def test_recomms(self):
        response = self.client.get('/product/7?skin_type=oily')
        recomms = Item.objects.filter(category='basemakeup').order_by('-oily', 'price')[:3]
        recomms_serializer = RecommProductsSerializer(recomms, many=True)
        for i in range(1, 4):
            self.assertDictEqual(response.data[i], recomms_serializer.data[i-1])

    def test_product_detail_keys(self):
        response = self.client.get('/product/7?skin_type=oily')
        answer = ['id', 'imgUrl', 'name', 'price', 'gender', 'category', 'ingredients', 'monthlySales']
        self.assertListEqual(list(response.data[0].keys()), answer)

    def test_recomm_keys(self):
        response = self.client.get('/product/7?skin_type=oily')
        answer = ['id', 'imgUrl', 'name', 'price']
        self.assertListEqual(list(response.data[1].keys()), answer)