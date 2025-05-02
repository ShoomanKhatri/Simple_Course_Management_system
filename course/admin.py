from django.contrib import admin
from .models import Instructor_Available,Student,Course_Available

# Register your models here.
admin.site.register(Course_Available)
admin.site.register(Instructor_Available)
admin.site.register(Student)


