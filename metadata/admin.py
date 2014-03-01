from django.contrib import admin
from metadata.models import (Project, ProjectLog, Action, Department,UserProfile)
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	list_display = ['name','dept_list','expected_start_date','expected_end_date','actual_start_date','actual_end_date']

class ProjectLogAdmin(admin.ModelAdmin):
	pass

class ActionAdmin(admin.ModelAdmin):
	list_display = ['project','user','action']

class DepartmentAdmin(admin.ModelAdmin):
	list_display=['name',"description"]

class UserProfileAdmin(admin.ModelAdmin):
	list_display=['user',"is_manager"]

admin.site.register(Project,ProjectAdmin)
admin.site.register(ProjectLog,ProjectLogAdmin)
admin.site.register(Action,ActionAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(UserProfile,UserProfileAdmin)