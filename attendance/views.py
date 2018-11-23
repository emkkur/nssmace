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


def view(request,attendance_id):

	output = Students.objects.filter(unit=unit_id);
	return render(request, 'attendancesheet.html', {'output': output})


def attendances(request,unit_id):

	output = Students.objects.filter(unit=unit_id);
	return render(request, 'attendancesheet.html', {'output': output})

def unit(request,unit_id):
	students = Students.objects.filter(unit=unit_id);
	thisunit = NSSUnits.objects.get(id=unit_id);
	return render(request, 'unit.html', {'students': students,'unit':thisunit})


def student(request,student_id):
	output = Students.objects.get(id=student_id);
	return render(request, 'student.html', {'output': output})