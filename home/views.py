from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import AboutMeModel, ProjectModel, AchievementModel, HomeButtonModel
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    achievements = AchievementModel.objects.all()
    buttons = HomeButtonModel.objects.all()
    instance = get_object_or_404(AboutMeModel)
    context = {
        "aboutme" : instance,
        "achievements" : achievements,
        "buttons" : buttons
    }
    return render(request, "home/home.html", context=context)

def project(request):
    project_list = ProjectModel.objects.all().order_by('position')
    paginator = Paginator(project_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, "home/project.html", context=context)
