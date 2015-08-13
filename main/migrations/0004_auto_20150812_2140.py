# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150812_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='tag',
            field=models.ForeignKey(related_name='messages', blank=True, to='main.Tag', null=True),
        ),
    ]
