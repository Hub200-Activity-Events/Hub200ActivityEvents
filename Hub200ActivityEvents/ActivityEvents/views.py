from django.shortcuts import render

# Create your views here.

def navigationlinks(request):
    navigation_links = [
        {'text': 'Home', 'href': 'home'},
        {'text': 'Events', 'href': 'events'},
        {'text': 'Calendar', 'href': 'calendar'},
        {'text': 'Registration', 'href': 'registration'},
    ]
    
    
    return render(request, 'ActivityEvents/layout.html', {'navigation_links': navigation_links})
def home(request):
    return render(request,'ActivityEvents/home.html')

def events(request):
    return render(request,'ActivityEvents/events.html')

def calendar(request):
    return render(request,'ActivityEvents/calendar.html')

def registration(request):
    return render(request,'ActivityEvents/registration.html')

def signin(request):
    return render(request,'ActivityEvents/signin.html')

def signup(request):
    return render(request,'ActivityEvents/signup.html')

