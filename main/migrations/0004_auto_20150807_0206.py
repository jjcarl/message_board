# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_message_pin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to=b'%Y/%m/%d', validators=[main.validators.validate_file]),
        ),
    ]
