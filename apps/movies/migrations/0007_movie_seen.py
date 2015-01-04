# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20150104_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='seen',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
