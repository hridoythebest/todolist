from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import TaskModel
from .forms import TaskForm

# Create your views here.



class ShowTasksView(ListView):
    model = TaskModel
    template_name = 'show_tasks.html'
    context_object_name = 'tasks'

class CompletedTasksView(ListView):
    model = TaskModel
    template_name = 'completed_tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return TaskModel.objects.filter(is_completed=True)

class AddTaskView(CreateView):
    model = TaskModel
    form_class = TaskForm
    template_name = 'add_task.html'
    success_url = '/show_tasks'

class EditTaskView(UpdateView):
    model = TaskModel
    form_class = TaskForm
    template_name = 'edit_task.html'
    success_url = '/show_tasks'

class DeleteTaskView(DeleteView):
    model = TaskModel
    template_name = 'delete_task.html'
    success_url = '/show_tasks'

def complete_task(request, pk):
    task = TaskModel.objects.get(id=pk)
    task.is_completed = True
    task.save()
    return redirect('/completed_tasks')
