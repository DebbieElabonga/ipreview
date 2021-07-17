from django.shortcuts import render
from .models import Project, Profile
# Create your views here.
def index(request):
    project = Project.objects.all()
    return render(request, 'index.html', {'project': project})

def profile(request):
    user = request.user
    profiles = Profile.objects.filter(user=user)
    projects = Project.objects.filter(user = user)
    context = {

        'projects': projects,
        'profiles': profiles,
        
    }
    return render(request, 'profile.html', context)

