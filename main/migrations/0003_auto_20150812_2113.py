# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150812_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='message',
        ),
        migrations.AddField(
            model_name='message',
            name='tag',
            field=models.ForeignKey(blank=True, to='main.Tag', null=True),
        ),
    ]
