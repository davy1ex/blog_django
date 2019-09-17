from django.db import models
from django.urls import path


class Article(models.Model):
    title = models.CharField(max_length=64)
    text = models.CharField(max_length=256)
    photo = models.FileField(upload_to='myblog/static/images')


class Comment(models.Model):
    body = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    #models.ForeignKey(Reporter, on_delete=models.CASCADE)