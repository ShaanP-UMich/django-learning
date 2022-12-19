# Long method
# from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader

# Shortcut method
from django.shortcuts import render, get_object_or_404

from django.http import Http404

from .models import Question

# Create your views here.


def index(request):
    # questions = {"question1": "What is your name?", "question2": "What is your favorite color?"}

    # return HttpResponse(json.dumps(questions))
    # return HttpResponse("Hello, world. You're at the polls index page.")

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }

    return render(request, 'polls/index.html', context)

    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    # return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse(f"You're looking at question {question_id}.")

    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")

def leaderline(request):
    return render(request, 'polls/leaderline.html', {})