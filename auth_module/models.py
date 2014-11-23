from datetime import timedelta, datetime
from django.utils.crypto import get_random_string

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

class MetadataUserManager(BaseUserManager):

	def create_user(self, email, password, first_name, last_name):
		user = self.model(
			email = email,
			first_name = first_name,
			last_name = last_name,
		)
		user.set_password(password)
		return user

	def create_superuser(self, email, password, first_name, last_name):
		user = self.create_user(email, password, first_name, last_name)
		user.is_superuser = True
		user.is_staff = True
		user.is_manager = True
		user.save()
		return user

class MetadataUser(AbstractBaseUser, PermissionsMixin):

	email = models.EmailField(unique = True, db_index = True)
	first_name = models.CharField(max_length = 70)
	middle_name = models.CharField(max_length = 70, null = True, blank = True)
	last_name = models.CharField(max_length = 70)
	is_manager = models.BooleanField(default = False)
	is_staff = models.BooleanField(default = False)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["first_name", "last_name",]

	objects = MetadataUserManager()

	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __unicode__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

class AccessToken(models.Model):
	user = models.ForeignKey(MetadataUser, related_name="tokens")
	token = models.CharField(max_length="32", null=True, blank=True)
	created = models.DateTimeField(null=True, blank=True)
	expires = models.DateTimeField(null=True, blank=True)

	@staticmethod
	def create_token(user):
		token = get_random_string(length=32)
		AccessToken.objects.create(
			user = user,
			token = token,
			created = datetime.now(),
			expires = datetime.now() + timedelta(days=1)
		)
		return token

	@property
	def is_valid(self):
	    return self.expires < datetime.now()


	def refresh_token(self):
		self.expiry_date = self.expiry_date + timedelta(days=1)

	@staticmethod
	def validate(username, token):
		print "Validating {},{}".format(username, token)
		try:
			user = MetadataUser.objects.get(email = username)
			access_token = AccessToken.objects.get(user = user, token = token)
			if access_token.is_valid:
				print "Valid Access Token"
				return True
		except Exception as e:
			print e
			return False
		print "Invalid Access Token"
		return False

