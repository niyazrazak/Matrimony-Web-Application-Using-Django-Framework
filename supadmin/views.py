from django.shortcuts import redirect, render
from . models import *
from staffadmin .models import *
from user .models import *
from django.contrib import messages
from django.contrib import auth
import datetime
from random import random
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.


def indexadm(request):
    admin_id = request.session['admin']
    return render(request, 'indexadmin.html')


def homeAdmin(request):
    admin_id = request.session['admin']
    print(admin_id)
    return render(request, 'homeadmin.html')


def logoutAdmin(request):
    try:
        del request.session['admin']
        return render(request, 'smartlogin.html')
    except:
        return render(request, 'smartlogin.html')


def allprofilesAdmin(request):
    allUser = User.objects.all()
    context = {'user': allUser}
    return render(request, 'allprofiles.html', context)


def premiumprofilesAdmin(request):
    return render(request, 'premiumprofiles.html')


def unapprovedrequestAdmin(request):
    user = User.objects.all()
    context = {'user': user}
    return render(request, 'unapprovedrequest.html', context)


def membershipplanAdmin(request):
    plan = MembershipPlan.objects.all
    context = {'plan': plan}
    return render(request, 'membershipplan.html', context)


def deleteplanAdmin(request, pid):
    MembershipPlan.objects.filter(id=pid).delete()
    messages.success(
        request, 'Plan Deleted Successfully')
    return redirect('membershipplan')


def editplanAdmin(request, pid):
    print(pid)
    planid = MembershipPlan.objects.filter(id=pid).get(id=pid)
    context = {'data': planid}
    return render(request, 'editplan.html', context)


def newplanAdmin(request):
    context = {}
    return render(request, 'newplan.html', context)


def addplanAdmin(request):
    if request.method == 'POST':
        name = request.POST['members_plan_name']
        credit = request.POST['profile_count']
        valdity = request.POST['days_count']
        offer = request.POST['offer_price']
        price = request.POST['plan_amount']
        color = request.POST['plan_color']
        order = request.POST['plan_order']
        printedView = request.POST['is_printed_view']
        message = request.POST['is_messageing']
        tax = request.POST['is_service_tax']
        print(name, credit, valdity, offer, price,
              color, printedView, message, tax)
        MembershipPlan.objects.create(
            name=name, credit=credit, valdity=valdity, offer=offer, price=price, color=color, order=order, printedView=printedView, message=message, tax=tax)
        print("plan added")
        messages.success(
            request, 'Plan Added Successfully')
        return redirect('membershipplan')
    return redirect('membershipplan')


def updateplanAdmin(request, pid):
    if request.method == 'POST':
        name = request.POST['members_plan_name']
        credit = request.POST['profile_count']
        valdity = request.POST['days_count']
        price = request.POST['offer_price']
        offer = request.POST['plan_amount']
        color = request.POST['plan_color']
        order = request.POST['plan_order']
        printedView = request.POST['is_printed_view']
        message = request.POST['is_messageing']
        tax = request.POST['is_service_tax']
        print(name, credit, valdity, offer, price,
              color, printedView, message, tax)
        MembershipPlan.objects.filter(id=pid).update(
            name=name, credit=credit, valdity=valdity, offer=offer, price=price, color=color, order=order, printedView=printedView, message=message, tax=tax)
        print("plan Updated")
        messages.success(
            request, 'Plan Updated Successfully')
        return redirect('membershipplan')
    return redirect('membershipplan')


def userfreeAdmin(request):
    return render(request, 'userfree.html')


def usersilverAdmin(request):
    return render(request, 'usersilver.html')


def usergoldAdmin(request):
    return render(request, 'usergold.html')


def userdiamondAdmin(request):
    return render(request, 'userdiamond.html')


def filterAdmin(request):
    return render(request, 'filter.html')


def moreAdmin(request):
    return render(request, 'moreadmin.html')


def staffprofilesAdmin(request):
    # admin_id = request.session['admin']
    obj = Admin.objects.all()
    context = {'data': obj}
    return render(request, 'staffprofiles.html', context)


def deletestaffAdmin(request):
    id = request.POST['id']
    Admin.objects.filter(id=id).delete()
    return JsonResponse({'msg': 'Deleted Data'})


def addstaffAdmin(request):
    # admin_id = request.session['admin']
    # print(admin_id)
    if request.method == 'POST':
        name = request.POST['name']
        designation = request.POST['designation']
        email = request.POST['email']
        password = request.POST['password']
        Admin.objects.create(name=name, designation=designation, email=email, password=password,
                             last_login=datetime.datetime.now(), date_joined=datetime.datetime.now())
        messages.success(
            request, 'Account Created Successfully')
        print("Staff created")
        context = {}
        return render(request, 'addstaff.html', context)
    return render(request, 'addstaff.html')


def verifiedusersAdmin(request):
    return render(request, 'verifiedusers.html')


def deletedusersAdmin(request):
    return render(request, 'deletedusers.html')


def settingsAdmin(request):
    return render(request, 'settingsadmin.html')


def profilesAdmin(request):
    return render(request, 'profilesadmin.html')
# def Admin(request):
#     return render(request, '.html')
# def Admin(request):
#     return render(request, '.html')
# def Admin(request):
#     return render(request, '.html')
# def Admin(request):
#     return render(request, '.html')
# def Admin(request):
#     return render(request, '.html')
# def Admin(request):
#     return render(request, '.html')
# def Admin(request):
#     return render(request, '.html')
# def Admin(request):
#     return render(request, '.html')
# def Admin(request):
#     return render(request, '.html')
# def Admin(request):
#     return render(request, '.html')

# def allprofilesAdmin(request):
#     return render(request, 'myprofile.html')
