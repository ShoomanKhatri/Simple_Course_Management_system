from django.urls import path
from . import views

urlpatterns = [
    path('student/',views.show_students,name='student'),
    path('addStudent/',views.add_students,name='addStudent'),
    path('editStudent/<int:pk>',views.edit_students,name='editStudent'),
    path('deleteStudent/<int:pk>',views.delete_students,name='deleteStudent'),
]