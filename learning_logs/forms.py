"""learning_logs/forms.py"""

# Django modules
from django import forms

# My modules
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """ADD: Class TopicForm"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """ADD: Class EntryForm"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}