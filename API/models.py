# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Stock(models.Model):
	symbol = models.CharField(max_length=5)
	name = models.CharField(max_length=100)

class Trader(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	balance = models.FloatField()
	created_at = models.CharField(max_length=20)
	updated_at = models.CharField(max_length=20)