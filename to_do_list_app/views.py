from django.shortcuts import render, redirect
from to_do_list_app.models import To_Do_List
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from to_do_list_app.models import To_Do_List

# Create your views here.
def home(request):
    data=To_Do_List.objects.all()
    return render(request, 'home.html',{'data':data})


def add_task(request):
    if request.method=="POST":
        title=request.POST.get('title')
        description=request.POST.get('description')

        if title and description:
            To_Do_List.objects.create(title=title, description=description)
            return redirect('home')
    return render(request, 'add_task.html')   


def edit_task(request):
    return render(request,'edit_task.html')     





from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import To_Do_List


# Display all tasks
def home(request):

    data = To_Do_List.objects.all().order_by('-created')

    return render(request, 'home.html', {'data': data})


# Add a new task
def add_task(request):

    if request.method == "POST":

        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()

        if title:
            To_Do_List.objects.create(
                title=title,
                description=description
            )

            return redirect('home')

    return render(request, 'add_task.html')


# Edit an existing task
def edit_task(request, id):

    task = get_object_or_404(To_Do_List, id=id)

    if request.method == "POST":

        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()

        if title:
            task.title = title
            task.description = description

            task.save()

            return redirect('home')

    return render(request, 'edit_task.html', {'task': task})


# Mark task as completed or pending
@require_POST
def complete_task(request, id):

    task = get_object_or_404(To_Do_List, id=id)

    task.done = not task.done

    task.save()

    return redirect('home')


# Delete a task
@require_POST
def delete_task(request, id):

    task = get_object_or_404(To_Do_List, id=id)

    task.delete()

    return redirect('home')


@require_POST
def update_task_status(request, task_id):

    task = get_object_or_404(To_Do_List, id=task_id)

    done_values = request.POST.getlist("done")

    if "true" in done_values:
        task.done = True
    else:
        task.done = False

    task.save()

    return redirect("home")