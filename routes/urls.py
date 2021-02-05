from django.urls import path

from .views import RouteSearchView, RouteResultView

app_name = 'routes'

urlpatterns = [
    path('', RouteSearchView.as_view(), name='search'),
    path('results/', RouteResultView.as_view(), name='result'),
]
