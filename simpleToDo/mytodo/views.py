from django.shortcuts import render
from django.utils import timezone
from mytodo.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'mytodo/home.html', {'todo_items': todo_items})

def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=current_date, text=content)
    return HttpResponseRedirect("/")
    



