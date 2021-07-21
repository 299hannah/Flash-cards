from django.shortcuts import render

# Create your views here.
def index(request):
	tasks = Task.objects.all()

	context = {
	'tasks':tasks
	}
	return render(request, 'index.html', context)