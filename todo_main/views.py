from django.shortcuts import render
from todo.models import Task
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required(login_url='login')
def home(request):
    # Get filter parameters from URL
    search_query = request.GET.get('search', '')
    category_filter = request.GET.get('category', '')
    status_filter = request.GET.get('status', 'active')  # Default to active tasks
    
    # Start with user's tasks
    tasks = Task.objects.filter(user=request.user)
    
    # Apply search filter
    if search_query:
        tasks = tasks.filter(Q(task__icontains=search_query))
    
    # Apply category filter
    if category_filter:
        tasks = tasks.filter(category=category_filter)
    
    # Apply status filter
    if status_filter == 'active':
        tasks = tasks.filter(is_completed=False)
    elif status_filter == 'completed':
        tasks = tasks.filter(is_completed=True)
    # If 'all', don't filter by completion status
    
    # Order by most recently updated
    tasks = tasks.order_by('-updated_at')
    
    # Get completed tasks separately for the completed section
    completed_tasks = Task.objects.filter(is_completed=True, user=request.user)
    
    # Get all categories for the filter dropdown
    categories = Task.CATEGORY_CHOICES
    
    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
        'search_query': search_query,
        'category_filter': category_filter,
        'status_filter': status_filter,
        'categories': categories,
    }
    return render(request, 'home.html', context)