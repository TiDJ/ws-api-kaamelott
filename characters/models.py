from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
from actors.models import *

# Character model

class Character(models.Model):

	#actor = models.OneToOneField(Actor, verbose_name="Acteur")
	first_name = models.CharField(max_length=50, verbose_name="Prenom")
	last_name = models.CharField(null=True, blank=True, max_length=50, verbose_name="Nom")
	title = models.CharField(max_length=200, null=True, blank=True, verbose_name="Titre")
	image = models.ImageField(upload_to="character_images",null=True, blank=True, verbose_name="Photo du personnage")
	origin = models.CharField(max_length=100, null=True, blank=True, verbose_name="Origine")
	description = models.TextField(null=True, blank=True, verbose_name="Description")

	def __unicode__(self):
		return self.first_name
