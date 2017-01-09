from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Task
from django.template import RequestContext
from .forms import TasksForm
#from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

def index(request):
	
	if request.method == 'POST':
		form = TasksForm(request.POST)
		if form.is_valid():
			form.save()
			
	
	return render(request, 'toDO/main.html', {'form': TasksForm()})
	
	
def tasks(request):
	task = Task.objects.all()
	return render(request, 'toDo/show.html', {'task':task})

def done(request):
	task = Task.objects.all()
	for t in task:
		t.delete()
	return render(request, 'toDo/done.html')
	
	
def complete(request):
	task = Task.objects.all()
	done_task = task.get(pk=request.POST['done'])
	done_task.isComplete = True
	done_task.save()
	return render(request, 'toDo/main.html', {'task': task})
	'''try:
		done_task = task.get(pk=request.POST['done'])
	except(KeyError, Task.DoesNotExist):
		return render(request, 'toDo/main.html', {
		'task': task,
		'error_message': "You did not select a valid task",
		})
	else:
		done_task.isComplete = True
		done_task.save()
		return render(request, 'toDo/main.html', {'task': task})'''
	
