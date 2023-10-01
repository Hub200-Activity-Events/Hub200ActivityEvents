from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Events
import datetime
from django.core import serializers
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import Events,Event_registration



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
    return render(request, 'ActivityEvents/home.html')


def events(request):
    all_events = Events.objects.all()
    next_month = datetime.date.today() + datetime.timedelta(days=30)
    next_week = datetime.date.today() + datetime.timedelta(days=7)
    next_month_events = Events.objects.filter(event_date__range=[datetime.date.today(), next_month])
    next_week_events = Events.objects.filter(event_date__range=[datetime.date.today(), next_week])
    if request.POST.get('filter') == 'next_month':
        return render(request, 'ActivityEvents/events.html', {'all_events': next_month_events})
    elif request.POST.get('filter') == 'next_week':
        return render(request, 'ActivityEvents/events.html', {'all_events': next_week_events})
    else:
        return render(request, 'ActivityEvents/events.html', {'all_events': all_events})


def calendar(request):
    return render(request, 'ActivityEvents/calendar.html')

def registrations(request):
    if request.method == 'POST':
        Username = request.POST.get('UsernameRegistration')
        Phonenumber = request.POST.get('PhonenumberRegistration')
        Email = request.POST.get('EmailRegistration')
        Dateofbirth = request.POST.get('DateofbirthRegistration')
        Location = request.POST.get('LocationRegistration')
        event_id = request.POST.get('EventsRegistration')
        Guests = request.POST.get('GuestsRegistration')
        Comment = request.POST.get('CommentRegistration')

        
        try:
            event = Events.objects.get(pk=event_id)
        except Events.DoesNotExist:
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'Event does not exist'
            })

        else:
            registration = Event_registration(
                 username=Username,
                phone_number=Phonenumber,
                email=Email,
                date_of_birth=Dateofbirth,
                location=Location,
                guests=Guests,
                comment=Comment,
            )
            registration.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'ActivityEvents/registrations.html')



def signin(request):
    if request.method == 'POST':
        email = request.POST.get('inputsigninemail')
        password = request.POST.get('inputsigninpassword')
        rememberme = request.POST.get('remeberme')
    
        if not (email and password):
            
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'Please fill in both email and password fields'
            })
        
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            if rememberme:
                request.session.set_expiry(1209600)
            else:
                request.session.set_expiry(0)
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'invalid email or password'})
    else:
        return render(request, 'ActivityEvents/signin.html')
     

    # if request.method == 'POST':
    #     email = request.POST.get('inputsigninemail')
    #     password = request.POST.get('inputsigninpassword')
    #     rememberme= request.POST.get('remeberme')
    #     user = authenticate(request, email=email, password=password)
    #     if user is not None:
    #         if rememberme:
    #             request.session.set_expiry(1209600)
    #         else:
    #             request.session.set_expiry(0)
    #         login(request, user)
    #         return HttpResponseRedirect(reverse('home'))
    #     else:
    #         return render(request,'ActivityEvents/errorpage.html', {
    #             'error':'invalid email or password'})
    # else:
    #     return render(request,'ActivityEvents/signin.html')


# SIGN UP IS WORKING LETS GOOOOO
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('inputusername')
        # phone_number = request.POST.get('inputphonenumber')
        email = request.POST.get('inputemail')
        password = request.POST.get('inputpassword')
        confirm_password = request.POST.get('inputconfirmpassword')
        # photo = request.FILES.get('inputphoto')]

        if not (username and email and password and confirm_password):
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'please fill all the fields'})
        elif User.objects.filter(username=username).exists():
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'username already exists'})
        elif User.objects.filter(email=email).exists():
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'email already exists'})
        elif password != confirm_password:
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'passwords do not match'})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            # user.phone_number = phone_number
            # user.image = photo
            user = authenticate(email=email, password=password)
            user.save()
            if user:
                login(request, user)
                send_welcome_email(email, username)
                return HttpResponseRedirect(reverse('signingupdone'))
    return render(request, 'ActivityEvents/signup.html')

    #     if inputusername == "" or inputphonenumber == "" or inputemail == "" or inputpassword == "" or inputconfirmpassword == "":
    #         return render(request,'ActivityEvents/errorpage.html', {
    #             'error':'please fill all the fields'})
    #
    #     if inputpassword != inputconfirmpassword:
    #         return render(request,'ActivityEvents/errorpage.html',
    #          {'error':'passwords do not match'}
    #          )
    #
    #     try:
    #         user = User.objects.create_user(inputusername,inputemail,inputpassword)
    #         user.phone_number = inputphonenumber
    #         user.image = inputphoto
    #         user.save()
    #     except IntegrityError:
    #         return render(request, "auctions/errorpage.html", {
    #             "message": "Username already taken."
    #         })
    #     login(request, user)
    #     return HttpResponseRedirect(reverse('signingupdone'))
    # else:
    #     return render(request,'ActivityEvents/signup.html')


def forgotpassword(request):
    return render(request, 'ActivityEvents/forgotpassword.html')


def resetpassword(request):
    return render(request, 'ActivityEvents/resetpassword.html')


def signingupdone(request):
    return render(request,
                  'ActivityEvents/signingupdone.html')  # Maybe you will need to render the signingupdone.html in the signup function(after he comepletes the sign up)


def errorpage(request):
    return render(request,
                  'ActivityEvents/errorpage.html')  # Maybe you will need to render the signingupdone.html in the signup function(after he comepletes the sign up)


# this is a function for the date filter next week brings out the events for the next week and next month brings out the events for the next month >shanshal
def all_events(request):
    all_events = Events.objects.all()
    next_month = datetime.date.today() + datetime.timedelta(days=30)
    next_week = datetime.date.today() + datetime.timedelta(days=7)
    next_month_events = Events.objects.filter(event_date__range=[datetime.date.today(), next_month])
    next_week_events = Events.objects.filter(event_date__range=[datetime.date.today(), next_week])
    print(all_events)
    if request.POST.get('filter') == 'next_month':
        return render(request, 'ActivityEvents/events.html', {'all_events': next_month_events})
    elif request.POST.get('filter') == 'next_week':
        return render(request, 'ActivityEvents/events.html', {'all_events': next_week_events})
    else:
        return render(request, 'ActivityEvents/events.html', {'all_events': all_events})


def display_event(request, event_id):
    event = Events.objects.get(id=event_id)
    return render(request, 'ActivityEvents/display_event.html', {'event': event})
    # you can use the events details in the html with event.title event.blah blah


def register_event(request, event_id):
    event = Events.objects.get(id=event_id)
    event.registered_users.add(request.user)
    event.save()
    return HttpResponseRedirect(reverse('display_event', args=(event_id,)))


def get_events(request):
    events = Events.objects.all()
    serialized_events = serializers.serialize('json', events)
    return JsonResponse({'events': serialized_events})


def events_details(request, event_id):
    event = Events.objects.get(id=event_id)
    return render(request, 'ActivityEvents/event_details.html', {'event': event})

def send_welcome_email(email, username):
    subject = 'Welcome to Hub200 Activity Events'
    from_email = 'ahmedmahdii2003@gmail.com'
    to = email
    html_template = get_template('ActivityEvents/email.html')
    context = {'username': username}
    html_content = html_template.render(Context(context))

    email_message = EmailMultiAlternatives(subject, 'this is the plain text version of the email', from_email, to)
    email_message.attach_alternative(html_content, 'text/html')

    email_message.send()

def apply_filter(request):
    events = Events.objects.all()
