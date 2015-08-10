# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_message_file_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='file_type',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'IMG', b'Image'), (b'VID', b'Video'), (b'AUD', b'Audio')]),
        ),
    ]
