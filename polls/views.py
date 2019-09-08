from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date").all()[:5]
    return render(request, "polls/index.html", {"latest_question_list": latest_question_list})


def detail(request, question_id):
    return HttpResponse("Your question is %s" % question_id)


def results(request, question_id):
    response = "Your results is %s" % question_id


def test(request):

    try:
        response = request.POST["text"]
    except:
        template = loader.get_template("polls/test.html")
        return HttpResponse(template.render({}, request))
    else:
        template = loader.get_template("polls/test.html")
        return HttpResponse(template.render({"response": response}, request))
