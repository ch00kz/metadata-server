# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth_module', '0004_metadatauser_access_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=b'32', null=True, blank=True)),
                ('start_date', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('user', models.ForeignKey(related_name='tokens', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='metadatauser',
            name='access_token',
        ),
    ]
