# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.beertasting.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('ibu', models.IntegerField()),
                ('abv', models.FloatField()),
                ('code', models.CharField(max_length=50, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BeerRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.IntegerField(validators=[apps.beertasting.models.validate_beer_rating])),
                ('comment', models.TextField()),
                ('rated', models.DateTimeField(auto_now_add=True)),
                ('beer', models.ForeignKey(to='beertasting.Beer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('style', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TastingEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('finished', models.BooleanField(default=False)),
                ('beers', models.ManyToManyField(to='beertasting.Beer', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='beerrating',
            name='event',
            field=models.ForeignKey(to='beertasting.TastingEvent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beerrating',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beer',
            name='brewery',
            field=models.ForeignKey(to='beertasting.Brewery'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='beer',
            name='style',
            field=models.ForeignKey(to='beertasting.Style'),
            preserve_default=True,
        ),
    ]
