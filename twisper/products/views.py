from django.shortcuts import (render, redirect)
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import (tweetsForm, registerForm)
from .getTweets import (fetch_tweets,bar_chart,pie_chart,lineChart)
from .saveTweets import (save_tweets, get_users_and_queries_from_db, delete_from_database)
import pandas as pd
import json
# Create your views here.

fetchedtweets=[]

def register_page(request, *args, **kwargs):
    form = registerForm()
    if request.method == "POST":
        form= registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {"form":form}
    return render(request,"register.html",context)

def login_page(request, *args, **kwargs):
    if request.method == "POST":
        user=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request,username=user,password=password)
        if user is not None:
            login(request,user)
            return redirect('search_page')
        else:
            messages.info(request, "Username or Password is not correct!")

    context = {}
    return render(request,"login.html",context)

def log_out(request):
    logout(request)
    return redirect('login')


def search_view(request, *args, **kwargs):
    context={}  
    myvalue=request.GET       
    query=myvalue.get("query","")
    number=myvalue.get("selected_number",0)
    saveStasus=myvalue.get("save","")
    global fetchedtweets
    if (query != "" and number!=0) and (saveStasus==""):
        print(number)
        fetchedtweets=fetch_tweets(query,number)
        barChart = bar_chart(fetchedtweets,query)
        pieChart = pie_chart(fetchedtweets)        
        data = fetchedtweets.reset_index().to_dict(orient ='records')
        context={"data":data,"barChart":barChart,"pieChart":pieChart} 
    elif saveStasus == "True" and isinstance(fetchedtweets,pd.DataFrame):
        barChart = bar_chart(fetchedtweets,query)
        pieChart = pie_chart(fetchedtweets)        
        data = fetchedtweets.reset_index().to_dict(orient ='records')   
        if request.user.is_authenticated:
            logedInUser = request.user.username
            print(logedInUser)
            save_tweets(data,logedInUser)
            saved=True 
            context={"data":data,"barChart":barChart,"pieChart":pieChart,"saved":saved }
    return render(request,"forms.html",context)

def home_page(request, *args, **kwargs):
    return render(request,"homepage.html",{})

@login_required(login_url='login')
def history_page(request, *args, **kwargs):
    if request.user.is_authenticated:
        logedInUser = request.user.username
        df=get_users_and_queries_from_db()
        df=df[df["twhisper_user"]==logedInUser]
        df["queries_and_dates"]=df["query"]+"/"+df["date"]
        queries_and_dates=list(set(df["queries_and_dates"]))
        context={"queries_and_dates":queries_and_dates}
        myvalue=request.GET       
        selectedQueriesAndDates=myvalue.get("selected_query_and_date","None")
        deleteButtonClicked=myvalue.get("delete","False")
        if selectedQueriesAndDates!="None" and deleteButtonClicked=="False":
            query=selectedQueriesAndDates[:-11]
            date=selectedQueriesAndDates[-10:]
            df=df[df["query"]==query]
            context["lineChart"] = lineChart(df,query)
            df=df[df["date"]==date]
            barChart = bar_chart(df,query)
            pieChart = pie_chart(df)
            context["selectedQueriesAndDates"]=selectedQueriesAndDates
            context["data"]= df.reset_index().to_dict(orient ='records')
            context["barChart"]=barChart
            context["pieChart"]=pieChart  
        if selectedQueriesAndDates!="None" and deleteButtonClicked=="True":
            query=selectedQueriesAndDates[:-11]
            date=selectedQueriesAndDates[-10:]
            delete_from_database(query,date,logedInUser)
            deleted=True
            df=get_users_and_queries_from_db()
            df=df[df["twhisper_user"]==logedInUser]
            df["queries_and_dates"]=df["query"]+"/"+df["date"]
            queries_and_dates=list(set(df["queries_and_dates"]))
            context={"queries_and_dates":queries_and_dates,"deleted":deleted}
            print(deleteButtonClicked)

    return render(request,"searchHistory.html",context)


    