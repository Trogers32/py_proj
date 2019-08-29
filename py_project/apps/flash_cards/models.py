from __future__ import unicode_literals
from django.db import models


class Card(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    answered = models.BooleanField(default=False)