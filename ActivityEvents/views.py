from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Events, CustomUser
import datetime
from django.core import serializers
from django.http import JsonResponse
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from .models import Events,Event_registration
<<<<<<< HEAD



# Create your views here.
=======
>>>>>>> main

# Create your views here.
def navigationlinks(request):
    navigation_links = [
        {'text': 'Home', 'href': 'home'},
        {'text': 'Events', 'href': 'events'},
        {'text': 'Calendar', 'href': 'calendar'},
    ]
<<<<<<< HEAD

=======
    
>>>>>>> main
    return render(request, 'ActivityEvents/layout.html', {'navigation_links': navigation_links})


def home(request):
<<<<<<< HEAD
    return render(request, 'ActivityEvents/home.html')



=======
    all_events = Events.objects.only('title', 'description', 'event_date', 'location', 'image')[:3]
    return render(request,'ActivityEvents/home.html', {"all_events":all_events})

def events(request):
    all_events = Events.objects.all()
    next_month = datetime.date.today() + datetime.timedelta(days=30)
    next_week = datetime.date.today() + datetime.timedelta(days=7)
    next_month_events = Events.objects.filter(event_date__range=[datetime.date.today(), next_month])
    next_week_events = Events.objects.filter(event_date__range=[datetime.date.today(), next_week])
    if request.POST.get('filter') == 'next_month':
        return render(request,'ActivityEvents/events.html',{'all_events':next_month_events})
    elif request.POST.get('filter') == 'next_week':
        return render(request,'ActivityEvents/events.html',{'all_events':next_week_events})
    else:
        return render(request,'ActivityEvents/events.html',{'all_events':all_events})


def display_event(request,event_id):
    event = Events.objects.get(id=event_id)
    return render(request,'ActivityEvents/display_event.html',{'event':event})
    #you can use the events details in the html with event.title event.blah blah
>>>>>>> main

def calendar(request):
    return render(request, 'ActivityEvents/calendar.html')

def registrations(request):
<<<<<<< HEAD
    if request.method == 'POST':
=======
    if request.method == 'POST':    
>>>>>>> main
        Username = request.POST.get('UsernameRegistration')
        Phonenumber = request.POST.get('PhonenumberRegistration')
        Email = request.POST.get('EmailRegistration')
        Dateofbirth = request.POST.get('DateofbirthRegistration')
        Location = request.POST.get('LocationRegistration')
        event_id = request.POST.get('EventsRegistration')
        Guests = request.POST.get('GuestsRegistration')
        Comment = request.POST.get('CommentRegistration')

<<<<<<< HEAD
        
        try:
            event = Events.objects.get(pk=event_id)
=======
     
        try:
            events = Events.objects.get(id=event_id)
>>>>>>> main
        except Events.DoesNotExist:
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'Event does not exist'
            })
<<<<<<< HEAD

        else:
            registration = Event_registration(
                 username=Username,
                phone_number=Phonenumber,
                email=Email,
                date_of_birth=Dateofbirth,
                location=Location,
                guests=Guests,
                comment=Comment,
=======
        else:
            registration = Event_registration(
                event = events,
                Username=Username,
                Phonenumber=Phonenumber,
                Email=Email,
                Location = Location,
                date_of_birth = Dateofbirth,
                guests = Guests,
                comment = Comment,
                status = 'pending'
>>>>>>> main
            )
            registration.save()
            return HttpResponseRedirect(reverse('home'))
    else:
<<<<<<< HEAD
        return render(request, 'ActivityEvents/registrations.html')


=======
           all_events = Events.objects.all()
    return render(request, 'ActivityEvents/registrations.html',{
            'all_events': all_events
        })
>>>>>>> main

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('inputsigninemail')
        password = request.POST.get('inputsigninpassword')
        rememberme = request.POST.get('remeberme')
<<<<<<< HEAD
    
=======
        print(rememberme)
>>>>>>> main
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
<<<<<<< HEAD
     
=======
>>>>>>> main




# SIGN UP IS WORKING LETS GOOOOO
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('inputusername')
<<<<<<< HEAD
        # phone_number = request.POST.get('inputphonenumber')
        email = request.POST.get('inputemail')
        password = request.POST.get('inputpassword')
        confirm_password = request.POST.get('inputconfirmpassword')
        # photo = request.FILES.get('inputphoto')]
=======
        phone_number = request.POST.get('inputphonenumber')
        email = request.POST.get('inputemail')
        password = request.POST.get('inputpassword')
        confirm_password = request.POST.get('inputconfirmpassword')
        photo = request.FILES.get('inputphoto')
>>>>>>> main

        if not (username and email and password and confirm_password):
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'please fill all the fields'})
<<<<<<< HEAD
        elif User.objects.filter(username=username).exists():
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'username already exists'})
        elif User.objects.filter(email=email).exists():
=======
        elif CustomUser.objects.filter(username=username).exists():
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'username already exists'})
        elif CustomUser.objects.filter(email=email).exists():
>>>>>>> main
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'email already exists'})
        elif password != confirm_password:
            return render(request, 'ActivityEvents/errorpage.html', {
                'error': 'passwords do not match'})
        else:
<<<<<<< HEAD
            user = User.objects.create_user(username=username, email=email, password=password)
=======
            user = CustomUser.objects.create_user(username=username, email=email, password=password,phone_number=phone_number,photo=photo)
>>>>>>> main
            # user.phone_number = phone_number
            # user.image = photo
            user = authenticate(email=email, password=password)
            user.save()
            if user:
                login(request, user)
                send_welcome_email(email, username)
                return HttpResponseRedirect(reverse('signingupdone'))
    return render(request, 'ActivityEvents/signup.html')
<<<<<<< HEAD


=======
    
>>>>>>> main

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def forgotpassword(request):
    return render(request, 'ActivityEvents/forgotpassword.html')


def resetpassword(request):
    return render(request, 'ActivityEvents/resetpassword.html')


def signingupdone(request):
    return render(request,
                  'ActivityEvents/signingupdone.html')  # Maybe you will need to render the signingupdone.html in the signup function(after he comepletes the sign up)


<<<<<<< HEAD
def errorpage(request):
    return render(request,
                  'ActivityEvents/errorpage.html')  # Maybe you will need to render the signingupdone.html in the signup function(after he comepletes the sign up)
=======
def errorpage(request,  exception=None):
    return render(request,'ActivityEvents/errorpage.html', status=404) #Maybe you will need to render the signingupdone.html in the signup function(after he comepletes the sign up)
>>>>>>> main


# def all_events(request):
#     all_events = Events.objects.all()
#     print(all_events)
#     if request.POST.get('filter') == 'next_month':
#         return render(request, 'ActivityEvents/events.html', {'all_events': next_month_events})
#     elif request.POST.get('filter') == 'next_week':
#         return render(request, 'ActivityEvents/events.html', {'all_events': next_week_events})
#     else:
#         return render(request, 'ActivityEvents/events.html', {'all_events': all_events})


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


<<<<<<< HEAD
=======

>>>>>>> main
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
<<<<<<< HEAD
    email_message = EmailMultiAlternatives(subject, 'this is the plain text version of the email', from_email, to)
    email_message.attach_alternative(html_content, 'text/html')
    email_message.send()


from django.utils import timezone


def apply_filter(request):
    if request.method == 'POST':
        filter_option = request.POST.get('filter')

        if filter_option == 'next_month':
            end_date = timezone.now() + timezone.timedelta(days=30)
            events = Events.objects.filter(event_date__range=[timezone.now(), end_date])
        elif filter_option == 'next_week':
            end_date = timezone.now() + timezone.timedelta(days=7)
            events = Events.objects.filter(event_date__range=[timezone.now(), end_date])
        elif filter_option == 'public':
            events = Events.objects.filter(event_type='public')
        elif filter_option == 'private':
            events = Events.objects.filter(event_type='private')
        elif filter_option == 'range':
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            events = Events.objects.filter(event_date__range=[start_date, end_date])
        else:
            events = Events.objects.all()

        if filter_option in ['next_month', 'next_week', 'range']:
            events = Events.objects.filter(event_date__range=[timezone.now(), end_date])

        context = {'all_events': events, 'filter_option': filter_option}

        return render(request, 'ActivityEvents/events.html', context)

    # If the request method is not POST, simply return all events
    all_events = Events.objects.all()
    return render(request, 'ActivityEvents/events.html', {'all_events': all_events})

def events(request):
    if request.method == 'GET':
        all_events = Events.objects.all()
        return render(request, 'ActivityEvents/events.html', {'all_events': all_events})
=======

    email_message = EmailMultiAlternatives(subject, 'this is the plain text version of the email', from_email, to)
    email_message.attach_alternative(html_content, 'text/html')

    email_message.send()

def apply_filter(request):
    events = Events.objects.all()
>>>>>>> main
