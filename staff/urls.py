from django.urls import path

from staff import views

urlpatterns = [
    path('<int:staff_id>/create_task/', views.CreateTask.as_view()),
    path('<int:task_id>/review_task/', views.ReviewTask.as_view())
]