from __future__ import unicode_literals
from django.db import models
from datetime import datetime, timedelta
import bcrypt
import re

#**************************TRIP BUDYDY***********************

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        # CHECKING IF FNAME AND LNAME ARE AT LEAST 2 CHARACTERS
        if len(postData['fname'])<2: 
            errors['fname'] = "First Name should be at least 2 characters."
        if len(postData['lname'])<2: 
            errors['lname'] = "Last Name should be at least 2 characters."
        # CHECKING PASSWORD TO BE 8 CHARACTERS, A NUMBER, CAPITAL, LOWERCASE, AND MATCH
        if len(postData['password'])<8:
            errors['password'] = "Password must be at least 8 characters."
        if postData['password'] != postData['checkpassword']:
            errors['nomatch'] = "Passwords must match."
        if not re.match('.*[0-9]', postData['password']):
            errors['pwnumber'] = "Your password must contain a number"
        if not re.match('.*[A-Z]', postData['password']):
            errors['pwupper'] = "Your password must contain at least 1 upper case character."
        if not re.match('.*[a-z]', postData['password']):
            errors['pwlower'] = "Your password must contain at least 1 lower case character." 
        # CHECKING EMAIL VALID FORMAT AND IN DATABASE
        if not EMAIL_REGEX.match(postData['email']):
            errors['format'] = "Invalid email address."
        if len(User.objects.filter(email=postData['email']))>0:
            errors['inuse'] = "Email in use."
        return errors

    def login_validator(self, postData):
        errors={}
        cemail = postData['email']
        user=User.objects.filter(email=cemail)
        print(user)
        # CHECKING EMAIL IN DATABASE
        if not EMAIL_REGEX.match(postData['email']):
            errors['emailformat'] = "Invalid login."
        if len(user)<1:
            errors['emailnot'] = "Invalid login."
        # CHECKING PASSWORD TO BE 8 CHARACTERS, A NUMBER, CAPITAL, LOWERCASE, AND MATCH
        elif not bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
            errors['pwfail'] = "Invalid login."
        return errors

class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors={}
        print(postData['start_date'])
        print(postData['end_date'])
        # CHECKING DESTINATION and Plan NOT EMPTY AND AT LEAST 3 CHARACTERS
        if len(postData['destination'])<3:
            errors["destination"]= "Destination must be at least 3 characters!"
        if len(postData['plan'])<3:
            errors["plan"]= "Plan must be at least 3 characters!"
        # CHECKING START DATE AND END DATE NOT EMPTY
        if postData['start_date']== '':
            errors['emptystart'] = 'You must include a start date!'
        if postData['end_date']== '':
            errors['emptyend'] = 'You must include an end date!'
        # CHECKING START DATE AND END DATE 
        if postData['end_date']!= '' and postData['start_date']!= '':
            present=datetime.now()
            start =datetime.strptime(postData['start_date'], '%Y-%m-%d')
            end =datetime.strptime(postData['end_date'], '%Y-%m-%d')
            if start < present:
                errors['startdate']= "Start date must be in the future, time travel is not allowed!"
            if end < start:
                errors['enddate']= "End date must be after start date, time travel is not allowed!"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name =models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    password =models.CharField(max_length=255)
    created_at =models.DateField(auto_now_add=True)
    updated_at =models.DateField(auto_now=True)
    objects =UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    plan = models.TextField()
    planner = models.ForeignKey(User, related_name='my_trips')
    guest = models.ManyToManyField(User, related_name='trips')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects =TripManager()