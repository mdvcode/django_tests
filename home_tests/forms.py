from django import forms
from .models import Language


class FilterPostForm(forms.Form):
    language = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all()
    )
