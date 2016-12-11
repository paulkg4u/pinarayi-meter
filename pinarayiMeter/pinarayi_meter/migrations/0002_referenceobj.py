# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pinarayi_meter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceObj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referenceType', models.CharField(max_length=10)),
                ('referenceLink', models.TextField(default='')),
                ('promise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinarayi_meter.Promise')),
            ],
        ),
    ]
