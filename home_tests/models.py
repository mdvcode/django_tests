from django.contrib.auth.models import User
from django.db import models


class Language(models.Model):
    objects = None
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    objects = None
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200, null=True, blank=True)
    answer = models.CharField(max_length=250, null=True, blank=True)
    pub_date = models.DateTimeField('date published', null=True, blank=True)


class Choice(models.Model):
    DoesNotExist = None
    language = models.ForeignKey(Language, null=True, blank=True, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    choice_text = models.CharField(max_length=250, null=True, blank=True)
    votes = models.IntegerField(default=0, null=True, blank=True)
    correct_votes = models.IntegerField(default=0, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)







