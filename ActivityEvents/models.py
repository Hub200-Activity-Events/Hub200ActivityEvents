from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',null=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.username}"


class Events(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50) 
    event_date = models.DateField(default=timezone.now().date(),null=True)
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title}"
 
class Event_registration(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth=models.DateField()
    gests = models.IntegerField()
    comment = models.CharField(max_length=50)
    status = models.CharField(max_length=50,default="pending")
    def __str__(self):
        return f"{self.event}"

