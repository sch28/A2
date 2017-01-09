from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Task(models.Model):
	name = models.CharField(max_length = 2500)
	isComplete = models.BooleanField(default = False)
	def __str__(self):
		return self.name
	#def get_absolute_url(self):
	#	return reverse('toDo:main', kwargs={'pk': self.pk})