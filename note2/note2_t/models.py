# models.py
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.urls import reverse

class notes(models.Model):
    title = models.CharField(max_length=255,default="Notes")
    body = RichTextUploadingField()

    def get_absolute_url(self):
        return reverse('home')
