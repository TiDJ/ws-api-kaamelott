#!/usr/local/bin/python
# coding: latin-1
from tastypie.resources import ModelResource
from characters.models import *
from tastypie import fields
from tastypie.resources import ALL_WITH_RELATIONS
from tastypie.authorization import Authorization

class CharacterResource(ModelResource):
	class Meta:
		queryset = Character.objects.all()
		resource_name = 'Character'
		allowed_methods = ['get','post','put']
		authorization= Authorization()
        # authentication = CustomApiKeyAuthentication()
        # authorization = DjangoAuthorization()
