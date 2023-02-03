from django.shortcuts import render, redirect

from .models import Catalog, Question
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required


@login_required(login_url='/users/login/')
def home(request):
    categories = Catalog.objects.all()
    context = {'categories': categories}
    return render(request, 'home_tests/home.html', context)


@login_required(login_url='/users/login/')
def take_quiz(request, pk):
    questions = Question.objects.filter(catalog=pk).order_by('-created_at')
    paginator = Paginator(questions, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'questions': questions, 'page_obj': page_obj, }
    if request.method == 'GET':
        try:
            questions = paginator.page(page_number)
        except PageNotAnInteger:
            questions = paginator.page(1)
        except EmptyPage:
            questions = paginator.page(paginator.num_pages)
        return render(request, 'home_tests/question.html', context)
    if request.method == 'POST':
        correct_user_answers = 0
        total_questions = questions.count()
        false_answers = 0
        for question in questions:
            user_answer = request.POST.get(f"option_{question.id}")
            correct_answer = question.answer
            if user_answer == correct_answer:
                correct_user_answers += 1
            else:
                false_answers += 1
        percent = (correct_user_answers * 100) / total_questions
        context = {'percent': percent, 'correct_user_answers': correct_user_answers, 'false_answers': false_answers,
                   'total_questions': total_questions, 'questions': questions}
        return render(request, 'home_tests/question.html', context)




