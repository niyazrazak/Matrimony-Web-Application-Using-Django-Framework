from django.shortcuts import render, redirect
from .models import *
from user .models import *
from random import random
from django.http import JsonResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

# Create your views here.


def smartLogin(request):
    return render(request, 'smartlogin.html')


def loginAdmin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email == 'admin@demo.com' and password == '123456':
            request.session['admin'] = '111'
            print("admin logged in")
            return redirect('homeadmin')
        else:
            adminStaff = Admin.objects.filter(
                email=email, password=password).exists()
            if adminStaff:
                adminUser = Admin.objects.get(email=email, password=password)
                request.session['staff'] = adminUser.id
                Admin.objects.get(id=adminUser.id)
                print("Staff Logged In")
                return render(request, 'staffhome.html')
            else:
                messages.error(request, 'Invalid Email Id or Password')
                return redirect('smartlogin')
    return redirect('smartlogin')


def logoutStaff(request):
    try:
        del request.session['staff']
        print("staff logged out")
        return redirect('smartlogin')
    except:
        return redirect('smartlogin')


def indexStaff(request):
    return render(request, 'indexstaff.html')


def homeStaff(request):
    request.session['staff']
    return render(request, 'staffhome.html')


def filteruserStaff(request):
    return render(request, 'filteruser.html')


def moreStaff(request):
    return render(request, 'morestaff.html')


def profilepremiumStaff(request):
    return render(request, 'profilepremium.html')


def unapproveduserStaff(request):
    return render(request, 'unapproveduser.html')


def userprofilesStaff(request):
    return render(request, 'userprofiles.html')


def freeuserStaff(request):
    return render(request, 'freeuser.html')


def silveruserStaff(request):
    return render(request, 'silveruser.html')


def golduserStaff(request):
    return render(request, 'golduser.html')


def diamonduserStaff(request):
    return render(request, 'diamonduser.html')


def settingStaff(request):
    return render(request, 'settingsstaff.html')


def profileStaff(request):
    return render(request, 'staffprofile.html')


def requestcontactStaff(request):
    return render(request, 'requestcontact.html')


def happystoriesStaff(request):
    return render(request, 'happystories.html')


def addstoriesStaff(request):
    if request.method == 'POST':
        name = request.POST['name']
        file = request.FILES['propic']
        caption = request.POST['caption']
        print(name)
        print(file)
        print(caption)
        file_name = str(random())+file.name
        print(file_name)
        obj1 = FileSystemStorage()
        obj1.save(file_name, file)
        obj2 = HappyStories(name=name, image=file_name, caption=caption)
        obj2.save()
        print("image added")
        return redirect('happystories')


def addOptions(request):
    return render(request, 'addoptions.html')

# def Staff(request):
#     return render(request,'.html')

# def Staff(request):
#     return render(request,'.html')
