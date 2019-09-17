from django.shortcuts import render
from myblog.models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles": articles})

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    comments = article.comment_set.all()
    return render(request, "article.html", {"article": article, "comments":comments})