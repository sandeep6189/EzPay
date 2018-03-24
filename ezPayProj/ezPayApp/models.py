# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    auth = models.CharField(max_length=200)

	def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class PayUser(models.Model):
    stuId = models.CharField(max_length=100, primary_key = True)
    name = models.CharField(max_length=200)
    balance = models.FloatField(default = 0.0)	
    dueDate = models.DateTimeField()
    has_acc = = models.BooleanField(default=False)

	def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
