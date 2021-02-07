from django.test import TestCase
from django.urls import resolve

from users import views
from django.contrib.auth import views as auth_views


class URLResolutionTests(TestCase):
    def test_signup_resolves_to_right_view(self):
        view = resolve('/users/signup/')
        self.assertEqual(view.url_name, 'signup')
        self.assertEqual(view.namespace, 'users')
        self.assertEqual(view.func, views.signup)

    def test_profile_resolves_to_right_view(self):
        view = resolve('/users/profile/')
        self.assertEqual(view.url_name, 'profile')
        self.assertEqual(view.namespace, 'users')
        self.assertEqual(view.func, views.profile)

    def test_avatar_change_resolves_to_right_view(self):
        view = resolve('/users/avatar/')
        self.assertEqual(view.url_name, 'avatar_change')
        self.assertEqual(view.namespace, 'users')
        self.assertEqual(view.func, views.avatar_change)

    def test_login_resolves_to_right_view(self):
        view = resolve('/users/login/')
        self.assertEqual(view.url_name, 'login')
        self.assertEqual(view.namespace, '')
        self.assertEqual(view.func.view_class, auth_views.LoginView)

    def test_logout_resolves_to_right_view(self):
        view = resolve('/users/logout/')
        self.assertEqual(view.url_name, 'logout')
        self.assertEqual(view.namespace, '')
        self.assertEqual(view.func.view_class, auth_views.LogoutView)

    def test_password_reset_resolves_to_right_view(self):
        view = resolve('/users/password_reset/')
        self.assertEqual(view.url_name, 'password_reset')
        self.assertEqual(view.namespace, '')
        self.assertEqual(view.func.view_class, auth_views.PasswordResetView)

    def test_password_reset_done_resolves_to_right_view(self):
        view = resolve('/users/password_reset/done/')
        self.assertEqual(view.url_name, 'password_reset_done')
        self.assertEqual(view.namespace, '')
        self.assertEqual(
            view.func.view_class, auth_views.PasswordResetDoneView
        )

    def test_password_reset_confirm_resolves_to_right_view(self):
        view = resolve('/users/reset/asdf1234/asdf1234/')
        self.assertEqual(view.url_name, 'password_reset_confirm')
        self.assertEqual(view.namespace, '')
        self.assertEqual(
            view.func.view_class, auth_views.PasswordResetConfirmView
        )

    def test_password_reset_complete_resolves_to_right_view(self):
        view = resolve('/users/reset/done/')
        self.assertEqual(view.url_name, 'password_reset_complete')
        self.assertEqual(view.namespace, '')
        self.assertEqual(
            view.func.view_class, auth_views.PasswordResetCompleteView
        )
