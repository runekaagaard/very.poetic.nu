from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'very_poetic_nu.poems.views.index', name='index'),
    url(r'^([0-9]+)$', 'very_poetic_nu.poems.views.poem', name='poem'),
    url(r'^random$', 'very_poetic_nu.poems.views.random', name='random'),
    # url(r'^very_poetic_nu/', include('very_poetic_nu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)
