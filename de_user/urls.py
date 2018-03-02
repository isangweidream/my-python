from django.contrib import admin
from django.urls import path,include
from django.shortcuts import render
from de_user.views import *


urlpatterns = [
        path('login',login),
        path('reg',register),
        path('reg_hand',register_handle),
        path('log_hand',login_handle),
        path('logout',logout),
        path('checkname',register_exist),
        path('usercenter',user_center),
        path('userinfo',user_center_info),
        path('userupdate',userupdate),
        path('shdz',shdz),
        path('zhanghuguanli',zhanghuguanli),
        path('save_addr',save_addr),
        path('mrdz',mrdz),
        path('scdz',scdz),
        path('bjdz',bjdz),
        path("details",detail),
]
