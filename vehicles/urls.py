from django.urls import path

from .views import (
    VehicleCreateView,
    VehicleUpdateView,
    VehicleDeleteView,
    VehicleListView,
    VehicleImageChangeView,
)

app_name = 'vehicles'

urlpatterns = [
    path('', VehicleListView.as_view(), name='list'),
    path('create/', VehicleCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', VehicleUpdateView.as_view(), name="edit"),
    path('<int:pk>/delete/', VehicleDeleteView.as_view(), name="delete"),
    path(
        '<int:pk>/image/change/',
        VehicleImageChangeView.as_view(),
        name="image_change",
    ),
]
