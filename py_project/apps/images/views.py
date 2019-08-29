from django.shortcuts import render, HttpResponse, redirect
from .models import *
from apps.login_registration.models import *
from django.contrib import messages
import bcrypt
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView

def img_sharing(request):
  try:
    context = {
      "user": User.objects.filter(id=int(request.session['user_id'])).first(),
      "img": Image.objects.order_by("-created_at")
    }
    request.session['current'] = 5
    return render(request, "image_uploader/img_sharing.html", context)
  except:
    context = {
      "img": Image.objects.order_by("-created_at")
    }
    request.session['current'] = 5
    return render(request, "image_uploader/img_sharing.html", context)


def uploading_file(request):
  uploaded_file = request.FILES['document']
  user = User.objects.get(id=int(request.session['user_id']))
  Image.objects.create(image=uploaded_file,user=user) 
  return redirect('/image')


def clean_session(request):
  request.session.clear()
  return redirect('/image')