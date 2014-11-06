from django.conf.urls import patterns, include, url
from tastypie.api import Api
from django.contrib import admin
from metadata.api import *

v1_api = Api(api_name='v1')
v1_api.register(ActionResource())
v1_api.register(ProjectResource())
v1_api.register(ProjectSnippetResource())
v1_api.register(UserResource())
v1_api.register(StaffResource())
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
