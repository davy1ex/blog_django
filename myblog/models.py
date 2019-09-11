from django.db import models
from django.urls import path


class Article(models.Model):
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=256)
    photo = models.FileField(upload_to='myblog/static')