
from django.urls import path 
from induz import views
 
urlpatterns=[
 path('',views.index),
 path('1/',views.about),
 path('contact/',views.contact),
 path('3/',views.services),
  path('contact2/',views.contact2),
  path('login/',views.login),
  path('viewdt/',views.viewdata),
   path('logout/',views.logout),
   path('userprofile/',views.userprofile),
    path('data/',views.tabledata),
    path('delete/',views.datadelete),
    path('updatedata/',views.updatedata),
    path('updateformdata/',views.updateformdata),
    path('imgupload/',views.imgupload),
    path('imgupload1/',views.imgupload1),
    path('downloadtc/',views.downloadtc),
     path('favsteel/',views.favsteel),
 path('tabledatafav/',views.tabledatafav),
path('userajax/',views.viewuser),
path('box/',views.box),

    

] 