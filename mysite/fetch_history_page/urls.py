from django.urls import path

from . import views

urlpatterns = [
    path('', views.see_history, name='FetchHistory'),
]