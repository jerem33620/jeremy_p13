from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

from users.models import User
from users.forms import SignupForm, AvatarChangeForm


class UserSignupTests(TestCase):
    def test_signup_view_displays_signup_form(self):
        url = reverse('users:signup')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('signup.html')
        self.assertTrue(isinstance(response.context['form'], SignupForm))

    def test_signup_view_posts_valid_data_and_create_user(self):
        url = reverse('users:signup')
        response = self.client.post(
            url,
            data={
                'username': 'testuser',
                'email': 'test@test.fr',
                'password1': 'hglaIhlF.#2',
                'password2': 'hglaIhlF.#2',
            },
        )
        user = User.objects.get(username='testuser')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], reverse('pages:home'))
        self.assertEqual(user.email, 'test@test.fr')

    def test_signup_view_posts_invalid_email(self):
        url = reverse('users:signup')
        response = self.client.post(
            url,
            data={
                'username': 'testuser',
                'email': 'test',
                'password1': 'hglaIhlF.#2',
                'password2': 'hglaIhlF.#2',
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].has_error('email'))

    def test_signup_view_posts_simple_passwords(self):
        url = reverse('users:signup')
        response = self.client.post(
            url,
            data={
                'username': 'testuser',
                'email': 'test@test.fr',
                'password1': '1234',
                'password2': '1234',
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].has_error('password2'))

    def test_signup_view_posts_non_matching_passwords(self):
        url = reverse('users:signup')
        response = self.client.post(
            url,
            data={
                'username': 'testuser',
                'email': 'test@test.fr',
                'password1': 'hglaIhlF.#22',
                'password2': 'hglaIhlF.#33',
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].has_error('password2'))


class ProfileViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', email='test@test.fr', password='hglaIhlF.#22'
        )

    def test_profile_view_cannot_be_reached_without_auth(self):
        url = reverse('users:profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['Location'], f"{reverse('login')}?next={url}"
        )

    def test_profile_view_displays_page_when_authenticated(self):
        self.client.force_login(self.user)
        url = reverse('users:profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('account.html')
        self.assertEqual(response.context['user'], self.user)

    def test_avatar_change_view_cannot_be_reached_without_auth(self):
        url = reverse('users:avatar_change')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response['Location'], f"{reverse('login')}?next={url}"
        )

    def test_avatar_change_view_displays_when_user_is_authenticated(self):
        self.client.force_login(self.user)
        url = reverse('users:avatar_change')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('avatar_change.html')
        self.assertTrue(isinstance(response.context['form'], AvatarChangeForm))
        self.assertEqual(
            (
                response.context['avatar_image_min_width'],
                response.context['avatar_image_min_height'],
            ),
            settings.USER_AVATAR_SIZE,
        )
