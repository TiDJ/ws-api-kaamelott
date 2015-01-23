# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='title',
            field=models.CharField(default='Titre', max_length=b'100', verbose_name=b'Titre'),
            preserve_default=False,
        ),
    ]
