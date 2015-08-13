# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20150812_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='tag',
            field=models.ManyToManyField(related_name='messages', to='main.Tag', blank=True),
        ),
    ]
