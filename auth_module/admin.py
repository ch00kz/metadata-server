from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from auth_module.models import MetadataUser
from auth_module.forms import MetadataUserCreationForm, MetadataUserChangeForm

class MedataUserAdmin(UserAdmin):
  	# The forms to add and change user instances
    form = MetadataUserChangeForm
    add_form = MetadataUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_manager')
    list_filter = ('is_manager',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'middle_name','last_name')}),
        ('Permissions', {'fields': ('is_manager','is_superuser')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(MetadataUser, MedataUserAdmin)
admin.site.unregister(Group)