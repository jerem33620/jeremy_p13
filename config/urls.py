"""GPS & GO URL Configuration."""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('users/', include('users.urls', namespace='users')),
    path('users/', include('django.contrib.auth.urls')),
    path('vehicles/', include('vehicles.urls', namespace='vehicles')),
    path('bridges/', include('bridges.urls', namespace='bridges')),
    path('routes/', include('routes.urls', namespace='routes')),
]

# Handling of media files for development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
