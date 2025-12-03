from django.db import models

from django.contrib.auth.models import User

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('General', 'General'),
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Shopping', 'Shopping'),
        ('Health', 'Health'),
        ('Education', 'Education'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=250)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='General')
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
