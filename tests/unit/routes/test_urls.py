from django.test import TestCase
from django.urls import resolve

from routes.views import RouteSearchView, RouteResultView


class URLResolutionTests(TestCase):
    def test_search_resolves_to_right_view(self):
        view = resolve('/routes/')
        self.assertEqual(view.url_name, 'search')
        self.assertEqual(view.namespace, 'routes')
        self.assertEqual(view.func.view_class, RouteSearchView)

    def test_result_resolves_to_right_view(self):
        view = resolve('/routes/results/')
        self.assertEqual(view.url_name, 'result')
        self.assertEqual(view.namespace, 'routes')
        self.assertEqual(view.func.view_class, RouteResultView)