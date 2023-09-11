# views.py
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .utils import detect_face
import os
from django.conf import settings
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


def handler(image_url, face_img):
    return {'image_url': image_url, 'response': face_img}


def success_page(request, arg1, arg2):
    return render(request, 'success.html', {'image_url': arg1, 'response': arg2})


def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']

            file_name = uploaded_file.name  # Get the original file name
            # directory_path = os.path.join(STATIC_FILES, 'uploads')

            form.save()
            face_img = detect_face(f'./../media/uploads/{file_name}')
            os.remove(os.path.join(settings.MEDIA_ROOT,
                                   f'./../media/uploads/{file_name}'))
            file_names = os.listdir(settings.STATIC_FILES)

            # Redirect to a success page or do something else
            return render(request, 'success.html', {'response': face_img, 'image_url': file_names[0]})
    else:
        form = FileUploadForm()
    return render(request, './upload.html', {'form': form})
