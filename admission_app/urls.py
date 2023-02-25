from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('createCourse',views.createCourse,name='createCourse'),
    path('courseDescription/<int:li_id>/',views.coursedesc,name='courseDescription'),
    path('deleteCourse/<int:id>/',views.delete,name='deleteCourse')
]