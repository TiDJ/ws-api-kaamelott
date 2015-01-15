# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quote', models.TextField(verbose_name=b'Citation')),
                ('character', models.ForeignKey(verbose_name=b'Personnage', to='characters.Character')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
