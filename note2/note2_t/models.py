# models.py
from django.db import models
from django_quill.fields import QuillField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class notes(models.Model):
    title = models.CharField(max_length = 255)
    body = RichTextUploadingField()

