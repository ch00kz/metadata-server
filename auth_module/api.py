from auth_module.models import MetadataUser
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer


class MetadataUserResource(ModelResource):
	class Meta:
		queryset = MetadataUser.objects.all()
		resource_name = "auth/user"
		excludes = ['password','is_staff','is_superuser']
		serializer = Serializer(formats=['json'])