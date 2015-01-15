from django.conf.urls import patterns, include, url
from quotes.api import *
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(QuoteResource())

urlpatterns = patterns('',
	url(r'^api/', include(v1_api.urls)),
)