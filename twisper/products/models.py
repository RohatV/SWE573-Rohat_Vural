from django.db import models

# Create your models here.

class tweets(models.Model):
    query= models.CharField(max_length=20)
    tweet = models.TextField(null=True, blank=True)
    #favoriteNumber= models.IntegerField(default=0)
    #retweetNum= models.IntegerField(default=0)
    author = models.CharField(max_length=20)
    twhisper_user=models.CharField(max_length=20)
    sentiment = models.CharField(max_length=20)
    date=models.CharField(max_length=12)


