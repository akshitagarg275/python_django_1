from django.shortcuts import render
from .forms import ProjectForm
# Create your views here.

def projects(request):
    return render(request,'projects/projects.html')


def single_project(request , pk):
    return render(request, 'projects/single_project.html')


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        print(request.POST)
        # form = ProjectForm(request.POST)

    context = {'form':form}
    return render(request , 'projects/project_form.html',context)