from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.favorite_list, name='favorite_list'),
]