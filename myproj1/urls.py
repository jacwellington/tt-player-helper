from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^forms/', include('form_templates.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
