from django.conf.urls import patterns, include, url
from actors.api import *
from tastypie.api import Api


v1_api = Api(api_name='v1')
v1_api.register(ActorResource())

urlpatterns = patterns('',
	url(r'^api/', include(v1_api.urls)),
)