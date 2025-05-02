from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms.widgets import PasswordInput,TextInput
from .models import Course_Available
from django.forms import models


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class UpdateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password']


class CreateCourseForm(models.ModelForm):
    title =forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Course Name', 'class':'form-control'}),label="Enter the course name")
    description =forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Course Description', 'class':'form-control'}),label="Enter course details")
    course_period =forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'4', 'class':'form-control'}),label="Enter the course period")
    class Meta:
        model = Course_Available
        fields = ['title','description','course_period']


