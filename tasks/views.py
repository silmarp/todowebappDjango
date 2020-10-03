from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Task

# Create your views here.
def index(request):
    #### Query de objetos da classe Task e lista deles a ser passada para o front-end
    tasks = []
    query = Task.objects.all()

    ###acrecentando o texto dos objetos TASK para uma lista a ser reendenizada no front-end
    ###Context, Dicionario de termos compartilhados entre o front e o back-end
    context = { 
        'query': query,
    }

    return render(request, 'base.html', context)

def add_task(request):
    ### Adding a new task to the tasks
    new_task = request.POST['new_task']
    a = Task(text=new_task)
    a.save()

    context = {
        'new_task': new_task,
        
    }

    return HttpResponseRedirect('/')

def remove_task(request, task_id):
    ###removendo task da base de dados
    Task.objects.get(id=task_id).delete()


    
    return HttpResponseRedirect("/")