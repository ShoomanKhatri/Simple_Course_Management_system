from django.urls import path
from . import views

urlpatterns = [
    path('teacher/',views.show_teacher,name='teacher'),
    path('addTeacher/',views.add_teacher,name='addTeacher'),
    path('editTeacher/<int:pk>',views.edit_teacher,name='editTeacher'),
    path('deleteTeacher/<int:pk>',views.delete_teacher,name='deleteTeacher'),
]