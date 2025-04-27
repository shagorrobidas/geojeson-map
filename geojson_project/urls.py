from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from map_app.views import upload_geojson, map_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', upload_geojson, name='upload_view'),
    path('map/', map_view, name='map_view'),
    path('', map_view),  # Default to map view
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)