from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def user_home_view(request):
    return HttpResponse("<b>This will be homepage after user loged in</b>")