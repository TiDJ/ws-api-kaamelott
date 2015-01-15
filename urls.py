from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^quotes/', include('quotes.urls')),
    url(r'^actors/', include('actors.urls')),
    url(r'^characters/', include('characters.urls')),
)