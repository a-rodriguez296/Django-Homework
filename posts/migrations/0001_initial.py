# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('summary', models.TextField(default=b'')),
                ('body', models.TextField(default=b'')),
                ('url_image', models.URLField(null=True)),
                ('published_date', models.DateField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='post',
            field=models.ForeignKey(to='posts.Post'),
        ),
    ]
