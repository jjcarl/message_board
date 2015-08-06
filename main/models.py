from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    media = models.FileField(upload_to='%Y/%m/%d', null=True, blank=True)
    favorite = models.ManyToManyField(User,
                                      related_name='favorites', blank=True)
    pin = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    message = models.ForeignKey('Message')
    content = models.TextField()
    user = models.ForeignKey(User)
    date_posted = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey('self',
                                related_name='comment_parent',
                                null=True, blank=True)

    def __unicode__(self):
        return "%s, %s" % (self.user.username, self.message)
