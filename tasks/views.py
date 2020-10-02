from django.shortcuts import render

from .models import Task

# Create your views here.
def index(request):
    #### Query de objetos da classe Task e lista deles a ser passada para o front-end
    tasks = []
    query = Task.objects.all()


    ### Adding a new task to the tasks
    new_task = request.POST.get('new_task')
    a = Task(text=new_task)
    a.save()

    ### Removing a task when button pressed


    ###acrecentando o texto dos objetos TASK para uma lista a ser reendenizada no front-end
    for task in query:
        tasks.append(task.text)
    

    ###Context, Dicionario de termos compartilhados entre o front e o back-end
    context = { 'tasks': tasks,
                'new_task': new_task
    }

    return render(request, 'base.html', context)