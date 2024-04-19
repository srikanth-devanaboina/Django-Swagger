#Generic
from django.urls import path, include

from app1 import views


urlpatterns = [
    path("student_list", views.StudentList.as_view()),
    path("student_create", views.CreateStudent.as_view()),
    path("student_update", views.UpdateStudent.as_view()),
    path("student_delete/<str:student_id>", views.DeleteStudent.as_view()),
    
]