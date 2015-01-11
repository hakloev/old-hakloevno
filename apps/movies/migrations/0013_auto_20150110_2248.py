# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0012_remove_movie_poster_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('seen', models.BooleanField(default=False)),
                ('last_seen', models.DateField(null=True, blank=True)),
                ('added', models.DateField(auto_now_add=True)),
                ('movie', models.ForeignKey(to='movies.Movie')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='added',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='from_api',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='last_seen',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='seen',
        ),
    ]
