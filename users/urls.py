from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('account/', views.profile, name='profile'),
    path('avatar/', views.avatar_change, name="avatar_change"),
]