import json
from rest_framework import status
from django.test import TestCase, Client, tag
from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer

client = Client()

# 추후 정책에 따라 테스트 코드 변경이 필요함.
# 1. 유저가 CRUD 가능하다면, POST, PUT, DELETE 시 authenticate 테스트 필요
# 2. 유저는 GET만, 관리자가 CRUD 시, user authenticate, manager authenticate 테스트 필요

class IngredientListCreateViewTest(TestCase):
    def setUp(self):
        Ingredient.objects.create(name='밀가루')
        Ingredient.objects.create(name='설탕')
        Ingredient.objects.create(name='소금')
    
    def test_get_ingredients(self):
        response = client.get("/api/ingredients/")
        ingredients = Ingredient.objects.all()
        serializer = IngredientSerializer(ingredients, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_ingredient(self):
        insert_data = {
            'name': '우유'
        }
        response = client.post(
            '/api/ingredients/', 
            data=json.dumps(insert_data),
            content_type='application/json'
        )
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in data)
        self.assertEqual(data['name'], insert_data['name'])

    def test_create_category_bad_request_empty_value(self):
        response = client.post(
            '/api/ingredients/', 
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_category_bad_request_duplicate_name(self):
        insert_data = {
            'name': '밀가루'
        }
        response = client.post(
            '/api/ingredients/', 
            data=json.dumps(insert_data),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        queryset = Ingredient.objects.all()
        queryset.delete()

class IngredientRetrieveUpdateDestroyAPITest(TestCase):
    def setUp(self):
        Ingredient.objects.create(name='밀가루')
        Ingredient.objects.create(name='초콜릿')
        
    def test_get_single_ingrdient(self):
        response = client.get("/api/ingredients/1/")
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('id' in data)
        self.assertEqual(data['name'], '밀가루')

    def test_get_single_ingrdient_not_found(self):
        response = client.get("/api/ingredients/3/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_ingrdient(self):
        ingrdient = Ingredient.objects.get(pk=1)

        updated_info = {
            'name': 'test',
        }
        response = client.put(
            "/api/ingredients/1/",
            data=json.dumps(updated_info),
            content_type='application/json'
        )
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('id' in data)
        self.assertEqual(data['name'], updated_info['name'])

    def test_update_ingrdient_bad_request_empty_value(self): 
        response = client.put(
            "/api/ingredients/1/",
            data=json.dumps({ }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_ingrdient_bad_request_duplicated_value(self):
        updated_info = {
            'name': '초콜릿',
        } 
        response = client.put(
            "/api/ingredients/1/",
            data=json.dumps({ }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_update_ingredient_not_found(self):
        updated_info = {
            'name': 'test',
        }
        response = client.put(
            "/api/ingredients/3/",
            data=json.dumps(updated_info),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

    def test_delete_ingredient(self):
        response = client.delete("/api/ingredients/1/")
        ingredients = Ingredient.objects.all()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(ingredients), 1)

    def test_delete_ingredient_not_found(self):
        response = client.delete("/api/ingredients/3/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        queryset = Ingredient.objects.all()
        queryset.delete()