# coding=utf-8

from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(ur'^$', 'very_poetic_nu.poems.views.index', name='index'),
    url(ur'^([0-9]+)$', 'very_poetic_nu.poems.views.poem', name='poem'),
    url(ur'^¿$', 'very_poetic_nu.poems.views.random', name='random'),
    url(ur'^←$', 'very_poetic_nu.poems.views.logout', name='logout'),
    url(ur'^⊕$', 'very_poetic_nu.poems.views.add', name='add'),
    url(ur'^([0-9]+)/Δ$', 'very_poetic_nu.poems.views.edit', name='edit'),
    url(ur'^([0-9]+)/⊗$', 'very_poetic_nu.poems.views.delete', name='delete'),
    url(ur'^([0-9]+)/⊗⊗$', 'very_poetic_nu.poems.views.restore', name='restore'),
    

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (ur'^→/$', 'django.contrib.auth.views.login'),
)
