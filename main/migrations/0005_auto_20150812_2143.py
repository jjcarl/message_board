# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150812_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='tag',
            field=models.ForeignKey(related_name='messages', to_field=b'word', blank=True, to='main.Tag', null=True),
        ),
    ]
