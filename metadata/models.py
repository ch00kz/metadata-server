from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Title(models.Model):
	name = models.CharField(max_length=50,null=True,blank=True)

	def __unicode__(self):
		return u'{}'.format(self.name)

class Gender(models.Model):
	name = models.CharField(max_length=50,null=True,blank=True)

	def __unicode__(self):
		return u'{}'.format(self.name)

class Staff(models.Model):
	title = models.ForeignKey(Title, null=True, blank=True)
	gender = models.ForeignKey(Gender, null=True, blank=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	email = models.CharField(max_length=50,null=True,blank=True)
	office_phone = models.CharField(max_length=50,null=True,blank=True)
	mobile_phone = models.CharField(max_length=50,null=True,blank=True)
	home_phone = models.CharField(max_length=50,null=True,blank=True)
	photo = models.FileField(upload_to="staff_photos/", blank=True, null=True)

class Project(models.Model):
	name = models.CharField(max_length=50,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	expected_start_date = models.DateField(null=True,blank=True)
	actual_start_date = models.DateField(null=True,blank=True)
	expected_end_date = models.DateField(null=True,blank=True)
	actual_end_date = models.DateField(null=True,blank=True)
	expected_cost = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
	actual_cost = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
	department = models.ManyToManyField('Department',null=True,blank=True)

	@property
	def dept_list(self):
		listing = ""
   		for dept in self.department.all():
   			listing += dept.name
   		return listing

   	def __unicode__(self):
   		return u'%s' % self.name

class ProjectLog(models.Model):
	description = models.TextField(null=True, blank=True)
	date_created = models.DateField(null=True,blank=True)
	date_updated = models.DateField(null=True,blank=True)
	assigned_users = models.ManyToManyField(User)

class Action(models.Model):
	user = models.ForeignKey(User, related_name="actions")
	date = models.DateTimeField()
	project = models.ForeignKey('Project', related_name="actions", null=True, blank=True)
	action = models.CharField(max_length=50, null=True, blank=True)

class Department(models.Model):
	name = models.CharField(max_length=50,null=True,blank=True)
	description = models.TextField(null=True,blank=True)

	def __unicode__(self):
		return u'%s' % self.name
