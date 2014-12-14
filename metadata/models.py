from django.db import models
from auth_module.models import MetadataUser
from django.db.models.signals import post_save

class Title(models.Model):
	name = models.CharField(max_length = 50, null = True, blank =True)

	def __unicode__(self):
		return u'{}'.format(self.name)

class Gender(models.Model):
	name = models.CharField(max_length=50,null=True,blank=True)

	def __unicode__(self):
		return u'{}'.format(self.name)

class Department(models.Model):
	name = models.CharField(max_length=50,null=True,blank=True)

	def __unicode__(self):
		return u'{}'.format(self.name)

class Staff(models.Model):
	title = models.ForeignKey(Title, null=True, blank=True)
	gender = models.ForeignKey(Gender, null=True, blank=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	position = models.CharField(max_length=50)
	email = models.CharField(max_length=50, null=True, blank=True)
	office_phone = models.CharField(max_length=50, null=True, blank=True)
	mobile_phone = models.CharField(max_length=50, null=True, blank=True)
	home_phone = models.CharField(max_length=50, null=True, blank=True)
	photo = models.FileField(upload_to="staff_photos/", blank=True, null=True)
	department = models.ForeignKey(Department, null=True, blank=True)

	@property
	def full_name(self):
	    return "{} {}".format(self.first_name, self.last_name)

	def __unicode__(self):
		return u'{} {} {}'.format(self.title, self.first_name, self.last_name)

class Client(models.Model):
	title = models.ForeignKey(Title, null=True, blank=True)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	entity = models.CharField(max_length=80)
	position = models.CharField(max_length=50)
	email = models.CharField(max_length=50, null=True, blank=True)
	office_phone = models.CharField(max_length=50, null=True, blank=True)
	mobile_phone = models.CharField(max_length=50, null=True, blank=True)
	home_phone = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self):
		return u'{} {} {}'.format(self.title, self.first_name, self.last_name)

class ProjectStatus(models.Model):
	name = models.CharField(max_length = 50, null = True, blank =True)
	description = models.TextField(null = True, blank =True)

	def __unicode__(self):
		return u'{}'.format(self.name)

class ProjectCategory(models.Model):
	name = models.CharField(max_length = 50, null = True, blank =True)
	description = models.TextField(null = True, blank =True)

	def __unicode__(self):
		return u'{}'.format(self.name)

class Currency(models.Model):
	name = models.CharField(max_length = 50, null = True, blank =True)
	to_jmd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

	def __unicode__(self):
		return u'{}'.format(self.name)

class Project(models.Model):
	name = models.CharField(max_length=50,null=True,blank=True)
	status = models.ForeignKey(ProjectStatus, null=True, blank=True)
	category = models.ForeignKey(ProjectCategory, null=True, blank=True)
	currency = models.ForeignKey(Currency, null=True, blank=True)
	value = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
	clients = models.ManyToManyField(Client, null=True, blank=True)
	lead_staff = models.ManyToManyField(Staff, related_name='lead_projects', null=True, blank=True)
	assisting_staff = models.ManyToManyField(Staff, related_name='assisting_projects', null=True, blank=True)
	description = models.TextField(null=True,blank=True)
	start_date = models.DateField(null=True,blank=True)
	expected_end_date = models.DateField(null=True,blank=True)
	actual_end_date = models.DateField(null=True,blank=True)
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
	deleted = models.BooleanField(default=False)

class Action(models.Model):
	user = models.ForeignKey(MetadataUser, related_name="actions")
	date = models.DateTimeField()
	project = models.ForeignKey('Project', related_name="actions", null=True, blank=True)
	project_log = models.ForeignKey('ProjectLog', related_name="actions", null=True, blank=True)
	action = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self):
		return u'%s' % self.name
