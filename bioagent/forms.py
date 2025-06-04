from django import forms
from .models import AnnotatedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = AnnotatedFile
        fields = ['file']
