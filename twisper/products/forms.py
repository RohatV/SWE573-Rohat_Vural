from django import forms


class tweetsForm(forms.Form):
    query=forms.CharField()