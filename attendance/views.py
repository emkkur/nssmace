from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from attendance.models import NSSUnits,Students


def index(request):

	output = NSSUnits.objects.all();
	return render(request, 'attendance.html', {'output': output})

def new(request,unit_id):

	output = Students.objects.filter(unit=unit_id);
	return render(request, 'attendancesheet.html', {'output': output})


def view(request,unit_id):

	output = Students.objects.filter(unit=unit_id);
	return render(request, 'attendancesheet.html', {'output': output})

def unit(request,unit_id):
	output = Students.objects.filter(unit=unit_id);
	return render(request, 'attendancesheet.html', {'output': output})
