from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ws_kaamelott.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^quotes/', include('quotes.urls')),
    url(r'^actors/', include('actors.urls')),
    url(r'^characters/', include('characters.urls'))
)
