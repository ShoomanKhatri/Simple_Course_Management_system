from django.forms import models
from django import forms
from course.models import Instructor_Available
from course.models import Course_Available



class CreateTeacherForm(models.ModelForm):
    Instructor_name =forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Instructor Name', 'class':'form-control'}),label="Enter the Instructor name")
    course_assigned = forms.ModelChoiceField(
        queryset=Course_Available.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Select the Course Assigned"
    )
    instructor_number =forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'12345', 'class':'form-control'}),label="Enter the instructor number")
    address =forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Address', 'class':'form-control'}),label="Enter the instructor address")
    class Meta:
        model = Instructor_Available
        fields = ['Instructor_name','course_assigned','instructor_number','instructor_number']

