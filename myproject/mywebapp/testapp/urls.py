# -*- coding:utf-8 -*-

from django.conf.urls import url
from django.contrib import admin
from testapp import views as testapp_views  # new
 
 
urlpatterns = [
    url(r'^$', testapp_views.index, name="testapp"),  # new
]
