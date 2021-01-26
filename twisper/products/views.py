from django.shortcuts import render
from django.http import HttpResponse
from .forms import tweetsForm
from .getTweets import (fetch_tweets,bar_chart)
from .saveTweets import save_tweets

import pandas as pd
import json
# Create your views here.

def search_view(request, *args, **kwargs):
    context={}
    if request.method == "POST":
        post_data=request.POST or None
        if post_data != None:
            my_form= tweetsForm(request.POST)
            if my_form.is_valid():
                query=my_form.cleaned_data.get("query")
                df=fetch_tweets(query)
                barChart = bar_chart(df,query)
                json_records = df.reset_index().to_json(orient ='records')
                data = [] 
                data = json.loads(json_records)
                save_tweets(data)
                context={"data":data,"barChart":barChart}    
    return render(request,"forms.html",context)

def home_page(request, *args, **kwargs):
    return render(request,"homepage.html",{})
    #return HttpResponse("<h1> Hello Twhisper </h1>")