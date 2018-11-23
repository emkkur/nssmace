from django import forms

from .models import Donor

class PostForm(forms.ModelForm):

    class Meta:
        model = Donor
        fields = ('location', 'blood_type')