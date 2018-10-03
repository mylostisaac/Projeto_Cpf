from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question
from django.utils import timezone
from .validate_cpf import validate_CPF
from .validate_cpf import gera_CPF



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'cpf/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question2 = str(question.question_text)
    check = validate_CPF(question2)

    return render(request, 'cpf/detail.html', {'question': question, 'check': check})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'cpf/results.html', {'question': question})

def validateCpf(request):
    cpf = Question(question_text=request.POST['cpf'], pub_date=timezone.now())
    cpf.save()
    return HttpResponseRedirect(reverse('cpf:index'))

def generateCpf(request):
    cpf = Question(question_text=gera_CPF(), pub_date=timezone.now())
    cpf.save()
    return HttpResponseRedirect(reverse('cpf:index'))
    
    
    # if check == "{} eh Valido".format(cpf):
    #     cpf.save()
    #     return render(request, 'cpf/validate.html', {'cpf': cpf, 'answer':check})
    # else:
    #     return render(request, 'cpf/validate.html', {'cpf': cpf, 'answer':check})

def vote(request):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'cpf/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def voltar(request, question_id):

    return HttpResponseRedirect(reverse('cpf:index'))