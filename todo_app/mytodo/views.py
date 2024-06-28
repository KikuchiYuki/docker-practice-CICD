from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Task
from .forms import TaskForm

# Create your views here.
from django.shortcuts import render
from django.views import View
from .models import Task

class IndexView(View):
    def get(self, request):
        # 未完了のタスクを取得
        todo_list = Task.objects.filter(complete=False)
        # 完了したタスクを取得
        completed_tasks = Task.objects.filter(complete=True)
        
        context = {
            'todo_list': todo_list,
            'completed_tasks': completed_tasks
        }
        
        return render(request, 'mytodo/index.html', context)


class AddView(View):
    def get(self, request):
        form = TaskForm()
        # テンプレートのレンダリング処理
        return render(request, "mytodo/add.html", {'form': form})
    
    def post(self, request, *args, **kwargs):
        # 登録処理
        form = TaskForm(request.POST)
        is_valid = form.is_valid()
        
        if is_valid:
            form.save()
            return redirect('/')
        
        return render(request, 'mytodo/add.html', {'form': form})

class UpdateTaskCompleteView(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')
        
        if task_id:
            task = Task.objects.get(id=task_id)
            task.complete = not task.complete
            task.save()
        
        return redirect('/')

class EditTaskView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskForm(instance=task)
        return render(request, 'mytodo/edit.html', {'form': form, 'task': task})
    
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'mytodo/edit.html', {'form': form, 'task': task})
    

class DeleteTaskView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        return render(request, 'mytodo/delete.html', {'task': task})
    
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('index')


# ビュークラスをインスタンス化 
index = IndexView.as_view()
add = AddView.as_view()
update_task_complete = UpdateTaskCompleteView.as_view()
edit_task = EditTaskView.as_view()
delete_task = DeleteTaskView.as_view
