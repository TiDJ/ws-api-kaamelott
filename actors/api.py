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

class ActorResource(CORSModelResource):
#class ActorResource(ModelResource):
	character = fields.ToOneField(CharacterResource, 'character', blank=True, null=True, full=True)
	class Meta:
		queryset = Actor.objects.all()
		resource_name = 'Actor'
		allowed_methods = ['get','post','put']
		authorization= Authorization()
        # authentication = CustomApiKeyAuthentication()
        # authorization = DjangoAuthorization()
