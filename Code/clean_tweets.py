import pandas as pd
import re
import string
from bs4 import BeautifulSoup
import spacy
import en_core_web_sm
import nltk

def clean_tweets(data_path, language='en'):
    tweets = pd.read_pickle(data_path)
    #tweets = tweets.head(10)
    
    #use and configure spacy and nltk for text cleaning
    #nlp = spacy.load('en_core_web_sm')
    stop_words = nltk.corpus.stopwords.words("english")
    
    # remove all tweets where language doesnt match
    tweets = tweets.loc[tweets['tweet_lang'] == language]
    #print(tweets)
    
    for r in range(len(tweets)):
        raw_text = tweets['text'].iloc[r]
        print(r, raw_text)
        
        # make text lowercase
        text = raw_text.lower()
        
        # Remove line breaks
        text = re.sub(r'\n', '', text)
        
        # Remove puncuation
        #translator = str.maketrans('', '', string.punctuation)
        #text = text.translate(translator)
        
        # Remove stop words
        #text = text.split()
        
        #text = [word for word in text if not word in stop_words]
        
        # Remove numbers
        #text = re.sub(r'\w*\d\w*', '', w) for w in text
        
        #Remove links and @user_mention
        text = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", text)
        
        #Remove links
        #text = re.sub(r'http\S+', '', text)
        #text = re.sub(r'https\S+', '', text)
        
        #remove @user
        #text = re.sub(r'\@S+', '', text)
        
        text = text.lstrip()
        print(r, text)
        
        tweets.at[r, 'text'] = text
    
    tweets.to_pickle(data_path)
        
     

#clean_tweets('data/elonmusk_last_500.pkl','en')