from django.shortcuts import render

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
    