import pandas as pd
import re
import string
from bs4 import BeautifulSoup
import spacy
import en_core_web_sm
import nltk

def clean_tweets(data_path, language):
    tweets = pd.read_pickle(data_path)
    tweets = tweets.head(5)
    
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
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        
        # Remove stop words
        text = text.split()
        
        text = [word for word in text if not word in stop_words]
        
        # Remove numbers
        text = [re.sub(r'\w*\d\w*', '', w) for w in text]
        
        print(r, text)
        

clean_tweets('data/elonmusk_last_100.pkl','en')