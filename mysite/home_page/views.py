from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<b>Welcome to my website</b>")