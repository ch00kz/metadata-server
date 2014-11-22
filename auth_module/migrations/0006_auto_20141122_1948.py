# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0005_auto_20141122_1830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesstoken',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='accesstoken',
            name='start_date',
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='created',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='expires',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
