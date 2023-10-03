from django.contrib import admin
from .models import Events, Event_registration
from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Events)
admin.site.register(Event_registration)