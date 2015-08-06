from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import Message, Comment


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
