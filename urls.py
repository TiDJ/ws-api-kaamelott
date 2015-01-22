from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^quotes/', include('quotes.urls')),
    url(r'^actors/', include('actors.urls')),
    url(r'^characters/', include('characters.urls')),
)

