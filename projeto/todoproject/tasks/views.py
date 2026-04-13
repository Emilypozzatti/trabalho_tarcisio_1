from django.shortcuts import render, redirect
from .models import Task

def home(request):
    tasks = Task.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        Task.objects.create(title=title)

    return render(request, "home.html", {"tasks": tasks})
