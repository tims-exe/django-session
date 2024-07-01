from django.shortcuts import render

# Create your views here.

def get_home_page(request):
    return render(request, 'home.html', context={})

def add_student_view(request):
    return render(request, 'add.html', context={})