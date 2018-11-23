from django.db import models

class Donor(models.Model):
    bloodgroups = (('O Positive', 'O Positive'),
               ('O Negative', 'O Negative'),
               ('A Positive', 'A Positive'),
               ('A Negative', 'A Negative'),
               ('B Positive', 'B Positive'),
               ('B Negative', 'B Negative'),
               ('AB Negative', 'AB Negative'),
               ('AB Positive', 'AB Positive'),
               )
    genderchoice = (('M', 'Male'),
               ('F', 'Female'),
               ('O', 'Other'),
              )

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=1,choices=genderchoice)
    location = models.CharField(max_length=50)
    blood_type = models.CharField(max_length=30,choices=bloodgroups)
    contact_number = models.CharField(max_length=20)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name