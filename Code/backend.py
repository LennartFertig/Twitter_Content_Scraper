import pandas as pd
from twitter_scraper import get_tweets
from user_tweets_analysis import create_sentiments

def backend(twitter_user_name='elonmusk'):
  number_of_tweets = 500
  tweets_file_path = get_tweets(twitter_user_name, number_of_tweets)
  tweets = create_sentiments(tweets_file_path)
  print(tweets)
  
  # estimate subjectivity of user
  user_subjectivity_value = tweets['subjectivity_sentiment'].mean()
  if user_subjectivity_value >= 0.7:
    user_subjectivity = 'subjective'
  elif user_subjectivity_value < 0.3:
    user_subjectivity = 'objective'
  else:
    user_subjectivity = 'sometimes subjective, sometimes objctive'
  
  user_polarity = tweets['negative_positive_sentiment'].mean()
  print(f'User is {user_subjectivity} and ')

backend()