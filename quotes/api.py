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

class QuoteResource(CORSModelResource):
    character = fields.ForeignKey(CharacterResource, 'character', blank=True, null=True, full=True)
    class Meta:
        queryset = Quote.objects.all()
        resource_name = 'quote'
        allowed_methods = ['get','post','put']
        authorization= Authorization()
        # authentication = CustomApiKeyAuthentication()
        # authorization = DjangoAuthorization()

    def obj_create(self,bundle,request=None,**kwargs):
        print "test"
        #super(obj_create(self,bundle,request=None,**kwargs))
    # def obj_create(self, bundle, request=None, **kwargs):
       
    #     try:
    #     	store = Store.objects.get(id=bundle.data['store_id'])
    #     except:
    #     	raise BadRequest('Magasin non trouvé en base')


    #     if 'title' not in bundle.data:
    #     	raise BadRequest('Veuillez choisir un nom de produit')
    #     title = bundle.data['title']


    #     if 'description' not in bundle.data:
    #     	raise BadRequest('Veuillez renseigner une description')
    #     description = bundle.data['description']


    #     if 'price' not in bundle.data:
    #     	raise BadRequest('Veuillez renseigner un prix')
    #     price = bundle.data['price']

    #     if 'discount' in bundle.data :
    #     	discount = bundle.data['discount']

    #     store = Store.objects.get(id=bundle.data['store_id'])

    #     #Enregistre le magasin
    #     try:
    #         product = Product(title=title, description=description, price=price, discount=discount, store=store)
    #         product.save()
    #     except :
    #         raise BadRequest("Erreur inconnue lors de la création d'un produit")
        
    #     return bundle

