import psycopg2
import pandas as pd
from django.contrib.auth import authenticate
def connect_DB():
    connect=psycopg2.connect(
        database="d436npibmanq8u",
        user="dswaborggplsgu",
        password="7e2e87068c3f95f3d62fbe52ca1ad31599b197b2fe8f6f9618649af8c12790cb",
        host="ec2-52-2-82-109.compute-1.amazonaws.com",
        port="5432"
    )
    cur = connect.cursor()
    cur.execute("INSERT INTO products_tweets(query,tweet,author,twhisper_user,sentiment,date) VALUES (%s,%s,%s,%s,%s,%s)",
    ('a','b','c','d','e',1)
    )

    cur.close()
    connect.commit()
    connect.close()


def save_tweets(data,twhisper_user):

    conn = psycopg2.connect(
        database="d436npibmanq8u",
        user="dswaborggplsgu",
        password="7e2e87068c3f95f3d62fbe52ca1ad31599b197b2fe8f6f9618649af8c12790cb",
        host="ec2-52-2-82-109.compute-1.amazonaws.com",
        port="5432"
    )
    cur = conn.cursor()
    

    for item in data:
        cur.execute("INSERT INTO products_tweets(query,tweet,author,twhisper_user,sentiment,date)values(%s,%s,%s,%s,%s,%s)",(item['query'], item['tweet'], item['user'], twhisper_user, item['sentiment'],item['date']))        
    conn.commit()
    cur.close()
    conn.close()

def get_users_and_queries_from_db():
    conn = psycopg2.connect(
        database="d436npibmanq8u",
        user="dswaborggplsgu",
        password="7e2e87068c3f95f3d62fbe52ca1ad31599b197b2fe8f6f9618649af8c12790cb",
        host="ec2-52-2-82-109.compute-1.amazonaws.com",
        port="5432"
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
if __name__== "__main__":
    get_users_and_queries_from_db()