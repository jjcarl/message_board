# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150807_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='file_type',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'IMG', b'Image'), (b'VID', b'Video'), (b'DOC', b'Document'), (b'AUD', b'Audio')]),
        ),
    ]
