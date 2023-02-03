from django.contrib.auth.models import User
from django.db import models


class Language(models.Model):
    objects = None
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Catalog(models.Model):
    objects = None
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.category


class Question(models.Model):
    objects = None
    catalog = models.ForeignKey(Catalog, null=True, blank=True, on_delete=models.CASCADE)
    question = models.CharField(max_length=200, null=True, blank=True)
    answer = models.CharField(max_length=250, null=True, blank=True)
    option_one = models.CharField(max_length=100, null=True, blank=True)
    option_two = models.CharField(max_length=100, null=True, blank=True)
    option_three = models.CharField(max_length=100, blank=True)
    option_four = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    procent = models.IntegerField(default=0, null=True, blank=True)
    correct_ans = models.IntegerField(default=0, null=True, blank=True)
    notcorrect_ans = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.question
