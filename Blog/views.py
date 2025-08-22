from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Hello World - Anderson")

def post_view(request):
    return HttpResponse("Hello World - Post")

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
