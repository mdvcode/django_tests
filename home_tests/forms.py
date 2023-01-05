from django import forms
from .models import Language, Question


class FilterPostForm(forms.Form):
    language = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all()
    )


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_text',)
