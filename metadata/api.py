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

		lead_staff = []
		assisting_staff = []
		clients = []

		for staff in obj.lead_staff.all():
			lead_staff.append(staff.full_name)
		bundle.data["lead_staff"] = lead_staff

		for staff in obj.assisting_staff.all():
			assisting_staff.append(staff.full_name)
		bundle.data["assisting_staff"] = assisting_staff

		for client in obj.clients.all():
			clients.append(client.full_name)
		bundle.data["clients"] = clients
		return bundle
