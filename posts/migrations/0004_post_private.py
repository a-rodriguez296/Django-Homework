# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20150714_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
