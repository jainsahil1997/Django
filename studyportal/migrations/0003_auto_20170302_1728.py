# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 17:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studyportal', '0002_auto_20170228_0919'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='subject',
            new_name='sub_name',
        ),
    ]
