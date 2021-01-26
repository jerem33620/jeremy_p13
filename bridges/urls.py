from django.urls import path

from .views import BridgeCreate

app_name = 'bridges'

urlpatterns = [
    path('', BridgeCreate.as_view(), name='create')
]