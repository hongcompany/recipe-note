import json
from rest_framework import status
from django.test import TestCase, Client, tag
from categories.models import Category
from categories.serializers import CategorySerializer

client = Client()

class CategoryListAPITest(TestCase):
    def setUp(self):
        Category.objects.create(name='빵')
        Category.objects.create(name='케이크')
        Category.objects.create(name='디저트')
    
    def test_get_categories_without_owner(self):
        response = client.get("/api/categories/")
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    @tag("owner")
    def test_get_categories_with_owner(self):
        # 유저 권한이 있으면, owner 정보 필요
        pass

    @tag("owner")
    def test_get_categories_by_owner(self):
        # owner 정보 필요
        pass

    def tearDown(self):
        queryset = Category.objects.all()
        queryset.delete()


class CategoryCreateAPITest(TestCase):
    # 추후 authenticate 될 때, 안될 때 나눌 필요가 있음.
    def setUp(self):
        pass

    def test_create_category_default(self):
        insert_data = {
            'name': '빵',
        }
        
        response = client.post(
            '/api/categories/', 
            data=json.dumps(insert_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        data = response.data
        self.assertTrue('id' in data)
        self.assertTrue('created_at' in data)
        self.assertTrue('updated_at' in data)
        self.assertEqual(data['name'], insert_data['name'])
        self.assertEqual(data['is_deleted'], False)

    def test_create_category_settings(self):
        insert_data = {
            'name': '빵',
            'is_deleted': True
        }
        # 추후 authenticate 될 때, 안될 때 나눌 필요가 있음.
        response = client.post(
            '/api/categories/', 
            data=json.dumps(insert_data),
            content_type='application/json'
        )
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in data)
        self.assertTrue('created_at' in data)
        self.assertTrue('updated_at' in data)
        self.assertEqual(data['name'], insert_data['name'])
        self.assertEqual(data['is_deleted'], True)

    def test_create_category_bad_request(self):
        # 추후 authenticate 될 때, 안될 때 나눌 필요가 있음.
        response = client.post(
            '/api/categories/', 
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        queryset = Category.objects.all()
        queryset.delete()


class CategoryRetrieveUpdateDestroyAPITest(TestCase):
    def setUp(self):
        Category.objects.create(name='빵')

    def test_get_single_category(self):
        response = client.get("/api/categories/1/")
        data = response.data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('id' in data)
        self.assertTrue('created_at' in data)
        self.assertTrue('updated_at' in data)
        self.assertEqual(data['name'], '빵')
        self.assertEqual(data['is_deleted'], False)

    def test_get_single_category_not_found(self):
        response = client.get("/api/categories/2/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_category(self):
        category = Category.objects.get(pk=1)
        updated_at_after = category.updated_at

        updated_info = {
            'name': 'test',
            'is_deleted': True
        }

        response = client.put(
            "/api/categories/1/",
            data=json.dumps(updated_info),
            content_type='application/json'
        )
        data = response.data

        category = Category.objects.get(pk=1)
        updated_at_before = category.updated_at

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('id' in data)
        self.assertTrue('created_at' in data)
        self.assertLess(updated_at_after, updated_at_before)
        self.assertEqual(data['name'], 'test')
        self.assertEqual(data['is_deleted'], True)

    def test_update_category_bad_request(self): 
        response = client.put(
            "/api/categories/1/",
            data=json.dumps({ }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_update_category_not_found(self):
        updated_info = {
            'name': 'test',
            'is_deleted': True
        }

        response = client.put(
            "/api/categories/2/",
            data=json.dumps(updated_info),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        

    def test_delete_category(self):
        response = client.delete("/api/categories/1/")
        categories = Category.objects.all()

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(categories), 0)

    def test_delete_category_not_found(self):
        response = client.delete("/api/categories/2/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self):
        queryset = Category.objects.all()
        queryset.delete()