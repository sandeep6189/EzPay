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
	has_acc = models.BooleanField(default=False)

	def __unicode__(self):
	    return self.name
	def __str__(self):
	    return self.name

class Transfer(models.Model):
	TRANSFER_TYPES = [
	    ('ACH', 'ACH'),
	    ('Internal', 'Internal')
	]


	FREQUENCY_TYPES = [
		('OneTime', 'One time only')]
	
	originMoneyMovementAccountReferenceId = models.CharField(max_length=100)
	destinationMoneyMovementAccountReferenceId = models.CharField(max_length=100)
	transferAmount = models.FloatField(default = 0.0)
	currencyCode = models.CharField(max_length=100, default = "USD")
	transferDate =  models.CharField(max_length = 10)
	memo = models.CharField(max_length = 100)
	transferType = models.CharField(max_length = 10, default = 'ACH', choices = TRANSFER_TYPES)
	frequency = models.CharField(max_length = 10, default = 'OneTime', choices = FREQUENCY_TYPES)


