from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.translation import activate

from bridges.models import Bridge, BridgeManager, BridgeUpdate

User = get_user_model()


class BridgeModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', email='test@test.fr', password='ajHpq.p#2'
        )
        cls.bridge = Bridge.objects.create(
            height=10,
            width=10,
            latitude=Decimal('7.0'),
            longitude=Decimal('4.0'),
            latitude_north=Decimal('7.02'),
            latitude_south=Decimal('6.98'),
            longitude_west=Decimal('3.98'),
            longitude_east=Decimal('4.02'),
        )
        cls.bridge.contributors.add(cls.user)

    def test_height_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.get_field('height').verbose_name, 'bridge height'
        )

    def test_height_field_max_digits(self):
        self.assertEqual(Bridge._meta.get_field('height').max_digits, 4)

    def test_height_field_decimal_places(self):
        self.assertEqual(Bridge._meta.get_field('height').decimal_places, 2)

    def test_height_field_can_be_blank(self):
        self.assertTrue(Bridge._meta.get_field('height').blank)

    def test_height_field_can_be_null(self):
        self.assertTrue(Bridge._meta.get_field('height').null)

    def test_width_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.get_field('width').verbose_name, 'bridge width'
        )

    def test_width_field_max_digits(self):
        self.assertEqual(Bridge._meta.get_field('width').max_digits, 4)

    def test_width_field_decimal_places(self):
        self.assertEqual(Bridge._meta.get_field('width').decimal_places, 2)

    def test_width_field_can_be_blank(self):
        self.assertTrue(Bridge._meta.get_field('width').blank)

    def test_width_field_can_be_null(self):
        self.assertTrue(Bridge._meta.get_field('width').null)

    def test_latitude_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.get_field('latitude').verbose_name,
            'bounding box center latitude',
        )

    def test_latitude_field_max_digits(self):
        self.assertEqual(Bridge._meta.get_field('latitude').max_digits, 10)

    def test_latitude_field_decimal_places(self):
        self.assertEqual(Bridge._meta.get_field('latitude').decimal_places, 7)

    def test_latitude_field_cannot_be_blank(self):
        self.assertFalse(Bridge._meta.get_field('latitude').blank)

    def test_latitude_field_cannot_be_null(self):
        self.assertFalse(Bridge._meta.get_field('latitude').null)

    def test_longitude_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.get_field('longitude').verbose_name,
            'bounding box center longitude',
        )

    def test_longitude_field_max_digits(self):
        self.assertEqual(Bridge._meta.get_field('longitude').max_digits, 10)

    def test_longitude_field_decimal_places(self):
        self.assertEqual(Bridge._meta.get_field('longitude').decimal_places, 7)

    def test_longitude_field_cannot_be_blank(self):
        self.assertFalse(Bridge._meta.get_field('longitude').blank)

    def test_longitude_field_cannot_be_null(self):
        self.assertFalse(Bridge._meta.get_field('longitude').null)

    def test_latitude_north_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.get_field('latitude_north').verbose_name,
            'bounding box north latitude',
        )

    def test_latitude_north_field_max_digits(self):
        self.assertEqual(
            Bridge._meta.get_field('latitude_north').max_digits, 10
        )

    def test_latitude_north_field_decimal_places(self):
        self.assertEqual(
            Bridge._meta.get_field('latitude_north').decimal_places, 7
        )

    def test_latitude_north_field_cannot_be_blank(self):
        self.assertFalse(Bridge._meta.get_field('latitude_north').blank)

    def test_latitude_north_field_cannot_be_null(self):
        self.assertFalse(Bridge._meta.get_field('latitude_north').null)

    def test_latitude_south_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.get_field('latitude_south').verbose_name,
            'bounding box south latitude',
        )

    def test_latitude_south_field_max_digits(self):
        self.assertEqual(
            Bridge._meta.get_field('latitude_south').max_digits, 10
        )

    def test_latitude_south_field_decimal_places(self):
        self.assertEqual(
            Bridge._meta.get_field('latitude_south').decimal_places, 7
        )

    def test_latitude_south_field_cannot_be_blank(self):
        self.assertFalse(Bridge._meta.get_field('latitude_south').blank)

    def test_latitude_south_field_cannot_be_null(self):
        self.assertFalse(Bridge._meta.get_field('latitude_south').null)

    def test_longitude_west_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.get_field('longitude_west').verbose_name,
            'bounding box west longitude',
        )

    def test_longitude_west_field_max_digits(self):
        self.assertEqual(
            Bridge._meta.get_field('longitude_west').max_digits, 10
        )

    def test_longitude_west_field_decimal_places(self):
        self.assertEqual(
            Bridge._meta.get_field('longitude_west').decimal_places, 7
        )

    def test_longitude_west_field_cannot_be_blank(self):
        self.assertFalse(Bridge._meta.get_field('longitude_west').blank)

    def test_longitude_west_field_cannot_be_null(self):
        self.assertFalse(Bridge._meta.get_field('longitude_west').null)

    def test_longitude_east_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.get_field('longitude_east').verbose_name,
            'bounding box east longitude',
        )

    def test_longitude_east_field_max_digits(self):
        self.assertEqual(
            Bridge._meta.get_field('longitude_east').max_digits, 10
        )

    def test_longitude_east_field_decimal_places(self):
        self.assertEqual(
            Bridge._meta.get_field('longitude_east').decimal_places, 7
        )

    def test_longitude_east_field_cannot_be_blank(self):
        self.assertFalse(Bridge._meta.get_field('longitude_east').blank)

    def test_longitude_east_field_cannot_be_null(self):
        self.assertFalse(Bridge._meta.get_field('longitude_east').null)

    def test_created_date_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.get_field('created_date').verbose_name,
            'date of creation',
        )

    def test_last_update_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.get_field('last_update').verbose_name,
            'date of last update',
        )

    def test_contributors_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.get_field('contributors').verbose_name,
            'bridge contributors',
        )

    def test_contributors_field_is_many_to_many(self):
        self.assertTrue(Bridge._meta.get_field('contributors').many_to_many)

    def test_bridge_model_verbose_name(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.verbose_name,
            'bridge',
        )

    def test_bridge_model_verbose_name_plural(self):
        activate('en')
        self.assertEqual(
            Bridge._meta.verbose_name_plural,
            'bridges',
        )

    def test_bridge_model_uses_custom_manager(self):
        self.assertTrue(isinstance(Bridge.objects, BridgeManager))

    def test_string_convertion_is_correct(self):
        string_bridge = str(self.bridge)
        self.assertEqual(string_bridge, f"(7.0000000, 4.0000000)")

    def test_bbox_getter_is_correct(self):
        self.assertEqual(
            self.bridge.bbox,
            [
                Decimal('3.98'),
                Decimal('6.98'),
                Decimal('4.02'),
                Decimal('7.02'),
            ],
        )

    def test_bbox_string_getter(self):
        self.assertEqual(
            self.bridge.bbox_string,
            'bbox:3.9800000,6.9800000,4.0200000,7.0200000',
        )


class BridgeUpdateTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser', email='test@test.fr', password='ajHpq.p#2'
        )
        cls.bridge = Bridge.objects.create(
            height=10,
            width=10,
            latitude=Decimal('7.0'),
            longitude=Decimal('4.0'),
            latitude_north=Decimal('7.02'),
            latitude_south=Decimal('6.98'),
            longitude_west=Decimal('3.98'),
            longitude_east=Decimal('4.02'),
        )
        cls.bridge.contributors.add(cls.user)

    def test_contributor_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            BridgeUpdate._meta.get_field('contributor').verbose_name,
            'update contributor',
        )

    def test_contributor_field_is_many_to_one(self):
        self.assertTrue(
            BridgeUpdate._meta.get_field('contributor').many_to_one
        )

    def test_contributor_field_related_model(self):
        self.assertEqual(
            BridgeUpdate._meta.get_field('contributor').related_model, User
        )

    def test_bridge_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            BridgeUpdate._meta.get_field('bridge').verbose_name,
            'updated bridge',
        )

    def test_bridge_field_related_model(self):
        self.assertEqual(
            BridgeUpdate._meta.get_field('bridge').related_model, Bridge
        )

    def test_bridge_field_is_many_to_one(self):
        self.assertTrue(BridgeUpdate._meta.get_field('bridge').many_to_one)

    def test_updated_date_field_verbose_name(self):
        activate('en')
        self.assertEqual(
            BridgeUpdate._meta.get_field('updated_date').verbose_name,
            'updated date',
        )