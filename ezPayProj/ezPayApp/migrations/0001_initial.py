# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-24 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PayUser',
            fields=[
                ('stuId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('balance', models.FloatField(default=0.0)),
                ('dueDate', models.DateTimeField()),
                ('has_acc', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=500)),
                ('auth', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originMoneyMovementAccountReferenceId', models.CharField(max_length=100)),
                ('destinationMoneyMovementAccountReferenceId', models.CharField(max_length=100)),
                ('transferAmount', models.FloatField(default=0.0)),
                ('currencyCode', models.CharField(default='USD', max_length=100)),
                ('transferDate', models.DateField()),
                ('memo', models.CharField(max_length=100)),
                ('transferType', models.CharField(choices=[('ACH', 'ACH'), ('Internal', 'Internal')], default='ACH', max_length=10)),
                ('frequency', models.CharField(choices=[('OneTime', 'One time only')], default='OneTime', max_length=10)),
            ],
        ),
    ]
