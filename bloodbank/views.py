from django.http import HttpResponse
from django.shortcuts import render
from bloodbank.forms import PostForm
from blood.models import Donor

class BloodDonors(ModelForm):  
           class Meta:  
               model = Donor 


def results(request):
	form = PostForm()
	output = BloodDonors();
	return render(request, 'results.html', {'form':form,'output': output})
