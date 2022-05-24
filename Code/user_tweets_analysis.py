# Import Libraries
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk
import re
import string
from PIL import Image
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import SnowballStemmer


def percentage(part,whole):
     return 100 * float(part)/float(whole)

def create_sentiments(tweets_as_df):
    #Sentiment Analysis

    tweets = pd.read_pickle(tweets_as_df)
    #print(tweets.columns)
    for r in range(len(tweets)):
        tweet_text = tweets['text'].iloc[r]
        
        # get the polarity sentiment
        analysis = TextBlob(tweet_text)
        #print(analysis.sentiment)
        
        # get the positive or negative sentiment
        score = SentimentIntensityAnalyzer().polarity_scores(tweet_text)
        print(score)
        neg = score['neg']
        neu = score['neu']
        pos = score['pos']
        
        # get the polarity sentiment
        polarity = analysis.sentiment.polarity
        tweets.at[r, 'polarity_sentiment'] = polarity
        
        # get the subjectivity sentiment 
        subjectivity = analysis.sentiment.subjectivity
        tweets.at[r, 'subjectivity_sentiment'] = subjectivity
        
        #print(tweet.text)
        
        if neg > pos:
            negative_positive_sentiment = neg
        elif pos > neg:
            negative_positive_sentiment = pos
        elif pos == neg:
            negative_positive_sentiment = neu
        
        tweets.at[r, 'negative_positive_sentiment'] = negative_positive_sentiment
    
    print(tweets)
    tweets.to_pickle(tweets_as_df)
        
    
create_sentiments('data/elonmusk_last_100.pkl')