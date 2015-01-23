from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
from characters.models import *

# Quote model

class Quote(models.Model):

	character = models.ForeignKey(Character, verbose_name="Personnage")
	quote = models.TextField(verbose_name="Citation")
	title = models.CharField(max_length="100", verbose_name="Titre")


	def __unicode__(self):
		return self.quote
