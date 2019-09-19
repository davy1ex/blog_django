from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate

from myblog.models import Article
from django.contrib.auth.models import User


def index(request):
    articles = Article.objects.all()
    #return HttpResponse(request.session.get(user.username))
    return render(request, "index.html", {"articles": articles})

def article(request, article_id):
    # body author arcicle    
    #return HttpResponse(HttpResponse(user.username))
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        #user = request.session.get("user"
        user = User.objects.get(id=request.session.get("user_id"))
        if user is not None: 
            article.comment_set.create(author=user.username, body=request.POST.get("text_comment"), article=article)
            article.save()
            #return HttpResponse(request.POST.get("text_comment"))
    comments = article.comment_set.all()
    return render(request, "article.html", {"article": article, "comments":comments})
