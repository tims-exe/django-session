from django.urls import path
from . import views

urlpatterns = [
    path("landingpage", views.get_home_page, name="landingpage"),
    path("add", views.add_student_view, name='add')
]
