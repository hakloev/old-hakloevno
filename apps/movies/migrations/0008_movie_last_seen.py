# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movie_seen'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='last_seen',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
