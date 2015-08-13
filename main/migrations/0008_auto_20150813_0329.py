# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20150812_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='post_type',
            field=models.CharField(default=b'PST', max_length=3, choices=[(b'QTE', b'Quote'), (b'PST', b'Post'), (b'YTB', b'Youtube'), (b'VMO', b'Vimeo'), (b'AUD', b'Audio')]),
        ),
    ]
