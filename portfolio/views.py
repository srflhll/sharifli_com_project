from django.shortcuts import render, get_object_or_404
from .models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})


# Create your views here.
def project_detail(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {'project': project}
    return render(request, 'portfolio/project.html', context)
