# Event registration App | Capstone CS50W

</br>

# Overview

This ia a web application that allows people to register for an event that is happening at the HUB200 (a place in baghdad for aspiring programmers). The web application allows the users to register for the event, view the event details, view the list of people who have registered for the event, and get new updates on new upcoming events.

</br>

# Justification

I consider that this project meets all the expectations raised in the assignment of the CS50W final project, as it is a web platform that implements most of the concepts and techniques taught in the course.

The whole application is based on the Django framework, which allowed managing user authentication, database models, http requests, static files and the page rendering.

The frontend part was made with django templates and javascript, which allowed to render the pages dynamically, and with the help of tailwind and css, the application was made responsive.

The difference between this web application and previous projects is that this application makes use and manages the data to check the events and the people who have registered for the event. This application allows future development and adding new futures such as online events.

- [x] Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza project), and more complex than those.
- [x] Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
- [x] Your web application must be mobile-responsive.

</br>

# Structure

The web platform is structured as follows


- **Hub200ActivityEvents:** The home folder is the main Django app
- **ActivityEvents:** This folder contains the models and funtions relating to the events. making, deleting, filtering and registering for events.

</br>

# File Contents

## Front End:

### HTML files:

The HTML files are the files that are rendered to the client. These files are the ones that are responsible for the front end of the web application. These files are present in the templates folder of the Django web application.

### CSS files:

The CSS files are the files that are responsible for the styling of the web application. These files are present in the static folder of the Django web application.


## Back End:

### Models in the app

There are 6 models for the web application's database.

1. `User` - The built in Django User model.
2. `Events` - Holds the information of the events.
3. `Event_registration` - Holds the information of the registration process.
4. `Contact_us` - Holds the information of the contact us form and all of the messages will be stored here for the admin to see.

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
virtualenv env
pip install -r requirements.txt
python manage.py runserver
```


## For deploying

```json
npm run build
```

</br>

