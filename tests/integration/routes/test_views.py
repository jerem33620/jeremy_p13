from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from routes.forms import RouteSearchForm

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
