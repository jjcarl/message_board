# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150806_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='pin',
            field=models.BooleanField(default=False),
        ),
    ]
