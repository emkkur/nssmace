from django.contrib import admin
from attendance.models import Students,NSSUnits

class NSSUnitsPage(admin.ModelAdmin):
	list_display=[field.name for field in NSSUnits._meta.fields if field.name != "id"]

class StudentsPage(admin.ModelAdmin):
	list_display=[field.name for field in Students._meta.fields if field.name != "id"]

admin.site.register(NSSUnits, NSSUnitsPage)
admin.site.register(Students, StudentsPage)

