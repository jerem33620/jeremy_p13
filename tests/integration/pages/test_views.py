from django.test import TestCase
from django.urls import reverse


class PagesViewsTests(TestCase):
    def test_home_view_is_correctly_configured(self):
        url = reverse('pages:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('pages/home.html')