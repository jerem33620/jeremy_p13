from django.test import TestCase
from django.utils.translation import activate

from vehicles.models import Vehicle
from users.models import User


class VehicleModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            email='testuser@test.fr',
            password='aPZzt56.#12D',
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

    def test_model_verbose_name(self):
        activate('en')
        self.assertEqual(
            Vehicle._meta.verbose_name,
            "vehicle",
        )
        activate('fr')
        self.assertEqual(
            Vehicle._meta.verbose_name,
            "véhicule",
        )

    def test_model_verbose_name_plural(self):
        activate('en')
        self.assertEqual(
            Vehicle._meta.verbose_name_plural,
            "vehicles",
        )
        activate('fr')
        self.assertEqual(
            Vehicle._meta.verbose_name_plural,
            "véhicules",
        )

    def test_name_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Vehicle._meta.get_field('name').verbose_name,
            "vehicle name",
        )
        activate('fr')
        self.assertEqual(
            Vehicle._meta.get_field('name').verbose_name,
            "nom du véhicule",
        )

    def test_name_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Vehicle._meta.get_field('name').verbose_name,
            "vehicle name",
        )
        activate('fr')
        self.assertEqual(
            Vehicle._meta.get_field('name').verbose_name,
            "nom du véhicule",
        )

    def test_name_field_max_length(self):
        self.assertEqual(
            Vehicle._meta.get_field('name').max_length,
            200,
        )

    def test_name_field_not_blank(self):
        self.assertFalse(Vehicle._meta.get_field('name').blank)

    def test_name_field_not_null(self):
        self.assertFalse(Vehicle._meta.get_field('name').null)

    def test_gross_weight_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Vehicle._meta.get_field('gross_weight').verbose_name,
            "vehicle gross weight",
        )
        activate('fr')
        self.assertEqual(
            Vehicle._meta.get_field('gross_weight').verbose_name,
            "poids du véhicule",
        )

    def test_gross_weight_field_blank(self):
        self.assertTrue(Vehicle._meta.get_field('gross_weight').blank)

    def test_gross_weight_field_not_null(self):
        self.assertTrue(Vehicle._meta.get_field('gross_weight').null)

    def test_height_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Vehicle._meta.get_field('height').verbose_name,
            "vehicle height",
        )
        activate('fr')
        self.assertEqual(
            Vehicle._meta.get_field('height').verbose_name,
            "hauteur du véhicule",
        )

    def test_height_field_max_digits(self):
        self.assertEqual(Vehicle._meta.get_field('height').max_digits, 4)

    def test_height_field_decimal_places(self):
        self.assertEqual(Vehicle._meta.get_field('height').decimal_places, 2)

    def test_height_field_blank(self):
        self.assertTrue(Vehicle._meta.get_field('height').blank)

    def test_height_field_not_null(self):
        self.assertTrue(Vehicle._meta.get_field('height').null)

    def test_width_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Vehicle._meta.get_field('width').verbose_name,
            "vehicle width",
        )
        activate('fr')
        self.assertEqual(
            Vehicle._meta.get_field('width').verbose_name,
            "largeur du véhicule",
        )

    def test_width_field_max_digits(self):
        self.assertEqual(Vehicle._meta.get_field('width').max_digits, 4)

    def test_width_field_decimal_places(self):
        self.assertEqual(Vehicle._meta.get_field('width').decimal_places, 2)

    def test_width_field_blank(self):
        self.assertTrue(Vehicle._meta.get_field('width').blank)

    def test_width_field_not_null(self):
        self.assertTrue(Vehicle._meta.get_field('width').null)

    def test_length_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Vehicle._meta.get_field('length').verbose_name,
            "vehicle length",
        )
        activate('fr')
        self.assertEqual(
            Vehicle._meta.get_field('length').verbose_name,
            "longueur du véhicule",
        )

    def test_length_field_max_digits(self):
        self.assertEqual(Vehicle._meta.get_field('length').max_digits, 4)

    def test_length_field_decimal_places(self):
        self.assertEqual(Vehicle._meta.get_field('length').decimal_places, 2)

    def test_length_field_blank(self):
        self.assertTrue(Vehicle._meta.get_field('length').blank)

    def test_length_field_not_null(self):
        self.assertTrue(Vehicle._meta.get_field('length').null)

    def test_tunnel_category_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Vehicle._meta.get_field('tunnel_category').verbose_name,
            "vehicle tunnel category",
        )
        activate('fr')
        self.assertEqual(
            Vehicle._meta.get_field('tunnel_category').verbose_name,
            "catégorie de tunnel du véhicule",
        )

    def test_tunnel_category_field_max_length(self):
        self.assertEqual(
            Vehicle._meta.get_field('tunnel_category').max_length, 1
        )

    def test_tunnel_category_field_blank(self):
        self.assertTrue(Vehicle._meta.get_field('tunnel_category').blank)

    def test_tunnel_category_field_not_null(self):
        self.assertFalse(Vehicle._meta.get_field('tunnel_category').null)

    def test_tunnel_category_field_english_choices(self):
        activate('en')
        choices = Vehicle._meta.get_field('tunnel_category').choices
        choice_letters = [letter for letter, description in choices]
        choice_descriptions = [description for letter, description in choices]
        self.assertEqual(len(choices), 5)
        self.assertIn('', choice_letters)
        self.assertIn('No tunnel category', choice_descriptions)
        for letter in "BCDE":
            self.assertIn(letter, choice_letters)
            self.assertIn(f"Tunnel category {letter}", choice_descriptions)

    def test_tunnel_category_field_french_choices(self):
        activate('fr')
        choices = Vehicle._meta.get_field('tunnel_category').choices
        choice_letters = [letter for letter, description in choices]
        choice_descriptions = [description for letter, description in choices]
        self.assertEqual(len(choices), 5)
        self.assertIn('', choice_letters)
        self.assertIn('Sans catégorie', choice_descriptions)
        for letter in "BCDE":
            self.assertIn(letter, choice_letters)
            self.assertIn(f"Catégorie {letter}", choice_descriptions)
