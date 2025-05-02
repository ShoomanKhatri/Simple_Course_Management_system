from django.shortcuts import render,redirect
from .forms import CreateStudentForm
from django.contrib import messages
from course.models import Student


# Create your views here.
from course.models import Student

# Create,edit,delete a student
def show_students(request):
    get_all_student = Student.objects.all()
    return render(request,'Student.html',{
        'students':get_all_student
    })

def add_students(request):
    form = CreateStudentForm()
    if request.method == "POST":
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            messages.success(request,"Student created successfully")
            form.save()
            return redirect('student')
    return render(request,'addStudent.html',{
        'form':form
    })


def edit_students(request,pk):
    if request.user.is_authenticated:
        current_user = Student.objects.get(id=pk)
        form = CreateStudentForm(request.POST or None,instance=current_user)
        if form.is_valid():
            messages.success(request,"Student updated successfully")
            form.save()
            return redirect('student')

        return render(request,'editStudent.html',{
            'form':form
        })
    else:
        messages.success(request,"You must be logged In")
        return redirect('home')

def delete_students(request,pk):
    if request.user.is_authenticated:
        current_user = Student.objects.get(id=pk)
        current_user.delete()
        messages.success(request,"Student deleted successfully")
        return redirect('student')
    else:
        messages.success(request,"You must be logged In")
        return redirect('home')

