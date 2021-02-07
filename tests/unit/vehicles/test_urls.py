from django.test import TestCase
from django.urls import resolve

from vehicles import views


class URLResolutionTests(TestCase):
    def test_list_resolves_to_right_view(self):
        view = resolve('/vehicles/')
        self.assertEqual(view.url_name, 'list')
        self.assertEqual(view.namespace, 'vehicles')
        self.assertEqual(view.func.view_class, views.VehicleListView)

    def test_create_resolves_to_right_view(self):
        view = resolve('/vehicles/create/')
        self.assertEqual(view.url_name, 'create')
        self.assertEqual(view.namespace, 'vehicles')
        self.assertEqual(view.func.view_class, views.VehicleCreateView)

    def test_edit_resolves_to_right_view(self):
        view = resolve('/vehicles/1234/edit/')
        self.assertEqual(view.url_name, 'edit')
        self.assertEqual(view.namespace, 'vehicles')
        self.assertEqual(view.func.view_class, views.VehicleUpdateView)

    def test_delete_resolves_to_right_view(self):
        view = resolve('/vehicles/1234/delete/')
        self.assertEqual(view.url_name, 'delete')
        self.assertEqual(view.namespace, 'vehicles')
        self.assertEqual(view.func.view_class, views.VehicleDeleteView)

    def test_image_change_resolves_to_right_view(self):
        view = resolve('/vehicles/1234/image/change/')
        self.assertEqual(view.url_name, 'image_change')
        self.assertEqual(view.namespace, 'vehicles')
        self.assertEqual(view.func.view_class, views.VehicleImageChangeView)