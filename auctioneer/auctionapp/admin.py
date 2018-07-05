# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import AuctionItem, AuctionImages

admin.site.register(AuctionItem)
admin.site.register(AuctionImages)

# Register your models here.
