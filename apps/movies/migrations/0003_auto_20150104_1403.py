# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20150104_1312'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['added'], 'permissions': (('view_movie', 'Can view movie'), ('add_movie', 'Can add movie'), ('delete_movie', 'Can delete movie'), ('edit_movie', 'Can edit movie'))},
        ),
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default='title'),
            preserve_default=False,
        ),
    ]
