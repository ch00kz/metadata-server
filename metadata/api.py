from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from metadata.models import Staff
from metadata.authorization import StaffAuthorization


class StaffResource(ModelResource):
	class Meta:
		queryset = Staff.objects.all()
		resource_name = "staff"
		allowed_methods = ['get', 'post']
		serializer = Serializer(formats=['json'])
		authorization = StaffAuthorization()