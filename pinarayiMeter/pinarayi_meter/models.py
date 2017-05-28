from __future__ import unicode_literals
import uuid
from django.db import models

# Create your models here.

class Promise(models.Model):
	STATUS = (
			('Not Started','Not Started'),
			('Completed', 'Completed'),
			('In Progress', 'In Progress'),
			('Broken','Broken')
		)
	CATEGORIES = (
			('Thirty Five Point Programme', 'Thirty Five Point Programme'),
			('Agriculture', 'Agriculture'),
			('Animal Husbandry','Animal Husbandry'),
			('Plantation Crops','Plantation Crops'),
			('Fisheries','Fisheries'),
			('Traditional Industries','Traditional Industries'),
			('Modern Industries','Modern Industries'),
			('Construction','Construction'),
			('Trade','Trade'),
			('IT','IT'),
			('Electricity','Electricity'),
			('Education','Education'),
			('Youth','Youth'),
			('Tourism', 'Tourism'),
			('Transportation','Transportation'),
			('Health','Health'),
			('Law and Order', 'Law and Order'),
			('Irrigation','Irrigation'),
			('Environment', 'Environment'),
			('Finance', 'Finance'),
			('Social Security','Social Security'),
		)
	uuid = models.UUIDField(unique=True,default=uuid.uuid4)
	title = models.CharField(max_length =200)
	status = models.CharField(max_length = 50, choices = STATUS, default = "Not Started")
	description = models.TextField(default = "")
	category = models.CharField(max_length = 50,choices = CATEGORIES)
	

	def __unicode__(self):
		return unicode(self.title)


class ReferenceObj(models.Model):
	TYPES = (
			('Document','Document'),
			('Video', 'Video'),
			('Web Page','Web Page')
		)
	uuid = models.UUIDField(unique=True, default=uuid.uuid4)
	promise = models.ForeignKey(Promise)
	referenceType = models.CharField(max_length = 10, choices=TYPES)
	referenceLink = models.TextField(default = "")
	title = models.CharField(max_length = 100,default = "")
	comments = models.TextField(default = "")
	approved = models.BooleanField(default = False)

	
	def __unicode__(self):
		return unicode(self.promise.title) 
