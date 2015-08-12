from django.contrib import admin
from main.models import Message, Comment, Tag

admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Tag)
