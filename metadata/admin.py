from django.contrib import admin
from metadata.models import *
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['name','dept_list','start_date','expected_end_date','actual_end_date']

class StaffAdmin(admin.ModelAdmin):
	list_display = ['title','first_name','last_name','position','email']

class ActionAdmin(admin.ModelAdmin):
	list_display = ['project','user','action']

class DepartmentAdmin(admin.ModelAdmin):
	list_display=['name']

class ClientAdmin(admin.ModelAdmin):
	list_display = ['title','first_name','last_name','position','email']

admin.site.register(Title)
admin.site.register(Gender)
admin.site.register(Currency)
admin.site.register(ProjectStatus)
admin.site.register(ProjectCategory)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Action,ActionAdmin)
admin.site.register(Department,DepartmentAdmin)
