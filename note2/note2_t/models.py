# models.py
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class notes(models.Model):
    body = RichTextUploadingField()

class save(models.Model):
    body = "something"
    # writing all the lines to a text file
    outputFile = open("outputFile.txt", "w")
    for line in body:
        outputFile.write(line)
        outputFile.write("\n")
    outputFile.close()

class read():
    # reading all the lines from a text tile
    body = ""
    readFile = open("outputFile.txt", "r")
    for line in readFile:
        # print(line)
        body = body + "" + line + " "
    readFile.close()
