from django.shortcuts import render
from .forms import TaskForm
# Create your views here.
def index(request):
	tasks = Task.objects.all()

	context = {
	'tasks':tasks
	}
	return render(request, 'index.html', context)

def create_task(request):
	task = Task.objects.create()
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	else:
		form = TaskForm()

	return render(request, 'create_task.html', {'form':form})

def get_task(request, pk):
	task = Task.objects.get(pk=pk)

	context = {
	'task':task
	}
	return render(request, 'task_detail.html', context)


def update_task(request, pk):
	task = Task.objects.get(pk=pk)
	form = TaskForm(instance=task)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context ={
        'form':form 
	}
 
	return render(request, 'update.html', context)
def delete_task(request, pk):
	task = Task.objects.get(pk=pk)
	task.delete()
	context = {
	'task':task
	}
	return render(request, 'delete.html')



