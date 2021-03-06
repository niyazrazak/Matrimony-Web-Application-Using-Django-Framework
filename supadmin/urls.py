from django.urls import path
from .import views
urlpatterns = [
    path('masteradmin/', views.indexadm, name='masteradmin'),
    path('homeadmin/', views.homeAdmin, name='homeadmin'),
    path('allprofiles/', views.allprofilesAdmin, name='allprofiles'),
    path('premiumprofiles/', views.premiumprofilesAdmin, name='premiumprofiles'),
    path('unapprovedrequest/', views.unapprovedrequestAdmin,
         name='unapprovedrequest'),
    path('membershipplan/', views.membershipplanAdmin, name='membershipplan'),
    path('deleteplan/<pid>', views.deleteplanAdmin, name='deleteplan'),
    path('editplan/<pid>', views.editplanAdmin, name='editplan'),
    path('updateplan/<pid>', views.updateplanAdmin, name='updateplan'),
    path('newplan/', views.newplanAdmin, name='newplan'),
    path('addplan/', views.addplanAdmin, name='addplan'),
    path('userfree/', views.userfreeAdmin, name='userfree'),
    path('usersilver/', views.usersilverAdmin, name='usersilver'),
    path('usergold/', views.usergoldAdmin, name='usergold'),
    path('userdiamond/', views.userdiamondAdmin, name='userdiamond'),
    path('filter/', views.filterAdmin, name='filter'),
    path('moreadmin/', views.moreAdmin, name='moreadmin'),
    path('staffprofiles/', views.staffprofilesAdmin, name='staffprofiles'),
    path('addstaff/', views.addstaffAdmin, name='addstaff'),
    path('verifiedusers/', views.verifiedusersAdmin, name='verifiedusers'),
    path('deletedusers/', views.deletedusersAdmin, name='deletedusers'),
    path('settingsadmin/', views.settingsAdmin, name='settingsadmin'),
    path('profilesadmin/', views.profilesAdmin, name='profilesadmin'),
    path('logoutadmin/', views.logoutAdmin, name='logoutadmin'),
    path('deletestaff/', views.deletestaffAdmin, name='deletestaff'),
    # path('',views.Admin,name=''),
    # path('',views.Admin,name=''),
    # path('',views.Admin,name=''),
    # path('',views.Admin,name=''),
    # # path('abcd',views.Admin,name=''),
    # path('abcd',views.Admin,name=''),
]
