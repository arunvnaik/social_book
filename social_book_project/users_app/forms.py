# from django import forms
# from .models import UploadedFile

# class UploadFileForm(forms.ModelForm):
#     class Meta:
#         model = UploadedFile
#         fields = ['title', 'description', 'file', 'visibility', 'cost', 'year_of_published']

# forms.py

from django import forms
from .models import UploadedFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['title', 'description', 'file', 'visibility', 'cost', 'year_of_published']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            # You can add further file validation here if needed
            if not file.name.endswith(('.pdf', '.jpeg', '.jpg')):
                raise forms.ValidationError("Only PDF, JPEG, and JPG files are allowed.")
        return file
