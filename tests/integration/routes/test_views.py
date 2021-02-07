from unittest.mock import patch
import json
import os

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from routes.forms import RouteSearchForm
from vehicles.models import Vehicle

User = get_user_model()


class RouteSearchViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', email='test@test.fr', password='alJpi.*87d-'
        )

    def test_route_search_view_returns_success_status(self):
        self.client.force_login(self.user)
        url = reverse('routes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('routes/search.html')
        self.assertTrue(isinstance(response.context['form'], RouteSearchForm))

    def test_route_search_view_cannot_be_accessed_without_auth(self):
        url = reverse('routes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['Location'], f"{reverse('login')}?next={url}"
        )


class RouteResultViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', email='test@test.fr', password='alJpi.*87d-'
        )
        cls.vehicle = Vehicle.objects.create(
            name='Test Vehicle',
            gross_weight=10000,
            height=4.0,
            width=6.0,
            length=20.0,
            tunnel_category='B',
            truck_type='S',
            owner=cls.user,
        )
        cls.route = None
        with open('tests/fake_route.json') as jsonfile:
            cls.route = json.load(jsonfile)

    @patch('routes.views.search_route')
    def test_route_result_view_cannot_be_reached_without_auth(
        self, mock_search_route
    ):
        mock_search_route.return_value = self.route
        url = reverse('routes:result')
        response = self.client.get(
            url,
            data={
                'vehicle': self.vehicle.id,
                'origin': '7.0000000,4.0000000',
                'destination': '8.0000000,5.0000000',
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['Location'].split('?')[0],
            reverse('login'),
        )

    @patch('routes.views.search_route')
    def test_route_result_view_sends_valid_data_with_get(
        self, mock_search_route
    ):
        mock_search_route.return_value = self.route
        self.client.force_login(self.user)
        url = reverse('routes:result')
        response = self.client.get(
            url,
            data={
                'vehicle': self.vehicle.id,
                'origin': 'Paris',
                'destination': 'Bordeaux',
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('routes/result.html')
        self.assertEqual(response.context['route'], json.dumps(self.route))
        self.assertEqual(
            response.context['here_key'], os.getenv('HERE_JS_API_KEY')
        )
