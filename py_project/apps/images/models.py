from django.db import models
import re
from django.utils import timezone
import os
from uuid import uuid4
from apps.login_registration.models import *

def path_and_rename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Image(models.Model):
  image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
  user = models.ForeignKey(User, related_name="images")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  

