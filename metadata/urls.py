from django.conf.urls import patterns, include, url
from tastypie.api import Api
from django.contrib import admin
from metadata.api import ActionResource, UserResource,ProjectResource,ProjectSnippetResource

v1_api = Api(api_name='v1')
v1_api.register(ActionResource())
v1_api.register(ProjectResource())
v1_api.register(ProjectSnippetResource())
v1_api.register(UserResource())
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'metadata.views.dashboard', name='welcome'),
    url(r'^login/$', 'metadata.views.auth_login', name='login'),
    url(r'^dashboard/$', 'metadata.views.dashboard', name='dashboard'),
    url(r'^projects/$', 'metadata.views.projects', name='projects'),
    url(r'^calendar/$', 'metadata.views.calendar', name='calendar'),
    url(r'^settings/$', 'metadata.views.settings', name='settings'),

    # other urls
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$', 'metadata.views.auth_logout', name='logout'),
    url(r'^api/', include(v1_api.urls)),
)
