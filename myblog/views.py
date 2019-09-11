from django.shortcuts import render
from myblog.models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles": articles})