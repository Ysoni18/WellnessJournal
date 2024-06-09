from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
from django.conf import settings

class class_id(models.Model):
	user = models.CharField(max_length=15, null=True, blank=True)
	title = models.CharField(max_length=40, null=True)
	number = models.SmallIntegerField(primary_key=True)
	text = models.CharField(max_length=150, null=True)
	date = models.CharField(max_length=20, null=True, default='')
	def __str__(self):
		return self.title or ''

class teacher_id(models.Model):
	number = models.SmallIntegerField(primary_key=True)
	user = models.CharField(max_length=15, null=True, blank=True)

	def __int__(self):
		return self.number or ''
