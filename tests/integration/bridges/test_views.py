from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from bridges.models import Bridge, BridgeUpdate
from bridges.forms import BridgeCreationForm

User = get_user_model()


class BridgeViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', email='test@test.fr', password='apJdeZ*k.#1'
        )

    def test_bridge_create_view_with_get_displays_form(self):
        self.client.force_login(self.user)
        url = reverse('bridges:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('bridges/register.html')
        self.assertTrue(
            isinstance(response.context['form'], BridgeCreationForm)
        )

    def test_bridge_create_view_posts_valid_data_and_creates_bridge(
        self,
    ):
        self.client.force_login(self.user)
        url = reverse('bridges:create')
        response = self.client.post(
            url,
            data={
                'height': '10.0',
                'width': '10.0',
                'latitude': '7.0',
                'longitude': '4.0',
            },
            follow=False,
        )
        bridge = Bridge.objects.first()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(bridge.latitude, Decimal('7.0'))
        self.assertEqual(bridge.longitude, Decimal('4.0'))
        self.assertEqual(response['Location'], url)

    def test_bridge_create_view_posts_invalid_data_and_does_not_create_bridge(
        self,
    ):
        self.client.force_login(self.user)
        url = reverse('bridges:create')
        response = self.client.post(
            url,
            data={
                'height': 'abc',
                'width': '10.0',
                'latitude': '7.0',
                'longitude': '4.0',
            },
            follow=False,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('bridges.register.html')
        self.assertTrue(response.context['form'].has_error('height'))
        self.assertFalse(response.context['form'].has_error('width'))

    def test_bridge_creation_view_cannot_be_reached_without_auth(self):
        url = reverse('bridges:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['Location'], f"{reverse('login')}?next={url}"
        )
