from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Question, Choice
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'ultimasPreguntas'

    def get_queryset(self):
        return Question.objects.order_by('pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'


def vote(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    try:
        selectedChoice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question, 
            'error_message': 'No seleccionaste ninguna opcion'
            })
    else:
        selectedChoice.votes += 1
        selectedChoice.save()
        return HttpResponseRedirect(reverse('mainSite:results', args=(question.id,)))
