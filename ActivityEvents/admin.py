from django.contrib import admin
from .models import User, Events, Event_registration
# Register your models here.
admin.site.register(User)
admin.site.register(Events)
admin.site.register(Event_registration)