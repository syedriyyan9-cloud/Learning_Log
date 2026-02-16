from django import forms

from .models import Topics, Entry

class TopicForm(forms.ModelForm):
    """User forms for topics"""
    class Meta:
        """create forms on Topics model"""
        model = Topics
        fields = ['text']
        label = {'text': ''}

class EntryForm(forms.ModelForm):
    """Entry forms for users"""
    class Meta:
        """create forms on Entry model"""
        model = Entry
        fields = ['text']
        label = {'text':'Entry:'}
        widgets = {'text': forms.Textarea(attrs = {'cols':80})}