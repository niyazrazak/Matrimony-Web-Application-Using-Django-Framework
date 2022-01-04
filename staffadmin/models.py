from django.db import models

# Create your models here.


class Admin(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    last_login = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=False)


class HappyStories(models.Model):
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    caption = models.TextField()


class Languages(models.Model):
    name = models.CharField(max_length=50)
