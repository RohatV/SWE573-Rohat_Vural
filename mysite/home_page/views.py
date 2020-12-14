from typing import ContextManager
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request):
    
    if request.user.is_authenticated:
        username=request.user.username
        context={"name":username}
    else:
        context={"name":"visitor"}

    return render(request,"home_page.html", context)