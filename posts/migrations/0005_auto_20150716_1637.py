# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_private'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='private',
            new_name='is_publicated',
        ),
    ]
