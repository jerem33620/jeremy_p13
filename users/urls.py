from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('account/', views.accountlog, name='accountlog'),
    path('avatar/', views.avatar_change, name="avatar_change"),
]