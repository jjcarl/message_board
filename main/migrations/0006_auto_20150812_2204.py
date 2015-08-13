# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20150812_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='tag',
        ),
        migrations.AddField(
            model_name='message',
            name='tag',
            field=models.ManyToManyField(related_name='messages', null=True, to='main.Tag', blank=True),
        ),
    ]
