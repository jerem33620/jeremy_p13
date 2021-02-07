from django.test import TestCase
from django.utils.translation import activate

from users.models import User


class UserModelTests(TestCase):
    def test_image_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            User._meta.get_field('avatar').verbose_name, 'user avatar'
        )

    def test_image_field_max_length(self):
        self.assertEqual(User._meta.get_field('avatar').max_length, 255)

    def test_image_field_can_be_blank(self):
        self.assertTrue(User._meta.get_field('avatar').blank)

    def test_image_field_cannot_be_null(self):
        self.assertFalse(User._meta.get_field('avatar').null)
