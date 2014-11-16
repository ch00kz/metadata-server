# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadatauser',
            name='is_staff',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='metadatauser',
            name='is_superuser',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
