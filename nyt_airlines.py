#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 11:49:34 2024

@author: emmaheck
"""
import datetime
from pynytimes import NYTAPI

nyt = NYTAPI("WPOkVMKgvkBcb75utTUbhWu9uKurjhnB", parse_dates=True)

#define 1-year period
period = {"begin": datetime.datetime(2023,1,1), "end": datetime.datetime(2023,12,31)}

americanAirlines = nyt.article_search(query="American Airlines", dates=period)
jetblue = nyt.article_search(query="JetBlue", dates=period)
delta = nyt.article_search(query="Delta Airlines", dates=period)
southwest = nyt.article_search(query="Southwest Airlines", dates=period)
united = nyt.article_search(query="United Airlines", dates=period)

airlines2 = americanAirlines + jetblue + delta + southwest + united

#import pandas
import pandas as pd

#create an empty list for American Airlines articles and add articles to list
airlines = []
for article in americanAirlines[:10]:
    airlines.append({
        "Airline": "American Airlines",
        "Title": article["headline"]["main"],
        "Date": article["pub_date"],
        "Abstract": article["abstract"]
        })

#add JetBlue articles
for article in jetblue[:10]:
    airlines.append({
        "Airline": "JetBlue",
        "Title": article["headline"]["main"],
        "Date": article["pub_date"],
        "Abstract": article["abstract"]
        })

#add Delta articles
for article in delta[:10]:
    airlines.append({
        "Airline": "Delta Airlines",
        "Title": article["headline"]["main"],
        "Date": article["pub_date"],
        "Abstract": article["abstract"]
        })
    
#add Southwest articles
for article in southwest[:10]:
    airlines.append({
    "Airline": "Southwest Airlines",
    "Title": article["headline"]["main"],
    "Date": article["pub_date"],
    "Abstract": article["abstract"]
    })
    
#add United articles
for article in united[:10]:
    airlines.append({
        "Airline": "United Airlines",
        "Title": article["headline"]["main"],
        "Date": article["pub_date"],
        "Abstract": article["abstract"]
        })
    
    
#create a dataframe
airlines = pd.DataFrame(airlines)

#import libraries
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


# #calculate sentiment score
sentiment_score = []
for abstract in airlines['Abstract']:
    myText = abstract
    sentiment = analyzer.polarity_scores(myText)["compound"]
    sentiment_score.append(sentiment)
print(sentiment_score)

#add sentiment score to dataframe
airlines['Sentiment'] = sentiment_score

#define levels
sentiment_level = []
for number in airlines['Sentiment']:
    if number < 0:
        n = "negative"
    else:
        n = "positive"
    sentiment_level.append(n)
    
#add levels to dataframe
airlines['Sentiment_Level'] = sentiment_level

#create a csv file
airlines.to_csv('airlines.csv', index=False)




