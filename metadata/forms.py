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
		self.helper.layout = Layout(
			Div(
				Field('name', ng_model="name"),
				Field('category', ng_model="category"),
				Field('currency', ng_model="currency"),
				css_class="half-screen inline"
			),
			Div(
				Field('start_date', ng_model="start_date"),
				Field('status', ng_model="status"),
				Field('value', ng_model="value"),
				css_class="half-screen inline"
			),
			Div(
				Field('department', ng_model="department"),
				css_class="half-screen inline"
			),
			Div(
				Field('clients', ng_model="clients"),
				css_class="half-screen inline"
			),
			Div(
				Field('description', ng_model="description"),
				css_class="full-screen"
			),
			Div(
				Field('expected_end_date', ng_model="expected_end_date"),
				css_class="half-screen inline"
			),
			Div(
				Field('actual_end_date', ng_model="actual_end_date"),
				css_class="half-screen inline"
			),
			Div(
				Field('lead_staff', ng_model="lead_staff"),
				css_class="half-screen inline"
			),
			Div(
				Field('assisting_staff', ng_model="assisting_staff"),
				css_class="half-screen inline"
			)
		)
