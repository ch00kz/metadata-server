from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from metadata.models import Staff


class StaffResource(ModelResource):
	class Meta:
		queryset = Staff.objects.all()
		resource_name = "staff"
		allowed_methods = ['get', 'post']
		serializer = Serializer(formats=['json'])