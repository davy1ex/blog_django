from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User

from .forms import UserForm


def login(request):
    if request.method == "POST":
        data = request.POST.copy()
        user = authenticate(username=data.get("username") , password=data.get("password"))
        
        if user is not None:
            return HttpResponse("Hello", + user.username)

    
    form = UserForm()

    return render(request, "auth/login.html", {"form": form})
