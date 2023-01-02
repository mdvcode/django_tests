from django.db import models


class Language(models.Model):
    objects = None
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tests(models.Model):
    objects = None
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    link = models.URLField(max_length=50, null=True, blank=True)
