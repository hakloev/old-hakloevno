# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_auto_20150110_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermovie',
            name='um_id',
            field=models.IntegerField(null=True, editable=False, blank=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='usermovie',
            unique_together=set([('um_id', 'movie')]),
        ),
    ]
