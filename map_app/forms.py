from django import forms
from .models import GeoJSONFile


class GeoJSONUploadForm(forms.ModelForm):
    class Meta:
        model = GeoJSONFile
        fields = ['name', 'description', 'file']