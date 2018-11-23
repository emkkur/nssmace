from django.http import HttpResponse
from django.shortcuts import render
from bloodbank.forms import PostForm
from django.forms import ModelForm
from bloodbank.models import Donor

# class BloodDonors(ModelForm):  
# 	class Meta:
# 		model = Donor
# 		fields = '__all__' 


# def results(request):
# 	form = PostForm()
# 	output = BloodDonors();
# 	return render(request, 'results.html', {'form':form,'output': output})


def results(request):
	form = PostForm()

	output = Donor.objects.all();

	return render(request, 'results.html', {'form':form,'output': output})
