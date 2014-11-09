from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from tastypie.api import Api
from django.contrib import admin
from metadata.api import *

v1_api = Api(api_name='v1')
v1_api.register(StaffResource())
v1_api.register(ProjectResource())
v1_api.register(UserResource())
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^$', RedirectView.as_view(url='admin', permanent=False), name='index'),
    url(r'^api/', include(v1_api.urls)),
)
