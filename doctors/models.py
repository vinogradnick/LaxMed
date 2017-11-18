from __future__ import unicode_literals
from django.db import models


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    specialization = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    obrazovanie = models.CharField(max_length=50)
    stage = models.IntegerField(default=1)
    about_info = models.TextField()
    phone = models.IntegerField(default=79000000001)


class Time(models.Model):
    id = models.AutoField(primary_key=True)
    day_data = models.IntegerField(default=0)
    doc_id = models.ForeignKey(Doctor, blank=True, null=True, on_delete=models.SET_NULL)


class ExtraTime(models.Model):
    time = models.TimeField()
    status = models.CharField(max_length=10)
    id = models.AutoField(primary_key=True)
    time_id = models.ForeignKey(Time, blank=True, null=True, on_delete=models.SET_NULL)


class Profile(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Schedule(models.Model):
    check = models.BooleanField(default=False)
    secret_code = models.IntegerField(default=0)
    people_email = models.EmailField(max_length=20)
    people_name = models.CharField(max_length=20)
    people_phone = models.IntegerField(default=0)
    doct = models.IntegerField(default=0)
    data = models.IntegerField(default=0)
    time = models.IntegerField(default=0)

# Create your models here.
