from django.urls import path,re_path

from de_goods.views import *

urlpatterns = [
    re_path('^list_(\d+)_(\d+)_(\d+)$', typelist),
    path('', index, name='index'),

]
