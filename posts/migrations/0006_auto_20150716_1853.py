# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20150716_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='is_publicated',
            new_name='is_published',
        ),
    ]
