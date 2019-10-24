from django.test import TestCase
from categories.models import Category

# Create your tests here.
class CategoryTest(TestCase):
    """category model test"""

    def setUp(self):
        Category.objects.create(name='빵')
        Category.objects.create(name='케이크')
        Category.objects.create(name='디저트')

    def test_get_all_categories(self):
        categories = Category.objects.all()
        self.assertEqual(len(categories), 3)

    def test_get_single_category(self):
        category = Category.objects.get(pk=1)
        self.assertEqual(category.id, 1)
        self.assertEqual(category.name, '빵')
        self.assertIsNotNone(category.created_at)
        self.assertIsNotNone(category.updated_at)

    def test_update_category(self):
        expected_name = 'TEST'
        category = Category.objects.get(pk=1)
        category.name = expected_name
        category.save()
        
        updated = Category.objects.get(pk=category.id)
        self.assertEqual(updated.name, expected_name)
        self.assertEqual(category.created_at, updated.created_at)
        self.assertLessEqual(category.updated_at, updated.updated_at)

    def test_delete_category(self):
        category = Category.objects.get(pk=1)
        category.delete()

        categories = Category.objects.all()
        self.assertEqual(len(categories), 2)

    # 추후 유저이름으로 카테고리를 찾는 메소드 필요
    
    def tearDown(self):
        queryset = Category.objects.all()
        queryset.delete()