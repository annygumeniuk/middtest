from multiprocessing.connection import Client

from django.test import TestCase, RequestFactory
from django.urls import reverse
from .models import Recipe, Category
from .views import main

class HomeViewTest(TestCase):
    def test_home_view(self):
        url = reverse('main')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

class RecipeModelTest(TestCase):
    def setUp(self):
        # Create a Category
        self.category = Category.objects.create(name='Test Category')

        # Create a Recipe
        self.recipe = Recipe.objects.create(
            title='Test Recipe',
            description='Test description',
            instructions='Test instructions',
            ingredients='Test ingredients',
            category=self.category
        )

    def test_recipe_model(self):
        # Retrieve the Recipe from the database
        recipe = Recipe.objects.get(title='Test Recipe')

        # Verify the field values
        self.assertEqual(recipe.title, 'Test Recipe')
        self.assertEqual(recipe.description, 'Test description')
        self.assertEqual(recipe.instructions, 'Test instructions')
        self.assertEqual(recipe.ingredients, 'Test ingredients')
        self.assertEqual(recipe.category, self.category)

    def test_recipe_str_method(self):
        # Retrieve the Recipe from the database
        recipe = Recipe.objects.get(title='Test Recipe')

        # Verify the string representation
        self.assertEqual(str(recipe), 'Test Recipe')

class CategoryModelTest(TestCase):
    def setUp(self):
        # Create a Category
        self.category = Category.objects.create(name='Test Category')

    def test_category_model(self):
        # Retrieve the Category from the database
        category = Category.objects.get(name='Test Category')

        # Verify the field values
        self.assertEqual(category.name, 'Test Category')

    def test_category_str_method(self):
        # Retrieve the Category from the database
        category = Category.objects.get(name='Test Category')

        # Verify the string representation
        self.assertEqual(str(category), 'Test Category')