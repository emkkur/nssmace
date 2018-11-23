from django.db import models

class Users(models.Model):
    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    studentname = models.CharField(max_length=200)
    nssid = models.TextField()
    unit = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title