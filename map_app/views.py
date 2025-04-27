from django.shortcuts import render, redirect
from .forms import GeoJSONUploadForm
from .models import GeoJSONFile
import os


def upload_geojson(request):
    if request.method == 'POST':
        form = GeoJSONUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('map_view')
    else:
        form = GeoJSONUploadForm()
    return render(request, 'map_app/upload.html', {'form': form})


def map_view(request):
    # Get the most recently uploaded file
    latest_file = GeoJSONFile.objects.last()
    geojson_url = latest_file.file.url if latest_file else None
    return render(request, 'map_app/map.html', {'geojson_url': geojson_url})