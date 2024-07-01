from django.urls import path
from . import views

urlpatterns = [
    path("landingpage", views.get_home_page, name="landingpage"),
    path("add", views.add_student_view, name='add'),
    path("save", views.save_student_view, name='save'),
    path("all", views.get_all_students, name="all"),
    path('student/<int:student_id>/', views.single_student_view, name="getsinglestudent"),
    path('delete/<int:student_id>/', views.delete_student_view, name="deletestudent"),
    path('update/<int:student_id>/', views.get_student_info, name="getstudent"),
    path('update_student/<int:student_id>/', views.update_student, name="updatestudent")
]
