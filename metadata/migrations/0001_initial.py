# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('action', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('entity', models.CharField(max_length=80)),
                ('position', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('office_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('mobile_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('home_phone', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('expected_start_date', models.DateField(null=True, blank=True)),
                ('actual_start_date', models.DateField(null=True, blank=True)),
                ('expected_end_date', models.DateField(null=True, blank=True)),
                ('actual_end_date', models.DateField(null=True, blank=True)),
                ('expected_cost', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('actual_cost', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('date_created', models.DateField(null=True, blank=True)),
                ('date_updated', models.DateField(null=True, blank=True)),
                ('deleted', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('office_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('mobile_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('home_phone', models.CharField(max_length=50, null=True, blank=True)),
                ('photo', models.FileField(null=True, upload_to=b'staff_photos/', blank=True)),
                ('department', models.ForeignKey(blank=True, to='metadata.Department', null=True)),
                ('gender', models.ForeignKey(blank=True, to='metadata.Gender', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='staff',
            name='title',
            field=models.ForeignKey(blank=True, to='metadata.Title', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='assisting_staff',
            field=models.ManyToManyField(related_name='+', null=True, to='metadata.Staff', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='clients',
            field=models.ManyToManyField(to='metadata.Client', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='department',
            field=models.ManyToManyField(to='metadata.Department', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='lead_staff',
            field=models.ManyToManyField(related_name='+', null=True, to='metadata.Staff', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='title',
            field=models.ForeignKey(blank=True, to='metadata.Title', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='action',
            name='project',
            field=models.ForeignKey(related_name='actions', blank=True, to='metadata.Project', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='action',
            name='project_log',
            field=models.ForeignKey(related_name='actions', blank=True, to='metadata.ProjectLog', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='action',
            name='user',
            field=models.ForeignKey(related_name='actions', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
