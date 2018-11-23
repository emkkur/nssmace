from django import forms

from .models import Donor

class PostForm(forms.ModelForm):

	location = forms.CharField(required=False)
	blood_type = forms.CharField(required=False)

	class Meta:
		model = Donor
		fields = ('location', 'blood_type')