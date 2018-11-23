from django.db import models
from django.contrib.auth.models import User

class NSSUnits(models.Model):
    name = models.CharField(max_length=30)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.id


genderchoice=(("M","Male"),("F","Female"))


class Students(models.Model):
    name = models.CharField(max_length=30)
    admission_no = models.CharField(max_length=11)
    contact_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=1,choices=genderchoice)
    dob = models.DateField()
    unit = models.ForeignKey(NSSUnits, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Attendance(models.Model):

    taken_by = models.ForeignKey(User,on_delete=models.CASCADE);

    # attendance = models.Ma

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name



