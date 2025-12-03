from django.urls import path
from . import views

urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name='mark_as_undone'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
]