# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_movie_runtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster_img',
            field=models.ImageField(null=True, upload_to=b'images/posters', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='poster_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
