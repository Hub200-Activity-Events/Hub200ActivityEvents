from django.urls import path


from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("events", views.events, name="events"),
    path("calendar", views.calendar, name="calendar"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("registrations", views.registrations, name="registrations"),
    path("forgotpassword", views.forgotpassword, name="forgotpassword"),
    path("resetpassword", views.resetpassword, name="resetpassword"),
    path("signingupdone", views.signingupdone, name="signingupdone"),
    path("errorpage", views.errorpage, name="errorpage"),
    path("get_events/", views.get_events, name="get_events"),
    path("display_event/<int:event_id>", views.display_event, name="display_event"),
    path("events_details", views.events_details, name="event_details"),
    # path("apply_filter", views.apply_filter, name="apply_filter"),


]
