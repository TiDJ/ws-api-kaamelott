# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, verbose_name=b'Prenom')),
                ('last_name', models.CharField(max_length=50, verbose_name=b'Nom')),
                ('birthdate', models.DateTimeField(null=True, verbose_name=b'Date de naissance', blank=True)),
                ('city', models.CharField(max_length=100, null=True, verbose_name=b"Ville d'origine", blank=True)),
                ('description', models.TextField(null=True, verbose_name=b'Description', blank=True)),
                ('image', models.ImageField(upload_to=b'actor_images', null=True, verbose_name=b"Photo de l'acteur", blank=True)),
                ('character', models.OneToOneField(verbose_name=b'Personnage', to='characters.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
