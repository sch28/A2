from django import forms
#from django.forms import ModelForm
from .models import Task

class TasksForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['name']