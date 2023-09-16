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

def forgotpassword(request):
    return render(request,'ActivityEvents/forgotpassword.html')

def resetpassword(request):
    return render(request,'ActivityEvents/resetpassword.html')

def signingupdone(request):
    return render(request,'ActivityEvents/signingupdone.html') #Maybe you will need to render the signingupdone.html in the signup function(after he comepletes the sign up)

def errorpage(request):
    return render(request,'ActivityEvents/errorpage.html') #Maybe you will need to render the signingupdone.html in the signup function(after he comepletes the sign up)


