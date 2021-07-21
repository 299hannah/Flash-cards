from django.db import models

# Create your models here.
class Task(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE)
	title = models.CharField(max_length='200')
	complete = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
