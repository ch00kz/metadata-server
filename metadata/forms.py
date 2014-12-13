from django.forms import ModelForm
from metadata.models import Project

class ProjectForm(ModelForm):
	class Meta:
		model = Project
