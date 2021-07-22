from django.forms import ModelForm
from .models import Task
from django import forms

#class for creating model forms

class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = '__all__'

		


