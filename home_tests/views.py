import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from django.contrib.sites.models import Site
from django.core.handlers.wsgi import WSGIRequest
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

from home_tests.forms import FilterPostForm
from home_tests.models import Tests, Language


def home(request):
    tests = Tests.objects.all()
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
                tests = Tests.objects.filter(language_id__in=language_id)
        else:
            form_filter = FilterPostForm
    return render(request, 'home_tests/home.html', context={'tests': tests, 'form_filter': form_filter,
                                                            'languages': languages})
