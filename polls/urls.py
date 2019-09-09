from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/question/", views.detail, name="vote"),
    path("test", views.test, name="test"),
    
]