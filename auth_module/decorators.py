from tastypie.exceptions import Unauthorized
from auth_module.models import AccessToken

def verify_token(outer):
	def inner(self, object_list, bundle):
		credentials = bundle.request.META.get("HTTP_AUTHORIZATION", None)
		if credentials:
			credentials = credentials.split(",")
			check_token = AccessToken.validate(credentials[1], credentials[0])
			if check_token['is_valid']:
				check_token['token'].refresh()
				return outer(self, object_list, bundle)
			else:
				raise Unauthorized
		raise Unauthorized
	return inner
