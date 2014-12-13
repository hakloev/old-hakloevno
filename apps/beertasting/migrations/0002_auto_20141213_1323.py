# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beertasting', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tastingevent',
            options={'permissions': (('view_admin', 'Can see admin list'),)},
        ),
    ]
