# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyportal', '0011_auto_20170328_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='material_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='material',
            name='material_link',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
