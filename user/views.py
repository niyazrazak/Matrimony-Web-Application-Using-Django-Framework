from typing import ContextManager
from django.core import exceptions
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
import datetime
from random import random
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from .models import *
from supadmin .models import *
from staffadmin .models import *

# Create your views here.


def indexFun(request):
    try:
        adds = HappyStories.objects.all()
    except:
        adds = ''
    context = {'adds': adds}
    return render(request, 'index.html', context)


def signupFun(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']
        gender = request.POST['gender']
        number = request.POST['number']
        profile = request.POST['profile']
        print(profile)
        if User.objects.filter(email=email).exists():
            print("Email Already Taken")
            messages.error(
                request, 'Email is Already Exists Try Another Email')
            return redirect('index')

        else:
            user = User.objects.create(email=email, password=password, name=name,
                                       gender=gender, phoneNumber=number, profileFor=profile, last_login=datetime.datetime.now(), date_joined=datetime.datetime.now())
            print("user created")
            messages.success(
                request, 'Account Created Successfully')
            return redirect('index')
    return redirect('index')


def loginFun(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        user = User.objects.filter(email=email, password=password).exists()
        if user:
            user = User.objects.get(email=email, password=password)
            request.session['log'] = user.id
            User.objects.get(id=user.id)
            print("Logged In")
            return redirect('userhome')
        else:
            return render(request, 'index.html', {'mes': 'Error : Wrong username/password'})
    return redirect('index')


def logoutFun(request):
    try:
        del request.session['log']
        print("logged out")
        return redirect('index')
    except:
        return redirect('index')


def homeFun(request):
    return render(request, 'userhome.html')


def userFun(request):
    return render(request, 'user_dash.html')


def myprofileFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    try:
        profile = Profiles.objects.get(user=user_id)
    except:
        profile = ''
    try:
        education = EducationalInfotb.objects.get(user=user_id)
    except:
        education = ''
    try:
        physical = PhysicalInfotb.objects.get(user=user_id)
    except:
        physical = ''
    try:
        family = FamilyInfotb.objects.get(user=user_id)
        print(family)
    except:
        family = ''
    try:
        contact = contactInfotb.objects.get(user=user)
    except:
        contact = ''
    try:
        other = OtherInfotb.objects.get(user=user)
    except:
        other = ''
    try:
        patner = PatnerPrefertb.objects.get(user=user)
    except:
        patner = ''
    context = {'user': user, 'profile': profile,
               'education': education, 'physical': physical, 'family': family, 'contact': contact, 'other': other, 'patner': patner}
    return render(request, 'myprofile.html', context)


def mymatchesFun(request):
    return render(request, 'mymatches.html')


def shortlistFun(request):
    return render(request, 'shortlist.html')


def manageprofileFun(request):
    return render(request, 'manageprofile.html')


def packageuserFun(request):
    plan = MembershipPlan.objects.all()
    context = {'plan': plan}
    return render(request, 'packageuser.html', context)


def searchbasicFun(request):
    return render(request, 'searchbasic.html')


def searcheducationFun(request):
    return render(request, 'searcheducation.html')


def searchoccupationFun(request):
    return render(request, 'searchoccupation.html')


def searchidFun(request):
    return render(request, 'searchid.html')


def searchadvancedFun(request):
    return render(request, 'searchadvanced.html')


def managephotosFun(request):
    return render(request, 'managephotos.html')


def expressinterestFun(request):
    return render(request, 'expressinterest.html')


def photorequestFun(request):
    return render(request, 'photorequest.html')


def messagesuserFun(request):
    return render(request, 'messagesuser.html')


def expresseduserFun(request):
    return render(request, 'expresseduser.html')


def recieveduserFun(request):
    return render(request, 'recieveduser.html')


def dashboardFun(request):
    return render(request, 'dashboard.html')


def basicinformationFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    if Profiles.objects.filter(user=user_id).exists():
        profile = Profiles.objects.get(user=user_id)
        context = {'user': user, 'profile': profile}
    else:
        context = {'user': user}
    return render(request, 'basicinformation.html', context)


def basicupdateFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    if Profiles.objects.filter(user=user_id).exists():
        profile = Profiles.objects.get(user=user_id)
        if request.method == 'POST':
            mem_profile_for = request.POST['mem_profile_for']
            mem_name = request.POST['mem_name']
            mem_dob = request.POST['mem_dob']
            mem_martial_status = request.POST['mem_martial_status']
            mem_mother_toungue = request.POST['mem_mother_toungue']
            mem_religion = request.POST['mem_religion']
            mem_caste = request.POST['mem_caste']
            mem_education = request.POST['mem_education']
            mem_annual_income = request.POST['mem_annual_income']
            country = request.POST['country']
            state = request.POST['state']
            city = request.POST['city']
            User.objects.filter(id=user_id).update(
                name=mem_name, profileFor=mem_profile_for)
            Profiles.objects.update(dob=mem_dob, martialStatus=mem_martial_status,
                                    motherTounge=mem_mother_toungue, religion=mem_religion, caste=mem_caste, education=mem_education, income=mem_annual_income, country=country, states=state, city=city, user=user)
            context = {'user': user, 'profile': profile,
                       'msg': 'updated successfully'}
            return render(request, 'basicinformation.html', context)
        context = {'user': user, 'profile': profile}
    else:
        if request.method == 'POST':
            mem_profile_for = request.POST['mem_profile_for']
            mem_name = request.POST['mem_name']
            mem_dob = request.POST['mem_dob']
            mem_martial_status = request.POST['mem_martial_status']
            mem_mother_toungue = request.POST['mem_mother_toungue']
            mem_religion = request.POST['mem_religion']
            mem_caste = request.POST['mem_caste']
            mem_education = request.POST['mem_education']
            mem_annual_income = request.POST['mem_annual_income']
            country = request.POST['country']
            state = request.POST['state']
            city = request.POST['city']
            print(mem_religion, mem_mother_toungue)
            User.objects.filter(id=user_id).update(
                name=mem_name, profileFor=mem_profile_for)
            Profiles.objects.create(dob=mem_dob, martialStatus=mem_martial_status,
                                    motherTounge=mem_mother_toungue, religion=mem_religion, caste=mem_caste, education=mem_education, income=mem_annual_income, country=country, states=state, city=city, user=user)
            profile = Profiles.objects.get(user=user_id)
            context = {'user': user, 'profile': profile,
                       'msg': 'updated successfully'}
            return render(request, 'basicinformation.html', context)
        context = {'user': user}
    return render(request, 'basicinformation.html', context)


def educationalinformationFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    try:
        education = EducationalInfotb.objects.get(user=user_id)
    except:
        education = ''
    context = {'education': education}
    return render(request, 'educationalinformation.html', context)


def eduUpdateFun(request):
    try:
        user_id = request.session['log']
        user = User.objects.get(id=user_id)
        if EducationalInfotb.objects.filter(user=user_id).exists():
            if request.method == 'POST':
                quallification = request.POST['mem_quallification']
                occupation = request.POST['mem_occupation']
                languagesknown = request.POST.getlist('mem_language_known')
                separator = ", "
                res = separator.join(languagesknown)
                EducationalInfotb.objects.update(
                    qualification=quallification, occupation=occupation, languagesKnown=res, user=user)
                print("Value Inserted")
                return redirect('educationalinformation')
            return redirect('educationalinformation')
        else:
            if request.method == 'POST':
                quallification = request.POST['mem_quallification']
                occupation = request.POST['mem_occupation']
                languagesknown = request.POST.getlist('mem_language_known')
                separator = ", "
                res = separator.join(languagesknown)
                EducationalInfotb.objects.create(
                    qualification=quallification, occupation=occupation, languagesKnown=res, user=user)
                print("Value Inserted")
                return redirect('educationalinformation')
            return redirect('educationalinformation')
    except:
        return redirect('educationalinformation')


def physicalinformationFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    try:
        physical = PhysicalInfotb.objects.get(user=user_id)
    except:
        physical = ''
    context = {'physical': physical}
    return render(request, 'physicalinformation.html', context)


def physicalUpdateFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    if PhysicalInfotb.objects.filter(user=user_id).exists():
        if request.method == 'POST':
            height = request.POST['mem_height']
            weight = request.POST['mem_weight']
            complexion = request.POST['mem_complexion']
            bloodGroup = request.POST['mem_blood_group']
            bodyType = request.POST['mem_body_type']
            diet = request.POST['mem_diet']
            smoke = request.POST['mem_smoke']
            drink = request.POST['mem_drink']
            physicallyImpaired = request.POST['mem_physically_impaired']
            dressStyle = request.POST['mem_dress_style']
            PhysicalInfotb.objects.update(height=height, weight=weight, complexion=complexion, bloodGroup=bloodGroup,
                                          bodyType=bodyType, diet=diet, smoke=smoke, drink=drink, physicallyImpaired=physicallyImpaired, dressStyle=dressStyle, user=user)
            print("Value Updated")
            return redirect('physicalinformation')
        return redirect('physicalinformation')
    else:
        if request.method == 'POST':
            height = request.POST['mem_height']
            weight = request.POST['mem_weight']
            complexion = request.POST['mem_complexion']
            bloodGroup = request.POST['mem_blood_group']
            bodyType = request.POST['mem_body_type']
            diet = request.POST['mem_diet']
            smoke = request.POST['mem_smoke']
            drink = request.POST['mem_drink']
            physicallyImpaired = request.POST['mem_physically_impaired']
            dressStyle = request.POST['mem_dress_style']
            print(height, weight, complexion, bloodGroup, bodyType,
                  diet, smoke, drink, physicallyImpaired, dressStyle)
            PhysicalInfotb.objects.create(height=height, weight=weight, complexion=complexion, bloodGroup=bloodGroup,
                                          bodyType=bodyType, diet=diet, smoke=smoke, drink=drink, physicallyImpaired=physicallyImpaired, dressStyle=dressStyle, user=user)
            print("Value Inserted")
            return redirect('physicalinformation')
        return redirect('physicalinformation')


def familyinformationFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    try:
        family = FamilyInfotb.objects.get(user=user_id)
    except:
        family = ''
    context = {'family': family}
    return render(request, 'familyinformation.html', context)


def familyUpdateFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    if FamilyInfotb.objects.filter(user=user_id).exists():
        if request.method == 'POST':
            fatherName = request.POST['mem_father_name']
            fathersOccupation = request.POST['mem_fathers_occupation']
            motherName = request.POST['mem_mother_name']
            mothersOccupation = request.POST['mem_mothers_occupation']
            noofBrothers = request.POST['mem_no_of_brothers']
            noofBrothersMarried = request.POST['mem_no_of_brothers_married']
            noofSisters = request.POST['mem_no_of_sisters']
            noofSistersMarried = request.POST['mem_no_of_sisters_married']
            familyValue = request.POST['mem_family_value']
            familyStatus = request.POST['mem_family_status']
            familyType = request.POST['mem_family_type']
            familyIncome = request.POST['mem_family_income']
            nativeLocation = request.POST['mem_native']
            medicalHistory = request.POST['mem_medical_history']
            FamilyInfotb.objects.update(fatherName=fatherName, fatherOcuupation=fathersOccupation, motherName=motherName, motherOcuupation=mothersOccupation, noofBrothers=noofBrothers, noofBrothersMarried=noofBrothersMarried,
                                        noofSisters=noofSisters, noofSistersMarried=noofSistersMarried, familyValue=familyValue, familyStatus=familyStatus, familyType=familyType, familyIncome=familyIncome, nativeLocation=nativeLocation, medicalHistory=medicalHistory, user=user)
            print("Value Updated")
            return redirect('familyinformation')
        return redirect('familyinformation')
    else:
        if request.method == 'POST':
            fatherName = request.POST['mem_father_name']
            fathersOccupation = request.POST['mem_fathers_occupation']
            motherName = request.POST['mem_mother_name']
            mothersOccupation = request.POST['mem_mothers_occupation']
            noofBrothers = request.POST['mem_no_of_brothers']
            noofBrothersMarried = request.POST['mem_no_of_brothers_married']
            noofSisters = request.POST['mem_no_of_sisters']
            noofSistersMarried = request.POST['mem_no_of_sisters_married']
            familyValue = request.POST['mem_family_value']
            familyStatus = request.POST['mem_family_status']
            familyType = request.POST['mem_family_type']
            familyIncome = request.POST['mem_family_income']
            nativeLocation = request.POST['mem_native']
            medicalHistory = request.POST['mem_medical_history']
            FamilyInfotb.objects.create(fatherName=fatherName, fatherOcuupation=fathersOccupation, motherName=motherName, motherOcuupation=mothersOccupation, noofBrothers=noofBrothers, noofBrothersMarried=noofBrothersMarried,
                                        noofSisters=noofSisters, noofSistersMarried=noofSistersMarried, familyValue=familyValue, familyStatus=familyStatus, familyType=familyType, familyIncome=familyIncome, nativeLocation=nativeLocation, medicalHistory=medicalHistory, user=user)
            print("Value Inserted")
            return redirect('familyinformation')
        return redirect('familyinformation')
    return redirect('familyinformation')


def contactinformationFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    try:
        contact = contactInfotb.objects.get(user=user)
    except:
        contact = ''
    context = {'user': user, 'contact': contact}
    return render(request, 'contactinformation.html', context)


def contactUpdateFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    if contactInfotb.objects.filter(user=user_id).exists():
        if request.method == 'POST':
            mobileCode = request.POST['mem_mobile_code']
            mobileNumber = request.POST['mem_mobile']
            phoneNumber = request.POST['mem_phone']
            email = request.POST['mem_email']
            address = request.POST['mem_address']
            residenceIn = request.POST['mem_residence_in']
            otherLocation = request.POST['mem_location']
            pincode = request.POST['mem_pincode']
            whatsappCode = request.POST['mem_whatsapp_code']
            whatsappNumber = request.POST['mem_whatsapp']
            User.objects.filter(id=user_id).update(
                phoneNumber=mobileNumber, email=email)
            contactInfotb.objects.update(mobileCode=mobileCode, phoneNumber=phoneNumber, address=address, residenceIn=residenceIn,
                                         otherLocation=otherLocation, pincode=pincode, whatsappCode=whatsappCode, whatsappNumber=whatsappNumber, user=user)
            print("value Updated")
            return redirect('contactinformation')
        return redirect('contactinformation')
    else:
        if request.method == 'POST':
            mobileCode = request.POST['mem_mobile_code']
            mobileNumber = request.POST['mem_mobile']
            phoneNumber = request.POST['mem_phone']
            email = request.POST['mem_email']
            address = request.POST['mem_address']
            residenceIn = request.POST['mem_residence_in']
            otherLocation = request.POST['mem_location']
            pincode = request.POST['mem_pincode']
            whatsappCode = request.POST['mem_whatsapp_code']
            whatsappNumber = request.POST['mem_whatsapp']
            User.objects.filter(id=user_id).update(
                phoneNumber=mobileNumber, email=email)
            contactInfotb.objects.create(mobileCode=mobileCode, phoneNumber=phoneNumber, address=address, residenceIn=residenceIn,
                                         otherLocation=otherLocation, pincode=pincode, whatsappCode=whatsappCode, whatsappNumber=whatsappNumber, user=user)
            print("value Insterted")
            return redirect('contactinformation')
        return redirect('contactinformation')


def otherinformationFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    try:
        other = OtherInfotb.objects.get(user=user)
    except:
        other = ''
    context = {'other': other}
    return render(request, 'otherinformation.html', context)


def otherUpdateFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    if OtherInfotb.objects.filter(user=user).exists():
        if request.method == 'POST':
            hobbies = request.POST.getlist('mem_hobbies')
            separator = ", "
            hobs = separator.join(hobbies)
            interest = request.POST.getlist('mem_interests')
            inter = separator.join(interest)
            describedProfile = request.POST['mem_profile']
            proofType = request.POST['mem_id_proof_type']
            proofNumber = request.POST['mem_id_proof_number']
            # proofFile = request.FILES['mem_id_proof']
            OtherInfotb.objects.update(
                hobbies=hobs, interest=inter, describedProfile=describedProfile, proofType=proofType, proofNumber=proofNumber, user=user)
            print("Value Updated")
            return redirect('otherinformation')
        return redirect('otherinformation')
    else:
        if request.method == 'POST':
            hobbies = request.POST.getlist('mem_hobbies')
            separator = ", "
            hobs = separator.join(hobbies)
            interest = request.POST.getlist('mem_interests')
            inter = separator.join(interest)
            describedProfile = request.POST['mem_profile']
            proofType = request.POST['mem_id_proof_type']
            proofNumber = request.POST['mem_id_proof_number']
            # proofFile = request.FILES['mem_id_proof']
            OtherInfotb.objects.create(
                hobbies=hobs, interest=inter, describedProfile=describedProfile, proofType=proofType, proofNumber=proofNumber, user=user)
            print("Value Inserted")
            return redirect('otherinformation')
        return redirect('otherinformation')


def patnerpreferenceFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    try:
        patner = PatnerPrefertb.objects.get(user=user)
    except:
        patner = ''
    context = {'patner': patner}
    return render(request, 'patnerpreference.html', context)


def patnerUpdateFun(request):
    user_id = request.session['log']
    user = User.objects.get(id=user_id)
    if PatnerPrefertb.objects.filter(user=user).exists():
        if request.method == 'POST':
            lookingFor = request.POST.getlist('partner_looking_for')
            separator = ", "
            lookingFor = separator.join(lookingFor)
            complexion = request.POST.getlist('partner_complexion')
            complexion = separator.join(complexion)
            livingIn = request.POST['partner_country']
            residentialState = request.POST['partner_residential_status']
            ageFrom = request.POST['partner_age_from']
            ageTo = request.POST['partner_age_to']
            heightFrom = request.POST['partner_height_from']
            heightTo = request.POST['partner_height_to']
            education = request.POST.getlist('partner_education')
            education = separator.join(education)
            occupation = request.POST.getlist('partner_occupation')
            occupation = separator.join(occupation)
            motherTongue = request.POST.getlist('partner_mother_tongue')
            motherTongue = separator.join(motherTongue)
            expectation = request.POST['partner_expectations']
            religion = request.POST['partner_religion']
            caste = request.POST.getlist('partner_caste')
            caste = separator.join(caste)
            PatnerPrefertb.objects.update(
                lookingFor=lookingFor, complexion=complexion, livingIn=livingIn, residentialState=residentialState, ageFrom=ageFrom, ageTo=ageTo, heightFrom=heightFrom, heightTo=heightTo, education=education, occupation=occupation, motherTongue=motherTongue, expectation=expectation, religion=religion, caste=caste, user=user)
            print("value Updated")
            return redirect('patnerpreference')
        return redirect('patnerpreference')
    else:
        if request.method == 'POST':
            lookingFor = request.POST.getlist('partner_looking_for')
            separator = ", "
            lookingFor = separator.join(lookingFor)
            complexion = request.POST.getlist('partner_complexion')
            complexion = separator.join(complexion)
            livingIn = request.POST['partner_country']
            residentialState = request.POST['partner_residential_status']
            ageFrom = request.POST['partner_age_from']
            ageTo = request.POST['partner_age_to']
            heightFrom = request.POST['partner_height_from']
            heightTo = request.POST['partner_height_to']
            education = request.POST.getlist('partner_education')
            education = separator.join(education)
            occupation = request.POST.getlist('partner_occupation')
            occupation = separator.join(occupation)
            motherTongue = request.POST.getlist('partner_mother_tongue')
            motherTongue = separator.join(motherTongue)
            expectation = request.POST['partner_expectations']
            religion = request.POST['partner_religion']
            caste = request.POST.getlist('partner_caste')
            caste = separator.join(caste)
            PatnerPrefertb.objects.create(
                lookingFor=lookingFor, complexion=complexion, livingIn=livingIn, residentialState=residentialState, ageFrom=ageFrom, ageTo=ageTo, heightFrom=heightFrom, heightTo=heightTo, education=education, occupation=occupation, motherTongue=motherTongue, expectation=expectation, religion=religion, caste=caste, user=user)
            print("value inserted")
            return redirect('patnerpreference')
        return redirect('patnerpreference')


def mypackageFun(request):
    context = {}
    return render(request, 'mypackage.html', context)


def photoreqreceivedFun(request):
    return render(request, 'photoreqreceived.html')


def photoreqsentFun(request):
    return render(request, 'photoreqsent.html')


def deleteprofileFun(request):
    return render(request, 'deleteprofile.html')


def profilevisitFun(request):
    return render(request, 'profilevisit.html')


def printprofileFun(request):
    return render(request, 'printprofile.html')


def viewprofileFun(request):
    return render(request, 'viewprofile.html')


def viewfullprofileFun(request):
    return render(request, 'viewfullprofile.html')

# def Fun(request):
#     return render(request, '.html')
# def Fun(request):
#     return render(request, '.html')

# def Fun(request):
#     return render(request, '.html')
# def Fun(request):
#     return render(request, '.html')

# def Fun(request):
#     return render(request, '.html')
# def Fun(request):
#     return render(request, '.html')


# def Fun(request):
#     return render(request, '.html')

# def Fun(request):
#     return render(request, '.html')


# def Fun(request):
#     return render(request, '.html')

# def Fun(request):
#     return render(request, '.html')


# def Fun(request):
#     return render(request, '.html')
