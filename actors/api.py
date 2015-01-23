#!/usr/local/bin/python
# coding: latin-1
from tastypie.resources import ModelResource
from characters.models import *
from characters.api import *
from actors.models import *
from tastypie import fields
from tastypie.resources import ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from cors_resource import *

#Actor resource : File which handles the web service for Actors

class ActorResource(CORSModelResource):

	# We need to re-declare relations between classes who have web services
	character = fields.ToOneField(CharacterResource, 'character', blank=True, null=True, full=True)
	class Meta:
		#Which base data we are returning in GET if no parameters are given (here, all actor objects)
		queryset = Actor.objects.all()
		
		#The name to access webservice
		resource_name = 'Actor'

		#Allowed methods for this webservice
		allowed_methods = ['get','post','put']

		#Type of authorization (By apikey, public, by login/password). Here, it is public
		authorization= Authorization()