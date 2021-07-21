from django.conf.urls import path
from . import views


urlpatterns = [

path('', views.index, name='homepage'),
path('update/<int:pk>/', views.update_task, name='update'),
path('create', views.create_task, name='create'),
path('detail<int:pk>', views.get_task, name='detail'),
path('delete/<int:pk>/', delete_task, name='delete')

]