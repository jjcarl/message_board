from django.contrib.auth.models import User
from django import forms
from main.models import Message, Comment, Tag


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class TagForm(forms.ModelForm):
    word = forms.CharField(
        label='Tags',
        required=False,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder':
                   'Write your tags in here'}))

    class Meta:
        model = Tag
        fields = '__all__'
