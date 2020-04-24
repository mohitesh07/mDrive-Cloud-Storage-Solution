from django import forms
from .models import UploadDataset

class UploadDataForm(forms.ModelForm):
    class Meta:
        model = UploadDataset
        fields = ['file_in_memory']

        labels = {
            "file_in_memory": "file"
        }