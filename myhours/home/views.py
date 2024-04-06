from django.shortcuts import render
from .models import Planner
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def update_task_status(request):
    data = json.loads(request.body)
    task = Planner.objects.get(id=data['task_id'])
    task.status = data['new_status']  # Changed from 'completed' to 'new_status'
    task.save()
    return JsonResponse({'status': 'ok'})
def home(request):
    return render(request, 'index.html')

def viewtasks(request):
    planners = Planner.objects.all()
    context = {'planners': planners}
    todo_tasks = Planner.objects.filter(status='todo')
    completed_tasks = Planner.objects.filter(status='complete')
    return render(request, 'plannerDisplay.html', {'context':context, 'todo_tasks': todo_tasks,  'completed_tasks': completed_tasks})


def addtask(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        time = request.POST['time']
        Planner.objects.create(title=title, description=description, date=date, time=time)
        return render(request, 'index.html')
    return render(request, 'addTask.html')

def login(request):
    return render(request, 'login.html')
def signup(request):
    
    return render(request, 'signup.html')