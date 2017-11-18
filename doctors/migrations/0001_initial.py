# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('specialization', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('obrazovanie', models.CharField(max_length=50)),
                ('stage', models.IntegerField(default=1)),
                ('about_info', models.TextField()),
                ('phone', models.IntegerField(default=79000000001L)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraTime',
            fields=[
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=10)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check', models.BooleanField(default=False)),
                ('secret_code', models.IntegerField(default=0)),
                ('people_email', models.EmailField(max_length=20)),
                ('people_name', models.CharField(max_length=20)),
                ('people_phone', models.IntegerField(default=0)),
                ('doct', models.IntegerField(default=0)),
                ('data', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day_data', models.IntegerField(default=0)),
                ('doc_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctors.Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='extratime',
            name='time_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctors.Time'),
        ),
    ]