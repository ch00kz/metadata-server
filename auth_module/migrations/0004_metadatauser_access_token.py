# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0003_auto_20141118_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadatauser',
            name='access_token',
            field=models.CharField(max_length=b'32', null=True, blank=True),
            preserve_default=True,
        ),
    ]
