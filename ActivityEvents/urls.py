from django.urls import path


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
    # path("display_event/<int:event_id>", views.display_event, name="display_event"),
    # # path("apply_filter", views.apply_filter, name="apply_filter"),


]
