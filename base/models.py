from django.db import models

# Create your models here.


# class Item(models.Model):
#     name = models.CharField(max_length=200)
#     created = models.DateTimeField(auto_now_add=True)


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
