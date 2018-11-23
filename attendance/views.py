from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.forms import ModelForm
from attendance.models import NSSUnits,Students,Attendance
import datetime


def index(request):

	output = NSSUnits.objects.all();
	return render(request, 'attendance.html', {'output': output})

def new(request,unit_id):

	# if(Attendance.objects.filter(unit=unit=unit_id,date=datetime.date.today).exists()):
	# 	return redirect('attendance/unit/'+str(unit_id)+'/view/')

	if request.method == 'POST' and 'attendance' in request.POST:
		studentlist = Students.objects.filter(unit=unit_id);
		newrecord = Attendance()
		for student in studentlist:
			checkbox = 'attend-'+str(student.id)
			if(not checkbox in request.POST):
				stu = Students.objects.get(id=student.id)
				newrecord.absentees.add(stu)
		newrecord.taken_by = request.user
		newrecord.unit = NSSUnits.objects.get(id=unit_id)
		newrecord.save()
		return redirect('attendance/unit/'+str(unit_id)+'/view/')


	output = Students.objects.filter(unit=unit_id);
	return render(request, 'attendancesheet.html', {'output': output})


def view(request,attendance_id):

	output = Attendance.objects.all();
	return render(request, 'attendanceview.html', {'output': len(output)})


def attendances(request,unit_id):

	output = Attendance.objects.filter(unit=unit_id);
	return render(request, 'attendanceview.html', {'output': output})


def unit(request,unit_id):
	students = Students.objects.filter(unit=unit_id);
	thisunit = NSSUnits.objects.get(id=unit_id);
	return render(request, 'unit.html', {'students': students,'unit':thisunit})


def student(request,student_id):
	output = Students.objects.get(id=student_id);
	return render(request, 'student.html', {'output': output})