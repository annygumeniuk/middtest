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

class MainViewTest(TestCase):
    def setUp(self):
        # Create dummy recipes
        for i in range(10):
            Recipe.objects.create(name=f"Recipe {i}")

        # Set up the request factory
        self.factory = RequestFactory()

    def test_main(self):
        # Create a request
        request = self.factory.get('/')

        # Call the main function
        response = main(request)

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the rendered template
        self.assertTemplateUsed(response, 'main.html')

        # Check the context data
        recipes = response.context['recipes']
        self.assertEqual(len(recipes), 5)
        self.assertTrue(all(isinstance(recipe, Recipe) for recipe in recipes))