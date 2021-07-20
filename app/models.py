from django.db import models
from django.contrib.auth.models import User
import datetime as dt
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='images/', default='default.jpg')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    contact = models.EmailField(max_length=100, blank=True)

    def __str__(self):
         return self.user.username

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

class Project(models.Model):
    project_name = models.CharField(max_length=155)
    link = models.URLField(max_length=255)
    details = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")
    date = models.DateTimeField(auto_now_add=True, blank=True)
    image = models.ImageField(upload_to='projectpics/',default='a.png')
     
    class Meta:
        ordering = ["-pk"]
 
    @classmethod
    def get_projects(cls):
        projects = Project.objects.all()
        return projects

    def __str__(self):
        return self.project_name

    def save_project(self):
        self.save()
    @classmethod
    def search_by_project_name(cls,search):
    	projects = cls.objects.filter(project_name__icontains=search)
    	return projects
    
