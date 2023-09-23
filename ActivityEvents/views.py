from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse

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

def registrations(request):
    print(request.method)
    if request.method == 'POST':
        UsernameRegistration = request.POST.get('UsernameRegistration')
        PhonenumberRegistration = request.POST.get('PhonenumberRegistration')
        EmailRegistration = request.POST.get('EmailRegistration')
        DateofbirthRegistration = request.POST.get('DateofbirthRegistration')
        LocationRegistration = request.POST.get('LocationRegistration')
        EventsRegistration = request.POST.get('EventsRegistration')
        gender = request.POST.get('gender')
        GuestsRegistration = request.POST.get('GuestsRegistration')
        CommentRegistration = request.POST.get('CommentRegistration')
        print(UsernameRegistration)
        print(PhonenumberRegistration)
        print(EmailRegistration)
        print(DateofbirthRegistration)
        print(LocationRegistration)
        print(EventsRegistration)
        print(gender)
        print(GuestsRegistration)
        print(CommentRegistration)
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request,'ActivityEvents/registrations.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('inputsigninemail')
        password = request.POST.get('inputsigninpassword')
        rememberme= request.POST.get('remeberme')
        return HttpResponseRedirect(reverse('home'))
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

        
        print(f'Username: {inputusername}')
        print(f'Phone Number: {inputphonenumber}')
        print(f'Email: {inputemail}')
        print(f'Password: {inputpassword}')
        print(f'Confirm Password: {inputconfirmpassword}')
        print(f'image: {inputphoto}')


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


