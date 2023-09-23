from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Events
import datetime
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
    if request.method == 'POST':
        email = request.POST.get('inputsigninemail')
        password = request.POST.get('inputsigninpassword')
        rememberme= request.POST.get('remeberme')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if rememberme:
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request,'ActivityEvents/errorpage.html', {
                'error':'invalid email or password'})
    else:
        return render(request,'ActivityEvents/signin.html')

def signup(request):
    if request.method == 'POST':
        inputusername = request.POST.get('inputusername')
        inputphonenumber = request.POST.get('inputphonenumber')
        inputemail = request.POST.get('inputemail')
        inputpassword = request.POST.get('inputpassword')
        inputconfirmpassword = request.POST.get('inputconfirmpassword')
        inputphoto = request.FILES.get('inputphoto')
        
        if inputusername == "" or inputphonenumber == "" or inputemail == "" or inputpassword == "" or inputconfirmpassword == "":
            return render(request,'ActivityEvents/errorpage.html', {
                'error':'please fill all the fields'})
        
        if inputpassword != inputconfirmpassword:
            return render(request,'ActivityEvents/errorpage.html',
             {'error':'passwords do not match'}
             )
          
        try:
            user = User.objects.create_user(inputusername,inputemail,inputpassword)
            user.phone_number = inputphonenumber
            user.image = inputphoto
            user.save()
        except IntegrityError:
            return render(request, "auctions/errorpage.html", {
                "message": "Username already taken."
            })  
        login(request, user)
        return HttpResponseRedirect(reverse('signingupdone'))
    else:
        return render(request,'ActivityEvents/signup.html')
    

def forgotpassword(request):
    return render(request,'ActivityEvents/forgotpassword.html')

def resetpassword(request):
    return render(request,'ActivityEvents/resetpassword.html')

def signingupdone(request):
    return render(request,'ActivityEvents/signingupdone.html') #Maybe you will need to render the signingupdone.html in the signup function(after he comepletes the sign up)

def errorpage(request):
    return render(request,'ActivityEvents/errorpage.html') #Maybe you will need to render the signingupdone.html in the signup function(after he comepletes the sign up)





#this is a function for the date filter next week brings out the events for the next week and next month brings out the events for the next month >shanshal
# def all_events(request):
#     all_events = Events.objects.all()
#     next_month = datetime.date.today() + datetime.timedelta(days=30)
#     next_week = datetime.date.today() + datetime.timedelta(days=7)
#     next_month_events = Events.objects.filter(event_date__range=[datetime.date.today(), next_month])
#     next_week_events = Events.objects.filter(event_date__range=[datetime.date.today(), next_week])
#     if request.POST.get('filter') == 'next_month':
#         return render(request,'ActivityEvents/all_events.html',{'all_events':next_month_events})
#     elif request.POST.get('filter') == 'next_week':
#         return render(request,'ActivityEvents/all_events.html',{'all_events':next_week_events})
#     else:
#         return render(request,'ActivityEvents/all_events.html',{'all_events':all_events})


# def display_event(request,event_id):
#     event = Events.objects.get(id=event_id)
#     return render(request,'ActivityEvents/display_event.html',{'event':event})
#     #you can use the events details in the html with event.title event.blah blah



# def register_event(request,event_id):
#     event = Events.objects.get(id=event_id)
#     event.registered_users.add(request.user)
#     event.save()
#     return HttpResponseRedirect(reverse('display_event',args=(event_id,)))
