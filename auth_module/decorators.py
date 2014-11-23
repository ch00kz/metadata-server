from tastypie.exceptions import Unauthorized
from auth_module.models import AccessToken

def verify_token(outer):
	def inner(self, object_list, bundle):
		credentials = bundle.request.META.get("HTTP_AUTHORIZATION", None)
		if credentials:
			credentials = credentials.split(",")
			is_valid = AccessToken.validate(credentials[1], credentials[0])
			if is_valid:
				return outer(self, object_list, bundle)
		else:
			raise Unauthorized
		raise Unauthorized
	return inner
