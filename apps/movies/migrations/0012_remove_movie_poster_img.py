# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20150104_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='poster_img',
        ),
    ]
