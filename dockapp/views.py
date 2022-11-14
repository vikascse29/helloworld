from django.shortcuts import render, get_object_or_404
import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    print(latest_question_list)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'dockapp/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question,question.question_text)
    return render(request, 'dockapp/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'dockapp/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'dockapp/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('dockapp:results', args=(question.id,)))

# def index(request):
    
#     p = "Hello Project"
#     #print(p)
#     #return render(request, "home.html", {})
#     return render(request, "home.html", {})

def nana(request):
    
    p = "Hello Project"
    print(p)
    return render(request, "nana.html", {})

def nanadocker(request):
    
    p = "Details submitted succeffully"
    print(p)
    return render(request, "home.html", {})
