from django.shortcuts import redirect, render
from studentapp.models import Student

# Create your views here.

def get_home_page(request):
    return render(request, 'home.html', context={})

def add_student_view(request):
    return render(request, 'add_students.html', context={})

def save_student_view(request):
    name = request.POST['name']
    age = request.POST['age']
    address = request.POST['address']
    email = request.POST['email']

    print("Name : ", name)
    print("Age : ", age)
    print("Address : ", address)
    print("Email : ", email)

    student = Student(name = name, age = age, address = address, email = email)
    student.save()
    return redirect("all")

def get_all_students(request):
    students = Student.objects.all()
    data = {
        'studentdata': students
    }
    return render(request, 'allstudents.html', context = data)

def single_student_view(request, student_id):
    singlestudent = Student.objects.get(pk = student_id)
    data = {
        'student': singlestudent
    }
    return render(request, 'singlestudent.html', context=data)

def delete_student_view(request, student_id):
    student = Student.objects.filter(pk = student_id)
    student.delete()
    return redirect('all')

def get_student_info(request, student_id):
    student = Student.objects.get(pk = student_id)
    data = {
        'student': student
    }
    return render(request, 'get_student_info.html', context=data)

def update_student(request, student_id):
    student = Student.objects.get(pk = student_id)
    student.name = request.POST['name']
    student.address = request.POST['address']
    student.age = request.POST['age']
    student.email = request.POST['email']
    student.save()
    return redirect('all')
    