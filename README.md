# Take home test questions.
Outcome to deliver: Simple Django app that shows utilization of a Django Rest Framework

### Goals
* Ability to utilize core/built-in functionality of Django and (third party library) Django Rest Framework
* 1-2 Django ORM Models - names / attributes of applicants chosing, at least one model should relate to another
database doesn’t matter, default django db (SQLite) is ok
* DjangoRestFramework views for the django models (standard/stock api actions are enough)
* No need to create a webpage screen - no front end - just code review 

### Review process:

* Set up Github repo and invite dev team members 
* Team is looking for the ability for you to create and implement functional code that  leverages built in functionality of Django and DRF 
* Interactive code review process after merging your submission to simulate interaction model with the team

## Project Design

### Model
The project at present is a simple project that has 2 models:
* Restaurant
* Delivery

There is a one to many relationship between Restaurant and Delivery.

### Authentication
There is basic authentication based on a username/password for a User.

There are basic REST API's for Restaurant and Delivery. At present all API's require authentication.
However there is not any fine access aside from requiring authentication.

## Using the Application

The following sequence of commands will have the appliction ready to use
* \> python manage.py makemigrations gcrestapp
* \> python manage.py migrate
* \> python manage.py createsuperuser
* \> python manage.py runserver

After running these commands, you can login to the application as the superuser at
* http://127.0.0.1:8000/admin/

After logging in as the superuser you will be able create non-superuser users at
* http://127.0.0.1:8000/users
or the admin API also.

