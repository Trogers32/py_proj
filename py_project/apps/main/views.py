from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import datetime
import bcrypt
from django.core.urlresolvers import reverse

###########################################################
###########################################################
        # methods for login and registration
###########################################################
###########################################################
def home(request):
    return redirect('/')