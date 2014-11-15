# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='/pen', max_length=200),
            preserve_default=False,
        ),
    ]
