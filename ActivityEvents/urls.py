from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("events", views.events, name="events"),
    path("calendar", views.calendar, name="calendar"),
    path("registration", views.registration, name="registration"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("forgotpassword", views.forgotpassword, name="forgotpassword"),
    path("resetpassword", views.resetpassword, name="resetpassword"),
    path("signingupdone", views.signingupdone, name="signingupdone"),
    path("errorpage", views.errorpage, name="errorpage"),


]