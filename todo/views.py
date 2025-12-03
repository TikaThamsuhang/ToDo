from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task, UserProfile
from .forms import UserRegistrationForm, UserUpdateForm, UserProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def addTask(request):
    if request.method == 'POST':
        task = request.POST['task']
        category = request.POST.get('category', 'General')
        due_date = request.POST.get('due_date')
        
        if not due_date:
            due_date = None
            
        Task.objects.create(user=request.user, task=task, category=category, due_date=due_date)
        return redirect('home')
    return redirect('home')

@login_required(login_url='login')
def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = True
    task.save()
    return redirect('home')

@login_required(login_url='login')
def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = False
    task.save()
    return redirect('home')

@login_required(login_url='login')
def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.category = request.POST.get('category', 'General')
        due_date = request.POST.get('due_date')
        if due_date:
            get_task.due_date = due_date
        else:
            get_task.due_date = None
            
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)

@login_required(login_url='login')
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    # Get or create profile for the user
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'profile': profile,
    }
    return render(request, 'profile.html', context)