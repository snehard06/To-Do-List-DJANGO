from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('add/', views.add_task, name='add_task'),

    path('edit/<int:id>/', views.edit_task, name='edit_task'),

    path('complete/<int:id>/', views.complete_task, name='complete_task'),

    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path(
    "update-task-status/<int:task_id>/",
    views.update_task_status,
    name="update_task_status"
),

]
