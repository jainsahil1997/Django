# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyportal', '0009_remove_subject_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='material',
            name='past_papers',
        ),
        migrations.RemoveField(
            model_name='material',
            name='ppt',
        ),
        migrations.AddField(
            model_name='material',
            name='material_desc',
            field=models.CharField(default='code', max_length=50),
        ),
        migrations.AddField(
            model_name='material',
            name='material_link',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='material',
            name='type',
            field=models.CharField(choices=[('books', 'Books'), ('ppt', 'PPT'), ('pp', 'Past Papers'), ('lv', 'Lecture Video'), ('notes', 'Notes'), ('others', 'Others')], default='books', max_length=50),
        ),
    ]