from django.shortcuts import render,redirect
from course.models import Instructor_Available
from .forms import CreateTeacherForm
from  course.models import Instructor_Available
from django.contrib import messages


# Create your views here.

# Create,edit,delete a Teacher
def show_teacher(request):
    get_teacher_details = Instructor_Available.objects.all()
    return render(request,'Teacher.html',{
        'teachers':get_teacher_details
    })

def edit_teacher(request,pk):
    if request.user.is_authenticated:
        getTeacher = Instructor_Available.objects.get(id=pk)
        form = CreateTeacherForm(request.POST or None,instance=getTeacher)
        if form.is_valid():
            form.save()
            messages.success(request,'Teacher updated successfully')
            return redirect('teacher')
        return render(request,'editTeacher.html',{
            'form':form
        })
    else:
        messages.success(request,'You have to be logged In')
        return redirect('home')


def add_teacher(request):
    form = CreateTeacherForm()
    if request.method == "POST":
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Teacher added successfully')
            return redirect('teacher')

    return render(request,'addTeacher.html',{
        'form':form
    })

def delete_teacher(request,pk):
    if request.user.is_authenticated:
        getTeacher = Instructor_Available.objects.get(id=pk)
        getTeacher.delete()
        messages.success(request,'Teacher deleted successfully')
        return redirect('teacher')
    else:
        messages.success(request,"You must be logged In")
        return redirect('home')

