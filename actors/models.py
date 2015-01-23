from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.db.models.signals import post_save
from characters.models import *

# Actor model

class Actor(models.Model):

	character = models.OneToOneField(Character, verbose_name="Personnage")
	first_name = models.CharField(max_length=50, verbose_name="Prenom")
	last_name = models.CharField(max_length=50, verbose_name="Nom")
	birthdate = models.DateTimeField(null=True, blank=True, verbose_name="Date de naissance")
	city = models.CharField(null=True, blank=True, max_length=100, verbose_name="Ville d'origine")
	description = models.TextField(null=True, blank=True, verbose_name="Description")
	image = models.ImageField(upload_to="actor_images",null=True, blank=True, verbose_name="Photo de l'acteur")

	def __unicode__(self):
		return self.first_name+self.last_name
