from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def sign_up_view(request):
    return HttpResponse("<b>This is sign_up page</b>")