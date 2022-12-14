from django.shortcuts import render
from django.utils import timezone
from mytodo.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('-id')
    context = {'todo_items': todo_items}
    return render(request, 'main/home.html', context) 

def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/")


def delete_todo(request, todo_id):
    if request.method == "POST":
        del_obj = Todo.objects.get(id=todo_id)
        del_obj.delete()


    return HttpResponseRedirect("/")
    



