# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0002_auto_20141115_1035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='_type',
            new_name='ttype',
        ),
    ]
