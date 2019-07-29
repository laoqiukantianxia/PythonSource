from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse(u"开启Django学习之旅!")

def home(request):
    return render(request, 'home.html')
