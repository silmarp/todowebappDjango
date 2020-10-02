from django.shortcuts import render

from .models import Task

# Create your views here.
def index(request):
    tasks = ()
    query = Task.objects.all()
    print(query)

    '''
    A query ja funciona, falta só torna-la util
    for task in query:
        task.append(task)
    '''



    return render(request, 'base.html')