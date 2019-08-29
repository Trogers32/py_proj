from django.db import models
import re
from apps.login_registration.models import *


class UserManager(models.Manager):
  def basic_validator_review(self,postData):
    errors = {}
    if len(postData['name']) < 2:
      errors['name'] = "Need more than 2 characters for name"
    if len(postData['review_text']) < 2:
      errors['review_text'] = "Need more than 2 characters for Review"
    if postData['rating'] == "0":
      errors['rating'] = "Please pick a rating"
    return errors  

class Review(models.Model):
  name = models.CharField(max_length=45)
  text = models.TextField()
  rating = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()