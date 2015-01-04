# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20150104_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='from_api',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='plot',
            field=models.TextField(default='migrate', blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
