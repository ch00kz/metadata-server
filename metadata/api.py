# myapp/api.py
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS, ALL
from tastypie.authorization import DjangoAuthorization
from metadata.models import Action, User, Project
from tastypie.serializers import Serializer
from tastypie import fields

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        serializer = Serializer(formats=['json'])

class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        resource_name = 'projects'
        serializer = Serializer(formats=['json'])

class ProjectSnippetResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        fields = ['name', 'id']
        resource_name = 'project-snippets'
        serializer = Serializer(formats=['json'])

class ActionResource(ModelResource):
	user = fields.ForeignKey(UserResource, 'user', full=True, blank=True, null=True)
	project = fields.ForeignKey(ProjectResource, 'project', full=True, blank=True, null=True)
	class Meta:
		queryset = Action.objects.all()
		authorization = DjangoAuthorization()
		resource_name = 'activity'
		serializer = Serializer(formats=['json'])