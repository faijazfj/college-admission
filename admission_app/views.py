from django.shortcuts import render,redirect
from .models import *
from .forms import *


# Create your views here.

def home(request):

    obj = Details.objects.all()
    return render(request,'main.html',{'obj':obj})


def createCourse(request):
    form = Addform()
    if request.method == 'POST':
        form =Addform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('createCourse')
    return render(request,'createCourse.html',{'form':form})


def coursedesc(request,li_id):
    obj =Details.objects.get(id=li_id)

    return render(request,'description.html',{'obj':obj})


def delete(request,id):
    course = Details.objects.get(id=id)
    if request.method=='POST':
        course.delete()
        return redirect('/')

    return render(request,'delete.html',{'course':course})




