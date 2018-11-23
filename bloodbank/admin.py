from django.contrib import admin
from bloodbank.models import Donor

class Donorpage(admin.ModelAdmin):
	list_display=('name', 'age', 'gender', 'location', 'blood_type', 'contact_number')

admin.site.register(Donor, Donorpage)




# Register your models here.
