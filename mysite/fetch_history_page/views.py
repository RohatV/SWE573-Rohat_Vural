from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def see_history(request):
    return HttpResponse("<b>This is the page where user can see fetch history and review the results</b>")
