# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from testapp import views  # new
 
 
urlpatterns = [
    url(r'', views.index, name="testapp"), 
]
