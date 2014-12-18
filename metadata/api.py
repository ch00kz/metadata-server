import json
from django.http import HttpResponse
from django.conf.urls import url
from tastypie.utils import trailing_slash
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

	def prepend_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/create%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('create_project'), name="create_project"),
		]

	def create_project(self, request, **kwargs):
		if request.POST:
			data = json.loads(request.POST['data'])
			name = data.get("name","")
			status = data.get("status","")
			category = data.get("category","")
			start_date = data.get("start_date","")
			expected_end_date = data.get("expected_end_date","")
			end_date = data.get("end_date","")
			value = data.get("value","")
			clients = data.get("clients","")
			departments = data.get("department","")
			currency = data.get("currency","")
			lead_staff = data.get("lead_staff","")

			error = None
			if not name:
				error = "Please give the project a name"
			elif not category:
				error = "Please select a category"
			elif not status:
				error = "Please select a status"
			elif value and not currency:
				error = "Please select a currency"
			elif not departments:
				error = "Please select a department"
			elif not lead_staff:
				error = "Please select a lead staff member"

			if error:
				return HttpResponse(json.dumps(dict(status = False, msg = error)), content_type="application/json")
		return HttpResponse(json.dumps(dict(status = True, project_name = name)), content_type="application/json")

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
