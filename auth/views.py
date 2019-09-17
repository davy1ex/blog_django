from django.shortcuts import render
from .forms import UserForm


def login(request):
    form = UserForm()
    return render(request, "auth/login.html", {"form": form})
