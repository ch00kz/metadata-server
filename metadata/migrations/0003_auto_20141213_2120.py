# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0002_auto_20141213_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='currency',
            field=models.ForeignKey(blank=True, to='metadata.Currency', null=True),
            preserve_default=True,
        ),
    ]
