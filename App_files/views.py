from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from django.contrib.auth import authenticate,login,logout,get_user_model
from .forms import TaskForm
from django.contrib import messages
# Create your views here.

User=get_user_model()

def task_list(request):
    if  request.user.is_authenticated:
        print("task list view called")
        tasks=Task.objects.filter(user=request.user)
        form=TaskForm()
        return render(request,'task_list.html',{"tasks":tasks,"form":form})
    return render(request,"login.html")

def add_task(request):
    if request.method=='POST':
            form=TaskForm(request.POST)
            if form.is_valid():
                new_task=form.save(commit=False)
                new_task.user=request.user
                new_task.save()
                messages.success(request,"Task added successfully!")
    return redirect("task_list")


def Update_task(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,"Task updated successfully!")
        return redirect("task_list")
    else:
        form=TaskForm(instance=task)
    return render(request,'update_task.html',{"form":form})

def delete_task(request,task_id):
    task=get_object_or_404(Task,id=task_id)
    if request.method=="POST":
        if task:
            task.delete()
            messages.success(request,"Task deleted successfully!")
        return redirect("task_list")
    return render(request,"confirm_delete_task.html",{"task":task})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logged in successfully!")
            return redirect("task_list")
        messages.error(request,"Invalid credentials! Please try again.")
    return render(request,'login.html')

def user_sign_up(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=User.objects.filter(username=username)
        if user.exists():
            messages.warning(request,"Username already taken!")
            return render(request,'sign_up.html')
        user=User.objects.create_user(username=username,password=password)
        user.save()
        login(request,user)
        messages.success(request,"User created successfully!")
        return redirect("task_list")
    return render(request,'sign_up.html')

def user_logout(request):
    if request.method=="POST":
        logout(request)
        return redirect("login")
    return redirect("task_list")