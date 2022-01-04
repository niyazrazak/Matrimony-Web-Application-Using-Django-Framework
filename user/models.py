from django.db import models
from django.db.models.fields import TextField

from staffadmin.models import Languages

# Create your models here.


class User(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    phoneNumber = models.BigIntegerField()
    profileFor = models.CharField(max_length=50)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()


class Profiles(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True,
        null=True)
    # basic information
    dob = models.DateField(blank=True,
                           null=True)
    martialStatus = models.CharField(max_length=50, default="never married", blank=True,
                                     null=True)
    motherTounge = models.CharField(max_length=50, blank=True,
                                    null=True)
    religion = models.CharField(max_length=50, blank=True,
                                null=True)
    caste = models.CharField(max_length=50, blank=True,
                             null=True)
    education = models.CharField(max_length=30, blank=True,
                                 null=True)
    income = models.CharField(max_length=30, blank=True,
                              null=True)
    country = models.CharField(max_length=20, blank=True,
                               null=True)
    states = models.CharField(max_length=20, blank=True,
                              null=True)
    city = models.CharField(max_length=20, blank=True,
                            null=True)


# class UserLanguages(models.Model):
#     language = models.CharField(max_length=100)
    # user = models.ForeignKey(
    #     User, on_delete=models.CASCADE, blank=True,
    #     null=True)


class EducationalInfotb(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True,
        null=True)
    qualification = models.CharField(max_length=100, blank=True,
                                     null=True)
    occupation = models.CharField(max_length=100, blank=True,
                                  null=True)
    languagesKnown = models.CharField(max_length=50)

    # languagesKnown = models.ForeignKey(UserLanguages, on_delete=models.CASCADE)


class PhysicalInfotb(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    height = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    complexion = models.CharField(max_length=100, blank=True, null=True)
    bloodGroup = models.CharField(max_length=100, blank=True, null=True)
    bodyType = models.CharField(max_length=100, blank=True, null=True)
    diet = models.CharField(max_length=100, blank=True, null=True)
    smoke = models.CharField(max_length=100, blank=True, null=True)
    drink = models.CharField(max_length=100, blank=True, null=True)
    physicallyImpaired = models.CharField(
        max_length=100, blank=True, null=True)
    dressStyle = models.CharField(max_length=100, blank=True, null=True)


class FamilyInfotb(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True,
        null=True)
    motherName = models.CharField(max_length=20, blank=True, null=True)
    motherOcuupation = models.CharField(max_length=30, blank=True, null=True)
    fatherName = models.CharField(max_length=20, blank=True, null=True)
    fatherOcuupation = models.CharField(max_length=30, blank=True, null=True)
    noofBrothers = models.CharField(
        max_length=20, default=0, blank=True, null=True)
    noofBrothersMarried = models.CharField(
        max_length=20, default=0, blank=True, null=True)
    noofSisters = models.CharField(
        max_length=20, default=0, blank=True, null=True)
    noofSistersMarried = models.CharField(
        max_length=20, default=0, blank=True, null=True)
    familyValue = models.CharField(max_length=20, blank=True, null=True)
    familyStatus = models.CharField(max_length=20, blank=True, null=True)
    familyType = models.CharField(max_length=20, blank=True, null=True)
    familyIncome = models.CharField(max_length=50, blank=True, null=True)
    nativeLocation = models.CharField(max_length=30, blank=True, null=True)
    medicalHistory = models.CharField(max_length=100, blank=True, null=True)


class contactInfotb(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True,
        null=True)
    mobileCode = models.CharField(max_length=50)
    phoneNumber = models.BigIntegerField()
    address = models.CharField(max_length=100)
    residenceIn = models.CharField(max_length=30)
    otherLocation = models.CharField(max_length=30)
    pincode = models.BigIntegerField()
    whatsappCode = models.CharField(max_length=50)
    whatsappNumber = models.BigIntegerField()


class OtherInfotb(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True,
        null=True)
    hobbies = models.CharField(max_length=200)
    interest = models.CharField(max_length=200)
    describedProfile = models.TextField()
    proofType = models.CharField(max_length=30)
    proofNumber = models.CharField(max_length=200)
    # proofFile = models.CharField(max_length=50)


class PatnerPrefertb(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True,
        null=True)
    lookingFor = models.CharField(max_length=200, null=True, blank=True)
    complexion = models.CharField(max_length=200, null=True, blank=True)
    livingIn = models.CharField(max_length=200, null=True, blank=True)
    residentialState = models.CharField(max_length=200, null=True, blank=True)
    ageFrom = models.IntegerField()
    ageTo = models.IntegerField()
    heightFrom = models.CharField(max_length=50, null=True, blank=True)
    heightTo = models.CharField(max_length=50, null=True, blank=True)
    education = models.CharField(max_length=200, null=True, blank=True)
    occupation = models.CharField(max_length=200, null=True, blank=True)
    motherTongue = models.CharField(max_length=200, null=True, blank=True)
    expectation = models.TextField(null=True, blank=True)
    religion = models.CharField(max_length=200, null=True, blank=True)
    caste = models.CharField(max_length=200, null=True, blank=True)


class Photos(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
