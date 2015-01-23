#!/usr/local/bin/python
# coding: latin-1
from tastypie.resources import ModelResource
from quotes.models import *
from characters.models import *
from characters.api import *
from tastypie import fields
from tastypie.resources import ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from cors_resource import *

#Quote resource : File which handles the web service for quotes

class QuoteResource(CORSModelResource):

    # We need to re-declare relations between classes who have web services
    character = fields.ForeignKey(CharacterResource, 'character', blank=True, null=True, full=True)
    class Meta:

        #Which base data we are returning in GET if no parameters are given (here, all quotes objects)
        queryset = Quote.objects.all()

        #The name to access webservice
        resource_name = 'Quote'
        
        #Allowed methods for this webservice
        allowed_methods = ['get','post','put']
        
        #Type of authorization (By apikey, public, by login/password). Here, it is public
        authorization= Authorization()
        
        #List of fields we are allowed to filter datas returned
        filtering= {
            'character': ALL_WITH_RELATIONS,
        }

    #Override of the obj_create method which is the method called when accessing to a Resource with GET req
    def obj_create(self, bundle, request=None, **kwargs):
        
        #Try to get the character from the character_id given, else raise an error
        try:
            character = Character.objects.get(id=bundle.data['character_id'])
        except:
            raise BadRequest('Personnage non trouvé en base')


        #If title isn't given, raise an error
        if 'title' not in bundle.data:
            raise BadRequest('Veuillez choisir un nom de citation')
        title = bundle.data['title']

        #If content of the quote isn't given, raise an error
        if 'quote' not in bundle.data:
            raise BadRequest('Veuillez renseigner une citation')
        quotetext = bundle.data['quote']

        #Try to save the quote
        try:
            quote = Quote(title=title, quote=quotetext, character=character)
            quote.save()
        except :
            raise BadRequest("Erreur inconnue lors de la création d'une citation")
        
        quotes = Quote.objects.all()

        bundle.data['quotes'] = quotes
        return bundle