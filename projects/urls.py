from django.urls import path

from . import views

urlpatterns = [
    path("projects/", views.project_list, name="project_list"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),
    path("projects/create/", views.project_create, name="project_create"),
    path("projects/delete/<id>", views.project_delete, name="project_delete"),
    path("tasks/", views.task_list, name="task_list"),
    path("tasks/<int:task_id>/", views.task_detail, name="task_detail"),
    path("tasks/create/", views.task_create, name="task_create"),
]