from django.db import models

class NSSUnits(models.Model):
    name = models.CharField(max_length=30)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=30)
    adno = models.CharField(max_length=30)
    contact_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=1,choices=genderchoice)
    dob = models.CharField(max_length=10)
    unit_number = models.CharField(max_length=3)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

