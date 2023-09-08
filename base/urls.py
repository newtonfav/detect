# urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_file, success_page

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('success/', success_page, name='success-page'),
    # Add more URL patterns as needed
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
