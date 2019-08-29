from django.shortcuts import render, redirect
from django.contrib import messages
from apps.login_registration.models import *
import datetime
import bcrypt
from django.core.urlresolvers import reverse

def home(request):
    try:
        uid = int(request.session['user_id'])
        context = {
            "user" : User.objects.get(id=uid),
        }
        request.session['current'] = 1
        return render(request, "index/index.html", context)
    except:
        request.session['current'] = 1
        return render(request, "index/index.html")

def reviews(request):
    try:
        uid = int(request.session['user_id'])
        context = {
            "user" : User.objects.get(id=uid),
        }
        request.session['current'] = 2
        return render(request, "index/reviews.html", context)
    except:
        request.session['current'] = 2
        return render(request, "index/reviews.html")

def contact(request):
    try:
        uid = int(request.session['user_id'])
        context = {
            "user" : User.objects.get(id=uid),
        }
        request.session['current'] = 3
        return render(request, "index/contact.html", context)
    except:
        request.session['current'] = 3
        return render(request, "index/contact.html")
