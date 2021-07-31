from django.shortcuts import render

from .models import Question


def index(request):
    questions = Question.objects.exclude(choice__isnull=True)
    return render(request, 'polls/index.html', {'questions': questions})
