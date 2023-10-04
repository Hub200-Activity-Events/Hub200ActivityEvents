from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=50)
#     first_name = models.CharField(max_length=50, null=True , blank=True )
#     last_name = models.CharField(max_length=50, null=True , blank=True)
#     email = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=50)
#     #we might not need an image field for the user
#     image = models.ImageField(upload_to='images/',null=True)
#     password = models.CharField(max_length=50)
#     # attending = models
#     def __str__(self):
#         return f"{self.username}"

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='images/', null=True)

class Events(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50) 
    event_date = models.DateField(default=timezone.now().date(),null=True)
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/',null=True)
<<<<<<< HEAD

=======
>>>>>>> main
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # atendees = models.ManyToManyField(User, related_name="event_atendees", blank=True)
    def __str__(self):
        return f"{self.title}"

class Event_registration(models.Model):
<<<<<<< HEAD
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    guests = models.IntegerField()
=======
    event = models.ForeignKey(Events,on_delete=models.CASCADE,null=True)
    Username = models.CharField(max_length=50, null=True)
    Phonenumber=models.IntegerField(null=True)
    Email=models.EmailField(max_length=254,null=True)
    Location = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    gender=models.CharField(max_length=50,null=True)
    guests = models.CharField(max_length=50,null=True)
>>>>>>> main
    comment = models.CharField(max_length=50)
    status = models.CharField(max_length=50,default="pending")
    def __str__(self):
        return f"{self.event} - {self.Username}"

class Contact_us(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} - {self.email}"