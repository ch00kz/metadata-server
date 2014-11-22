from django.contrib.auth import authenticate, login, logout
from django.conf.urls import url
from tastypie.utils import trailing_slash
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from auth_module.models import MetadataUser, AccessToken

class MetadataUserResource(ModelResource):
	class Meta:
		queryset = MetadataUser.objects.all()
		resource_name = "auth/user"
		excludes = ['password','is_staff','is_superuser']
		allowed_methods = ['get', 'post']
		serializer = Serializer(formats=['json'])

	def prepend_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/login%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('login'), name="api_login"),
		]

	def login(self, request, **kwargs):
		self.method_check(request,allowed=['post'])
	 	data = request.POST
		username = data.get('username')
		password = data.get('password')
		user = authenticate(username=username, password=password)

		if not user:
	 		return self.create_response(request, { 'status': False })

		token = AccessToken.create_token(user)
	 	return self.create_response(request, { 'status': True, 'access_token': token })


