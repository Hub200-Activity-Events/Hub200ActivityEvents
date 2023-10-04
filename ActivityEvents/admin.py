from django.contrib import admin
<<<<<<< HEAD
from .models import Events, Event_registration
# Register your models here.
=======
from .models import Events, Event_registration, Contact_us
from .models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
>>>>>>> main
admin.site.register(Events)
admin.site.register(Event_registration)
admin.site.register(Contact_us)