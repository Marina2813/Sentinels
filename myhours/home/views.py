from django.shortcuts import render
from .models import Planner
def home(request):
    return render(request, 'index.html')

def viewtasks(request):
    planners = Planner.objects.all()
    context = {'planners': planners}
    return render(request, 'plannerDisplay.html', context)


def addtask(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        time = request.POST['time']
        status = request.POST['status']
        Planner.objects.create(title=title, description=description, status=status, date=date, time=time)
        return render(request, 'index.html')
    return render(request, 'addTask.html')

def login(request):
    return render(request, 'login.html')
def signup(request):
    
    return render(request, 'signup.html')