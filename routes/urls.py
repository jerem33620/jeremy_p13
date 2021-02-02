from django.urls import path

from .views import route_search, route_result

app_name = 'routes'

urlpatterns = [
    path('', route_search, name='search'),
    path('results/', route_result, name='result'),
]
