# models.py
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class notes(models.Model):
    body = RichTextUploadingField()

class save():

# class read():

