from django.contrib.auth import forms
from django.forms import TextInput
from course.models import Student
from django import forms




class CreateStudentForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="Enter Student Name")
    course_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Course Name", "class":"form-control"}), label="Enter the course name")
    course_period = forms.IntegerField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Course Period", "class":"form-control"}), label="Enter course period")
    student_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Student Number", "class":"form-control"}), label="Enter student ID")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="Enter student address")

    class Meta:
        model = Student
        fields = ['name','course_name','course_period','student_number','address']