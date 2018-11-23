from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	context = {'username':'sds'}
	return render(request, 'demo.html',context)