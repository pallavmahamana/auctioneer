# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime, timedelta

# Create your models here.

class AuctionItem(models.Model):
	def get_end_auc_datetime():
		return datetime.now() + timedelta(days=1)
	title = models.CharField(max_length=50)
	desc = models.TextField()
	created_on = models.DateTimeField('Created on', auto_now_add=True)
	start_auc_datetime = models.DateTimeField(default=datetime.now)
	end_auc_datetime = models.DateTimeField(default=get_end_auc_datetime)

	def __str__(self):
		return self.title




class AuctionImages(models.Model):
	auctionitem = models.ForeignKey(AuctionItem,related_name='images',
		on_delete=models.CASCADE)
	image = models.ImageField()


