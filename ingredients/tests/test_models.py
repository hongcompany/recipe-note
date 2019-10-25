from django.test import TestCase

# Create your tests here.
from ingredients.models import Ingredient

# Create your tests here.
class IngredientTest(TestCase):
    """ingredient model test
    추후 정책 필요 현재는 다음 2가지로 생각중..
    1. 유저가 재료의 CRUD 다 할 수 있다.
    2. 관리자만 재료의 CRUD 가능, 일반 유저는 GET만 할 수 있다
    """

    def setUp(self):
        Ingredient.objects.create(name='밀가루')
        Ingredient.objects.create(name='설탕')
        Ingredient.objects.create(name='소금')

    def test_get_all_ingredients(self):
        ingredients = Ingredient.objects.all()
        self.assertEqual(len(ingredients), 3)

    def test_get_single_ingredient(self):
        ingredient = Ingredient.objects.get(pk=1)
        self.assertEqual(ingredient.id, 1)
        self.assertEqual(ingredient.name, '밀가루')

    def test_update_ingredient(self):
        expected_name = '초콜릿'
        ingredient = Ingredient.objects.get(pk=1)
        ingredient.name = expected_name
        ingredient.save()
        
        updated = Ingredient.objects.get(pk=ingredient.id)
        self.assertEqual(updated.name, expected_name)
        
    def test_delete_ingredient(self):
        ingredient = Ingredient.objects.get(pk=1)
        ingredient.delete()

        ingredients = Ingredient.objects.all()
        self.assertEqual(len(ingredients), 2)

    def tearDown(self):
        queryset = Ingredient.objects.all()
        queryset.delete()