from django.shortcuts import render
from myblog.models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles": articles})

def article(request, id):
    article = Article.objects.get(id=id)
    return render(request, "article.html", {})