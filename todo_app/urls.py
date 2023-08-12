from django.urls import path
from .views import ShowTasksView, CompletedTasksView, AddTaskView, EditTaskView, DeleteTaskView, complete_task




urlpatterns = [
    path('', ShowTasksView.as_view(), name='show_tasks'),
    path('show_tasks', ShowTasksView.as_view(), name='show_tasks'),
    path('completed_tasks', CompletedTasksView.as_view(), name='completed_tasks'),
    path('add_task', AddTaskView.as_view(), name='add_task'),
    path('edit_task/<int:pk>', EditTaskView.as_view(), name='edit_task'),
    path('delete_task/<int:pk>', DeleteTaskView.as_view(), name='delete_task'),
    path('complete_task/<int:pk>', complete_task, name='complete_task'),
]
