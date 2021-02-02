import tweepy
import pandas as pd
import operator as op
import nltk
from pathlib import Path
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib
import base64
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer

sid = SentimentIntensityAnalyzer()
wordnet_lemmatizer = WordNetLemmatizer()
STOPWORDS = set(stopwords.words("english"))

consumer_key = ""
consumer_secret = ""
access_token = '' 
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth) 

def clean_text(text:str):
    text=re.sub(r'@[A-Za-z0-9]+','',text)
    text=re.sub(r'#','',text)
    text=re.sub(r'https?:\/\/\S+','',text)
    return text

def bar_chart(df,query):
    malist=[]
    mydict={}
    TOKEN_PATTERN = r"\b[a-zA-Z][a-zA-Z]+\b"
    for i,row in df.iterrows():
        words=clean_text(row["tweet"])
        words= nltk.regexp_tokenize(words, TOKEN_PATTERN)
        for w in words:
            w=w.lower()            
            if w in STOPWORDS or w==query or w=="amp":
                continue
            w=wordnet_lemmatizer.lemmatize(w, pos="v")
            if w in mydict.keys():
                mydict[w] +=1
            else:
                mydict[w]=1
    sort_list = sorted(mydict.items(), key=op.itemgetter(1),reverse=True)
    words= list(zip(*sort_list))[0]
    frequancy = list(zip(*sort_list))[1]
    plt.figure(figsize=(7,5))
    plt.bar(words[0:20],frequancy[0:20],width=0.75,edgecolor="#f05131", label="Frequency",color="#4682B4")
    plt.legend(fontsize=15)
    plt.title("Most Common Words In Tweets",fontsize=20)
    #plt.xlabel("words", fontsize=15)
    plt.xticks(rotation=75,fontsize=12)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    pth=Path(__file__).parent
    img = io.BytesIO()
    plt.savefig(img,format='jpeg')
    img.seek(0)
    string = base64.b64encode(img.read())
    img64='data:img/png;base64,'+urllib.parse.quote(string)
    return img64

def pie_chart(df):
    y=df["sentiment"].value_counts()
    colour={"Very Positive":"#3BB9FF","Positive":"#82CAFF","Neutral":"#E5E4E2","Negatif":"#F75D59","Very Negatif":"#F62817"}
    plt.figure(figsize=(8,5))
    plt.pie(y,labels=y.values, colors=(colour[i] for i in y.keys()),shadow=True,textprops={'fontsize': 15})
    plt.title("Overall Sentiment Distribution",fontsize=20)
    plt.legend(y.keys(),loc="center left",bbox_to_anchor=(0.93,0.70),fontsize=15)
    plt.tight_layout()
    img = io.BytesIO()
    plt.savefig(img,format='jpeg')
    img.seek(0)
    string = base64.b64encode(img.read())
    img64='data:img/png;base64,'+urllib.parse.quote(string)
    return img64



def get_sentiment(text):
    compound=sid.polarity_scores(text).get('compound')
    if -0.1<=compound<=0.1:
        sentiment="Neutral"
    elif -0.5<=compound<-0.1:
        sentiment="Negatif"
    elif -1<=compound<-0.5:
        sentiment="Very Negatif"
    elif 0.1<compound<=0.5:
        sentiment="Positive"
    elif 0.5<compound<=1:
        sentiment="Very Positive"
    return sentiment

def fetch_tweets(query:str,number:int):
    tweets=[]
    dt = api.search(q=query, lang="en", count=number, tweet_mode='extended')
    for d in dt:
        if 'retweeted_status' in d._json:
            tweet=d._json['retweeted_status']['full_text']
        else:
            tweet=d.full_text
        user=d.user.screen_name
        date=str(d.created_at)
        date=date[0:10]
        sentiment= get_sentiment(tweet)
        tweets.append((tweet,sentiment,user,date,query))        
        headers=["tweet","sentiment","user","date","query"]
        mydf=pd.DataFrame(tweets,columns=headers)
    return mydf

def lineChart(df,query:str):
    mydf=df[df["query"]==query]
    dates=sorted(set(df['date']))
    complist=[]
    scorelist=[]
    for date in dates:
        comp=0
        tempdf=mydf[mydf["date"]==date]
        for tweet in tempdf["tweet"]:
            polarity = sid.polarity_scores(tweet).get('compound')
            comp=comp+polarity   
        complist.append(comp)
    plt.figure(figsize=(8,5))
    plt.plot(dates, complist, color='red', marker='o')
    plt.title('Sentiment Change by Date', fontsize=14)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Sum of polarity scores', fontsize=14)
    plt.grid(True)
    plt.tight_layout()
    img = io.BytesIO()
    plt.savefig(img,format='jpeg')
    img.seek(0)
    string = base64.b64encode(img.read())
    img65='data:img/png;base64,'+urllib.parse.quote(string)
    return img65


