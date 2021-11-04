from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from . forms import *

# Create your views here.

def home(request):
    notice = Notice.objects.all()
    attendance = Attendance.objects.all()
    marks = Marks.objects.all()

    context = {
        'notice':notice,
        'attendance':attendance,
        'marks':marks,
    }

    return render(request, 'app/home.html', context)

def addAttendance(request):