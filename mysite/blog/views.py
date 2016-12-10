from django.shortcuts import render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import blogEntry

def show_entries(request):

    if request.method == "POST":
        blogEntry.objects.create(name=request.POST.get("todo_name"),
                                 description=request.POST.get("description_name"))

    return render(request, "my_todos.html", {"todos": blogEntry.objects.all()})


def get_entry(request, entry_id):
    try:
        todo = blogEntry.objects.get(id=entry_id)
        return render(request, "detailed_todo.html", {"todo": todo})
    except blogEntry.DoesNotExist:
        raise Http404("We don't have any.")