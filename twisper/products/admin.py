from django.contrib import admin

# Register your models here.

from .models import tweets

admin.site.register(tweets)