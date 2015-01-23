#!/usr/local/bin/python
# coding: latin-1
from tastypie.resources import ModelResource
from characters.models import *
from tastypie import fields
from tastypie.resources import ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from cors_resource import *

#Character resource : File which handles the web service for Characters

class CharacterResource(CORSModelResource):
	class Meta:

		#Which base data we are returning in GET if no parameters are given (here, all character objects)
		queryset = Character.objects.all()

		#The name to access webservice
		resource_name = 'Character'

		#Allowed methods for this webservice
		allowed_methods = ['get','post','put']

		#Type of authorization (By apikey, public, by login/password). Here, it is public
		authorization= Authorization()
