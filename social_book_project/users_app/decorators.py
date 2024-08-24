from .models import UploadedFile  # Update the import based on your file model
from django.shortcuts import redirect

def check_uploaded_files(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if UploadedFile.objects.filter(user=request.user).exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect('upload_books')
    return _wrapped_view
