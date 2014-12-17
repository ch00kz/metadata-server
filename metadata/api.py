from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from metadata.models import Staff, Project
from metadata.authorization import StaffAuthorization

class StaffResource(ModelResource):
	class Meta:
		queryset = Staff.objects.all()
		resource_name = "staff"
		allowed_methods = ['get', 'post']
		serializer = Serializer(formats=['json'])

class ProjectResource(ModelResource):
	class Meta:
		queryset = Project.objects.all()
		resource_name = "project"
		allowed_methods = ['get', 'post']
		serializer = Serializer(formats=['json'])

	def dehydrate(self, bundle):
		obj = bundle.obj
		bundle.data['currency'] = obj.currency.name if obj.currency else None
		bundle.data['status'] = obj.status.name if obj.status else None
		bundle.data['category'] = obj.category.name if obj.status else None
		bundle.data['departments'] = [ dept.name for dept in obj.department.all() ]
		bundle.data["lead_staff"] = [ staff.full_name for staff in obj.lead_staff.all() ]
		bundle.data["assisting_staff"] = [ staff.full_name for staff in obj.assisting_staff.all() ]
		bundle.data["clients"] = [ client.full_name for client in obj.clients.all() ]
		return bundle
