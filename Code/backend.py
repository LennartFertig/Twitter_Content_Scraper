import pandas as pd
from twitter_scraper import get_tweets
from clean_tweets import clean_tweets
from user_tweets_analysis import create_sentiments
from fake_news_prediction import fake_news_prediction

def backend(twitter_user_name='elonmusk'):
  number_of_tweets = 500
  tweets_file_path = get_tweets(twitter_user_name, number_of_tweets)
  clean_tweets(tweets_file_path)
  create_sentiments(tweets_file_path)
  fake_news_prediction(tweets_file_path)
  tweets = pd.read_pickle(tweets_file_path)
  print(tweets)
  
  # estimate subjectivity of user
  user_subjectivity_value = tweets['subjectivity_sentiment'].mean()
  if user_subjectivity_value >= 0.7:
    user_subjectivity = 'mostly subjective'
  elif user_subjectivity_value < 0.3:
    user_subjectivity = 'mostly objective'
  else:
    user_subjectivity = 'sometimes subjective, sometimes objctive'
  
  # estimate polarity of user
  user_polarity_value = tweets['negative_positive_sentiment'].mean()
  if user_polarity_value > 0:
    user_polarity = 'positive'
  elif user_polarity_value < 0:
    user_polarity = 'negative'
  else:
    user_polarity = 'neutral'
  
  # estimate Fake/true news of user
  count_fake_news = tweets.loc[tweets['fake_news'] == ].count()
  
  count_true_news = tweets.loc[tweets['fake_news'] == ].count()
  
  count_all_tweets = len(tweets)
  
  share_of_fake_news = round((count_fake_news / count_all_tweets) * 100, 2)

  
  print(f'Tweets of the {twitter_user_name} are {user_subjectivity} and {user_polarity}')
  print(f'{share_of_fake_news}% of {twitter_user_name} are FakeNews')

backend()