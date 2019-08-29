from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
import bcrypt
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView

def index(request):
    return render(request, "my_apps/index.html")

def contact(request):
  return render(request, "my_apps/contact.html")

def reviews(request):
  context = {
    "all_reviews": Review.objects.order_by("-created_at")
  }
  return render(request, 'my_apps/reviews.html', context)

def taking_review(request):
  errors = Review.objects.basic_validator_review(request.POST)
  if len(errors) > 0:
    for key,value in errors.items():
      messages.error(request, value)
    return redirect('/paint/reviews')
  else:
    name = request.POST['name']
    rating = request.POST['rating']
    text = request.POST['review_text']
    add_review = Review.objects.create(name=name,text=text,rating=rating)
  return redirect("/paint/reviews")

def cars_home(request):
  return render(request, "my_apps/cars_home.html")