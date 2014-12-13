from django.forms import ModelForm
from metadata.models import Project

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Field, Button,HTML,MultiField, Div

class ProjectForm(ModelForm):
	class Meta:
		model = Project

	def __init__(self, *args, **kwargs):
		super(ProjectForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_id = 'form-create-project'
		self.helper.attrs = {'ng-submit': 'createProject()', 'method': ''}
		self.helper.layout = Layout(
			Div(
				Field('name'),
				Field('currency'),
				css_class="half-screen inline"
			),
			Div(
				Field('start_date'),
				Field('value'),
				css_class="half-screen inline"
			),
			Div(
				Field('description'),
				css_class="half-screen inline"
			),
			Div(
				Field('clients'),
				css_class="half-screen inline"
			),
			Div(
				Field('expected_end_date'),
				css_class="half-screen inline"
			),
			Div(
				Field('actual_end_date'),
				css_class="half-screen inline"
			),
			Div(
				Field('lead_staff'),
				css_class="half-screen inline"
			),
			Div(
				Field('assisting_staff'),
				css_class="half-screen inline"
			)
		)
