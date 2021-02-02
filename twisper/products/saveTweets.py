import psycopg2
import pandas as pd
from django.contrib.auth import authenticate



def save_tweets(data,twhisper_user):
    conn = psycopg2.connect(
        database="",
        user="",
        password="",
        host="",
        port=""
    )
    cur = conn.cursor()
    for item in data:
        cur.execute("INSERT INTO products_tweets(query,tweet,author,twhisper_user,sentiment,date)values(%s,%s,%s,%s,%s,%s)",(item['query'], item['tweet'], item['user'], twhisper_user, item['sentiment'],item['date']))        
    conn.commit()
    cur.close()
    conn.close()

def get_users_and_queries_from_db():
    conn = psycopg2.connect(
        database="",
        user="",
        password="",
        host="",
        port=""
    )
    cur = conn.cursor()
    cur.execute("select query, date, tweet, sentiment, twhisper_user from products_tweets")
    headers=["query","date","tweet", "sentiment","twhisper_user"]
    rows=cur.fetchall()
    df=pd.DataFrame(rows,columns=headers)
    conn.commit()
    cur.close()
    conn.close()
    return df

def delete_from_database(query,date,twhisper_user):
    conn = psycopg2.connect(
        database="",
        user="",
        password="",
        host="",
        port=""
    )
    cur = conn.cursor()   
    cur.execute("DELETE FROM products_tweets WHERE query=%s AND date=%s AND twhisper_user=%s", (query,date,twhisper_user,))
    conn.commit()
    cur.close()
    conn.close()


