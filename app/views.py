from django.shortcuts import render, redirect
from .models import Project, Profile
from .forms import ProjectForm, UpdateUserProfileForm, UpdateUserForm,UserCreationForm
from django.contrib.auth import login, authenticate

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


def  project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST or None, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('index')
    else:
        form = ProjectForm()
    return render(request,'project.html',{"form":form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
