# Twitter_Content_Scraper
Aktuelle Entwicklungen von Data Science Projekt

Link to Prototype in Figma:
(Click on "Check" to see second page)

https://www.figma.com/proto/2OYBDcQMGXogOKUQumtCk0/Untitled?page-id=0%3A1&node-id=1%3A2&viewport=-3501%2C3726%2C8.51&scaling=scale-down&starting-point-node-id=1%3A2

Link to Google Drive Ordner:
https://drive.google.com/drive/u/0/folders/1sswoFbUWnrNsAgr8meHGKwgv7Ob-MPkX  
Contains: 
- VPC
- data used for training BERT Model
- Saved Weights
- Presentation

Link zu Präsentation:
https://docs.google.com/presentation/d/1Lo8E3roxC5bU0iyvJ9-X2vO9JYJbJIzKxqFphfs4AJ8/edit#slide=id.g135bd44c6d9_0_753

A Mockup to a potential App can be found [here](https://www.figma.com/proto/2OYBDcQMGXogOKUQumtCk0/Untitled?page-id=0%3A1&node-id=1%3A2&viewport=-3501%2C3726%2C8.51&scaling=scale-down&starting-point-node-id=1%3A2)
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
2. Download the trained model from the Google Drive and put it into the directory ```~/Twitter_Content_Scraper/Code```

### Purpose and structure of the individual Python Files 
1. twitter_scraper.py In this file the function ```get_tweets()``` manages the extraction of the tweets from [twitter](https://twitter.com/). For this purpose it uses the [snscrape libary](https://github.com/JustAnotherArchivist/snscrape) which can scrape tweets with almost no restriction and no Twitter API Account. The scaped tweets are then safed pandas and after the full extraction as a pickle in ```f'./data/{username}_last_{number_of_tweets}.pkl'``` 

2. clean_tweets.py In this file the function ```clean_tweets()``` cleans the tweets. First it was thought to be a good idea to clean the tweets from stopwords, punctuations and numbers but instead it is now only cleaned from links and @user_mentions. If the tweet consists only out of links and/or @user_mentions the tweet is deleted and not used any further.

3. user_tweets_analysis.py In this file the function ```create_sentiments()``` estimates the polarity (how negativ or positive a tweet is) and the subjectivity (how objective or subjective a tweet is). For this task the [libary Textblob](https://textblob.readthedocs.io/en/dev/) and [nltk](https://www.nltk.org/) is used bc they are lightweight and easy to implement

4. fake_news_prediction.py In this file the function ```fake_news_prediction()``` uses a pretrainend [BERT Model](https://huggingface.co/blog/bert-101), to predict whether or not a tweet is Fake News or not. The Model is pretrained on a Fake News Dataset in the Fake_News_Predicition.ipynb

5. wordcloud_creator.py In this file the function ```create_wordCloud``` creates a Wordcloud image. The tweets are first cleaned of any topwords or punctuation using nltk. After that the Wordcloud is created through the wordcloud library.

6. backend.py In this file the function ```backend()``` combines all the previous functions and calculates the Polarity, Subjectivity, Percentage of Fake News and renders a wordcloud with the biggest topics which would then be given to the frontend. For now the results are saved in the data and img directory

  
