# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(related_name='comment_parent', blank=True, to='main.Comment', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('media', models.ImageField(null=True, upload_to=b'%Y/%m/%d', blank=True)),
                ('pin', models.BooleanField(default=False)),
                ('link', models.URLField(null=True, blank=True)),
                ('reference', models.CharField(max_length=100, null=True, blank=True)),
                ('post_type', models.CharField(default=b'PST', max_length=3, choices=[(b'QTE', b'Quote'), (b'PST', b'Post'), (b'VID', b'Video'), (b'AUD', b'Audio')])),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('favorite', models.ManyToManyField(related_name='favorites', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(unique=True, max_length=50)),
                ('message', models.ForeignKey(to='main.Message')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(to='main.Message'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
