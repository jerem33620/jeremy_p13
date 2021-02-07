from django.test import TestCase
from django.urls import resolve

from pages.views import HomeView


class URLResolutionTests(TestCase):
    def test_home_resolves_to_right_view(self):
        view = resolve('/')
        self.assertEqual(view.url_name, 'home')
        self.assertEqual(view.namespace, 'pages')
        self.assertEqual(view.func.view_class, HomeView)