# Event registration App | Capstone CS50W

</br>

# Overview

This ia a web application that allows people to register for an event that is happening at the HUB200 (a place in baghdad for aspiring programmers). The web application allows the users to register for the event, view the event details, view the list of people who have registered for the event, and get new updates on new upcoming events.

</br>

# Justification

I consider that this project meets all the expectations raised in the assignment of the CS50W final project, as it is a web platform that implements most of the concepts and techniques taught in the course.

The whole application is based on the Django framework, which allowed managing user authentication, database models, http requests, static files and the page rendering.

The Frontend part was made with django templates and javascript, which allowed to render the pages dynamically, and with the help of tailwind and css, the application was made responsive.

In the project, I added several libraries to enhance the user experience. I utilized Leaflet which is a library for displaying maps, to pinpoint Hub200's geographic coordinates. I used video.js to provide a more stylish and user-friendly video player. and also to  create amazing text animations, I implemented Typed.js, which adds an appealing typing effect. Additionally, I integrated Boxicons for high-quality icons and ScrollReveal for smooth and attractive animations throughout the application.


The difference between this web application and previous projects is that this application features a homepage highlighting the importance of events in Hub200 to attract people to join and register for these events. The homepage includes various sections, showcasing what attendees can expect from the events and displaying reviews from previous participants. Additionally, there is a calendar section that makes it easier for users to find upcoming events. The application includes a registration form for individuals interested in participating, which also enables organizers to track event attendance. Furthermore, it includes sign-up and sign-in forms on the same page, using JavaScript to toggle between them for user convenience. This application also allows for future development, with the potential to add new features like online events, event filtering options (weekly, monthly, date range), and a search bar. It aims to validate all forms to prevent users from entering mismatched passwords, invalid email addresses, or incorrect phone numbers, among other features.

- [x] Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza project), and more complex than those.
- [x] Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
- [x] Your web application must be mobile-responsive.

</br>

# Structure

The web platform is structured as follows


- **Hub200ActivityEvents:** The home folder is the main Django app
- **ActivityEvents:** This folder contains the models and funtions relating to the events. making, deleting, filtering and registering for events.
- **media:** all Images on image fields in the database saved in this folder

</br>

# Project Structure

## Front End:

### HTML files:

The HTML files are the files that are rendered to the client. These files are the ones that are responsible for the front end of the web application. These files are present in the templates folder of the Django web application.
+ ./templates/ActivityEvents:
    * calendar.html - This file has been created to display the available events in the calendar.
      ![image](https://github.com/me50/AzizAhsaan/assets/109335694/92e626b3-148a-490e-a8dd-0f5c90acd285)

    * display_event.html - This file has been created to display the event details, including the name, description, date, and other relevant information.
    * ![image](https://github.com/Hub200-Activity-Events/Hub200ActivityEvents/assets/109335694/49cfc94f-a5c7-4a19-b091-09e333a0d08b)
    * ![image](https://github.com/Hub200-Activity-Events/Hub200ActivityEvents/assets/109335694/2e1dd7a8-50e1-4edc-94d7-f6a9e6d9d1ec)
    * ![image](https://github.com/Hub200-Activity-Events/Hub200ActivityEvents/assets/109335694/f5ec2e50-d02c-48c8-a436-76adb1d27ff4)
    * ![image](https://github.com/Hub200-Activity-Events/Hub200ActivityEvents/assets/109335694/ccffde1b-0e9e-4925-bed8-d1f9f8abf483)




    * errorpage.html - This file has been created to display an error page in case the user enters an incorrect login username or password.
      ![image](https://github.com/me50/AzizAhsaan/assets/109335694/2f277df4-c2dc-4490-a27a-3751ba96bff2)

    * events.html - This file has been created to display all the Events in the database and also including filters such weekly,month and range date filter and a searchbar and displaying the number of all events, avaliable events, not avaliable events and also the registered people.
      ![image](https://github.com/me50/AzizAhsaan/assets/109335694/d90b3593-3b3c-4586-a9d1-c07bd06f4868)
      ![image](https://github.com/me50/AzizAhsaan/assets/109335694/afc3f8c7-920c-4474-939b-6af2e691e032)

    * home.html - This file has been created to display the Home Page of Hub200, which showcases the events it offers, provides information about ThursdayHub, and includes PeopleReviews.
    * ![image](https://github.com/Hub200-Activity-Events/Hub200ActivityEvents/assets/109335694/fe72d9b6-1bda-407b-a1d7-dd85f66e759c)
    * ![image](https://github.com/Hub200-Activity-Events/Hub200ActivityEvents/assets/109335694/48a5ff21-c3f7-4e42-968f-2066c536ab5b)
    * ![image](https://github.com/Hub200-Activity-Events/Hub200ActivityEvents/assets/109335694/b40d16bd-f5e9-473b-ae73-385aa0568ad0)
    * ![image](https://github.com/Hub200-Activity-Events/Hub200ActivityEvents/assets/109335694/12473480-1aa0-4e6d-94cf-4099177c36bb)





    * layout.html - This file has been created to display the Header,Body and Footer of the page and contains all the links and cdn.
    * registrations.html - This file has been created to facilitate the registration of people into Hub200's events by guiding them through the process of filling out all the required fields, including their name, phone number, location, and more.
      ![image](https://github.com/me50/AzizAhsaan/assets/109335694/0d5fa7b9-45a4-4d03-8e1c-448646e6600d)

    * signin.html - This file has been created to enable people to log in to the website and also includes the signup form. It has been developed as a single-page application using JavaScript.
    * ![image](https://github.com/Hub200-Activity-Events/Hub200ActivityEvents/assets/109335694/c678d130-3374-446f-86ac-ec3e9cda96a6)
    * ![image](https://github.com/Hub200-Activity-Events/Hub200ActivityEvents/assets/109335694/ce3952ec-6c6b-4cd9-bdf5-84ca33d5ab71)
    * ![image](https://github.com/Hub200-Activity-Events/Hub200ActivityEvents/assets/109335694/866a67c8-3c83-4140-b31a-56d3e56415b5)


    * signingupdone.html - This file has been created to display a thank you note after succussful signing up.
      ![image](https://github.com/me50/AzizAhsaan/assets/109335694/a315360c-ba93-4d4a-8a02-591e1cc063e9)


+ ./static/ActivityEvents:
    * askaquestionhub.png 
    * Contactuscuate.png 
    * error404photo.png 
    * Goodteampana.png 
    * Groupdiscussionamico2.png 
    * hub200logo.png 
    * hub200whitelogo.png
    * hubvideo.mb4 
    * index.js
    * keyracing.png 
    * Knowledgecuate.png 
    * movienight.png 
    * signupdone.png 
    * songhub.png
    * styless.css
    * Teleworkbro.png
    * thursdayhub.png
    * Unknownperson.jpg
    * tabletloginanimate2.svg
    * signupanimate2.svg
    * Formsbro.png
    * thinkingfaceanimate.svg
    * learninganimate.svg
    * collabanimate.svg
    * Smarthomecuate.png
    * Selectingteambro.png
    * calendar2.png
    * communityicon.png
    * securitypin.png

### CSS files:

The CSS files are the files that are responsible for the styling of the web application. These files are present in the static folder of the Django web application.

### JavaScript files:

The JavaScript files are the files that are responsible for creating dynamic webpage and it contains the validation of all the forms in the website and many other features . These files are present in the static folder of the Django web application.



## Back End:

### Models in the app

There are 9 models for the web application's database.

1. `User` - The built in Django User model.
2. `CustomUser` - An abstract user model that extends the base Django User model and includes additional fields such as photo and phone number.
3. `Events` - Holds the information of the events.
4. `Event_registration` - Holds the information of the registration process.
5. `Contact_us` - Holds the information of the contact us form and all of the messages will be stored here for the admin to see.
6. `AskaQuestion` - This model holds fields related to Ask A question form, including name, email, and message.
7. `PeopleReviews` - This model holds fields related to people's reviews, including name, photo, and description.
8. `EventImage` - This model stores Event's images that are displayed in each event.
9. `EventOrganizer` - This model stores Event Organizer's images that are displayed in each event.
### Views and serializers py files:

'views.py' contains the functions for the web application. These view functions sends and receives http request and response. They also combine with serializers to deal with model instances and querysets.

### Manage.py file:

This file is used as a command-line utility and for deploying, debugging, or running the web application.This file contains code for runserver, makemigrations or migrations, etc. that we use in the shell. (Not changing anything here)

### _init_.py files:

This file is empty and remains that way. they are present only to tell that this particular directory is a package. (No changes to this file either)

### settings folder:

This file is present for adding all the applications and the middleware application present. This also has informations about templates and databases. This is present in the main file of the Django web application.

### urls.py files:

This file handles all the URLs of our Django web application. This file contains the lists of all the endpoints that we will have for our web application. Also, this files is like a link to the views in the app with the host web URL.

### wsgi folder:

This file mainly concerns with the WSGI server and is used for deploying the web application on to the servers similar to apache, etc. (No changes to this file as well)

### admin.py files:

Similar to the name of the file, this file is used for registering the models into the django administration. The models that are present have a superuser/admin who can control the information that is being stored. (they are pre-built)

### apps.py files:

This file deals with the application configuration of the apps. The default configuration is sufficient enough in most of the cases.

### models.py files:

This file contains the models of our web application (classes). They are the blueprints of the database we are using and hence contain the information regarding attributes and the fields, etc of the database.

### views.py files:

This files are the crucial ones, it contains all the views. This file can be considered as the file that interacts with the client. This web application uses views with the concept of serializers in the Django Rest_Framework.



# Installation & how to run the application

Run the application in the default port (Django: 8000).
## Backend

```json
# Create a virtual environment:
python -m venv myenv

# Activate the virtual environment (Windows):
myenv\Scripts\activate

# Activate the virtual environment (macOS/Linux):
source myenv/bin/activate

#For installing the requrirements:
pip install -r requirements.txt

# To run the project:
python manage.py runserver
```


## The project is deployed on pythonanywhere
https://azizahsaan.pythonanywhere.com/
