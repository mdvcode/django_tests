from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from home_tests.forms import FilterPostForm, QuestionForm
from home_tests.models import Language, Question, Choice


def home(request):
    question_list = Question.objects.order_by('-pub_date')[:5]
    languages = Language.objects.all()
    form_filter = FilterPostForm
    if request.POST:
        form_filter = FilterPostForm(request.POST)
        if form_filter.is_valid():
            language = form_filter.cleaned_data.get('language')
            language_id = []
            for item in language:
                language_id.append(item.id)
            if len(language_id) > 0:
                question_list = Question.objects.filter(language_id__in=language_id)
        else:
            form_filter = FilterPostForm
    return render(request, 'home_tests/home.html', context={'question_list': question_list, 'languages': languages,
                                                            'form_filter': form_filter})


def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuestionForm
    return render(request, 'home_tests/question.html', {'question': question, 'form': form})


def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'home_tests/question.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        if selected_choice.votes == question.answer:
            print('correct')
            selected_choice.correct_votes += 1
            # selected_choice.save()
        elif selected_choice.votes != question.answer:
            print('not correct')
            selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('home_tests:results', args=(question.id,)))


def results(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, 'home_tests/results.html', {'question': question})



