from django.test import TestCase
from django.urls import resolve

from bridges.views import BridgeCreate


class URLResolutionTests(TestCase):
    def test_creates_resolves_to_right_view(self):
        view = resolve('/bridges/')
        self.assertEqual(view.url_name, 'create')
        self.assertEqual(view.namespace, 'bridges')
        self.assertEqual(view.func.view_class, BridgeCreate)