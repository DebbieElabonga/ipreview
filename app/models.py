from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.jpg')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
         return self.user.username

class Project(models.Model):
    project_name = models.CharField(max_length=155)
    link = models.URLField(max_length=255)
    details = models.TextField(max_length=255)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="projects")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(upload_to='projectpics/',default='a.png')

    def __str__(self):
        return self.project_name

