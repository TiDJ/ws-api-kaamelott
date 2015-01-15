# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, verbose_name=b'Prenom')),
                ('last_name', models.CharField(max_length=50, null=True, verbose_name=b'Nom', blank=True)),
                ('title', models.CharField(max_length=200, null=True, verbose_name=b'Titre', blank=True)),
                ('image', models.ImageField(upload_to=b'character_images', null=True, verbose_name=b'Photo du personnage', blank=True)),
                ('origin', models.CharField(max_length=100, null=True, verbose_name=b'Origine', blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Description', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
