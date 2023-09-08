from django.urls import path, include
from . import views
from .views import FileUploadView

urlpatterns = [
    path('', views.getData),
    path('add/', views.addData),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]
