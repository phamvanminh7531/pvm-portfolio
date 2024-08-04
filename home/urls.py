from django.urls import path
from .views import home, project

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", home, name="home-page"),
    path("project/", project, name="project-page")
]