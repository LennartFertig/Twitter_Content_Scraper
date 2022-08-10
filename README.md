# Twitter_Content_Scraper
Aktuelle Entwicklungen von Data Science Projekt

Link zu Google Drive Ordner:
https://drive.google.com/drive/u/0/folders/1sswoFbUWnrNsAgr8meHGKwgv7Ob-MPkX

## Dokumentation

### Installation
1. Download all required Libaries and [Python 3.9](https://www.python.org/downloads/release/python-3913/)
```
pip install pandas
pip install spacy
python -m spacy download en_core_web_sm
pip install nltk
pip install snscrape
pip install transformers
pip install numpy
pip install torch
pip install textblob
pip install matplotlib
pip install wordcloud
```
2. Download the trained model from this gdrive and put it into the directory ```~/Twitter_Content_Scraper```

### Purpose and structure of the individual Python Files 
1. twitter_scraper.py In this file the function ```get_tweets()``` manages the extraction of the tweets from [twitter](https://twitter.com/). For this purpose it uses the [snscrape libary](https://github.com/JustAnotherArchivist/snscrape) which can scrape tweets with almost no restriction and no Twitter API Account. The scaped tweets are then safed pandas and after the full extraction as a pickle in ```f'./data/{username}_last_{number_of_tweets}.pkl'``` 
2. clean_tweets.py In this file the function ```clean_tweets()``` cleans the tweets. First it was thought to be a good idea to clean the tweets from stopwords, punctuations and numbers but instead it is now only cleaned from links and @user_mentions. If the tweet consists only out of links and/or @user_mentions the tweet is deleted and not used any further.
3. user_tweets_analysis.py In this file the function ```create_sentiments()``` 
