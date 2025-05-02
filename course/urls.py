from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('login/',views.login_user,name='login'),
    path('signup/',views.Signup,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('course/',views.show_courses,name='course'),
    path('addCourse/',views.add_courses,name='addCourse'),
    path('editCourse/<int:pk>',views.edit_courses,name='editCourse'),
    path('deleteCourse/<int:pk>',views.delete_courses,name='deleteCourse'),
]