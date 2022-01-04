from django.contrib import messages
from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class MembershipPlan(models.Model):
    name = models.CharField(max_length=50)
    credit = models.IntegerField()
    valdity = models.CharField(max_length=50)
    price = models.IntegerField()
    offer = models.IntegerField()
    order = models.IntegerField()
    color = models.CharField(max_length=50)
    message = models.CharField(max_length=50)
    tax = models.CharField(max_length=50)
    printedView = models.CharField(max_length=50)
