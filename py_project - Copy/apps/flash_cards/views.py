from django.shortcuts import render, redirect
from django.contrib import messages
from apps.login_registration.models import *
from .models import *
import datetime
import bcrypt
from django.core.urlresolvers import reverse

def home(request):
    try:
        if 'correct' not in request.session:
            request.session['correct'] = 0
        if 'wrong' not in request.session:
            request.session['wrong'] = 0
        if 'count' not in request.session:
            request.session['count'] = 0
        if 'subject' not in request.session:
            request.session['subject'] = "Life"
        sub = request.session['subject']
        c = Card.objects.filter(subject=sub).filter(answered="False")
        if 'left' not in request.session:
            request.session['left'] = len(c)
        uid = int(request.session['user_id'])
        request.session['left'] = len(c)
        context = {
            "user" : User.objects.get(id=uid),
            "questions" : Card.objects.filter(subject=sub).filter(answered="False"),
            "subject" : request.session['subject'],
        }
        request.session['current'] = 4
        return render(request, "flash/flash.html", context)
    except:
        if 'correct' not in request.session:
            request.session['correct'] = 0
        if 'wrong' not in request.session:
            request.session['wrong'] = 0
        if 'count' not in request.session:
            request.session['count'] = 0
        if 'subject' not in request.session:
            request.session['subject'] = "Life"
        sub = request.session['subject']
        c = Card.objects.filter(subject=sub).filter(answered="False")
        if 'left' not in request.session:
            request.session['left'] = len(c)
        request.session['left'] = len(c)
        context = {
            "questions" : Card.objects.filter(subject=sub).filter(answered="False"),
            "subject" : request.session['subject'],
        }
        request.session['current'] = 4
        return render(request, "flash/flash.html", context)

def change(request):
    del request.session['left']
    del request.session['correct']
    del request.session['wrong']
    del request.session['count']
    request.session['subject'] = request.POST['subject']
    return redirect("/flash")

def answer(request):
    try:
        sub = request.session['subject']
        c = Card.objects.filter(subject=sub).filter(answered="False")
        if request.POST['ans'] == c.first().answer:
            request.session['correct'] += 1
        else:
            request.session['wrong'] += 1
        request.session['left'] -= 1
        uid = int(request.session['user_id'])
        context = {
            "user" : User.objects.get(id=uid),
            "questions" : Card.objects.filter(subject=sub).filter(answered="False"),
        }
        return render(request, "flash/answer.html", context)
    except:
        sub = request.session['subject']
        c = Card.objects.filter(subject=sub).filter(answered="False")
        if request.POST['ans'] == c.first().answer:
            request.session['correct'] += 1
        else:
            request.session['wrong'] += 1
        request.session['left'] -= 1
        context = {
            "questions" : Card.objects.filter(subject=sub).filter(answered="False"),
        }
        return render(request, "flash/answer.html", context)

def next(request):
    sub = request.session['subject']
    c = Card.objects.filter(subject=sub).filter(answered="False")
    c = c.first()
    c.answered = "True"
    c.save()
    return redirect('/flash')

def reset(request):
    del request.session['left']
    del request.session['correct']
    del request.session['wrong']
    del request.session['count']
    c = Card.objects.all()
    for i in c:
        i.answered = "False"
        i.save()
    return redirect("/flash")