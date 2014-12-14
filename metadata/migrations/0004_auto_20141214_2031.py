# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0003_auto_20141213_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='assisting_staff',
            field=models.ManyToManyField(related_name='assisting_projects', null=True, to='metadata.Staff', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='lead_staff',
            field=models.ManyToManyField(related_name='lead_projects', null=True, to='metadata.Staff', blank=True),
            preserve_default=True,
        ),
    ]
