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

def search_projects(request):
    if 'project' in request.GET and request.GET["project"]:
        search = request.GET.get("project")
        projects = Project.search_by_project_name(search)
        message = f"{search}"
        context = {"projects":projects, 'search':search}
        return render(request, 'result.html',context)
    else:
        message = "You haven't searched for any term"
        return render(request, 'result.html',{"message":message})