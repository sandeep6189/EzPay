# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 20:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ezPayApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='transferDate',
            field=models.CharField(max_length=10),
        ),
    ]
