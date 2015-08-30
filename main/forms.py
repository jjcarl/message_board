from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import Message, Comment, Tag


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
