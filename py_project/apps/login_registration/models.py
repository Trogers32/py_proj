from __future__ import unicode_literals
from django.db import models
from datetime import datetime, timedelta
import bcrypt
import pytz
from validate_email import validate_email
import re


class User_validation(models.Manager):   
    def register_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters long."
        if len(postData['last_name']) < 3:
            errors["last_name"] = "Last name should be at least 2 characters long."
        if User.objects.filter(email=postData['email']).first():
            errors["email"] = "Email already registered."
        elif postData['email'] == '':
            errors["email"] = "Email can't be blank."
        else:
            is_valid = validate_email(postData['email'])
            if is_valid == False:
                errors["email"] = "Invalid email."
            elif not re.match(r"[^@]+@[^@]+\.[^@]+",postData['email']):
                errors["email"] = "Invalid email."
        if len(postData['password']) < 8:
            errors["password"] = "Password needs to be at least 8 characters long."
        elif postData['password'] != postData['confirm_password']:
            errors["password"] = "Passwords do not match."
        return errors

    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            logged_user = user[0] 
            if not bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                errors['pword'] = "Incorrect email or password."
        else:
            errors['pword'] = "Incorrect email or password."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = User_validation()
