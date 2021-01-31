from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class tweetsForm(forms.Form):
    query=forms.CharField()

"""class historyForm(forms.Form):
    selectedquery=forms.CharField()"""

class registerForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]