#based on this tutorial https://medium.com/dataseries/how-to-scrape-millions-of-tweets-using-snscrape-195ee3594721

# importing libraries and packages
import snscrape.modules.twitter as sntwitter
import pandas as pd

def get_tweets(username, number_of_tweets):
    # Creating list to append tweet data 
    tweets_list = []
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{username}').get_items()): #declare a username 
        if i>number_of_tweets: #number of tweets you want to scrape
            break
        if i % 100 == 0:
            print(i)
        tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username, tweet.user.followersCount, tweet.user.location, tweet.replyCount, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.lang, tweet.hashtags]) #declare the attributes to be returned
    
    # Creating a dataframe from the tweets list above 
    #print(tweets_list)
    tweets_df = pd.DataFrame(tweets_list, columns=['datetime', 'tweet_Id', 'text', 'username', 'user_followersCount', 'user_location', 'tweet_replyCount', 'tweet_retweetCount', 'tweet_likeCount', 'tweet_quoteCount', 'tweet_lang', 'tweet_hashtags'])
    #print(tweets_df)
    path_to_save = f'./data/{username}_last_{number_of_tweets}.pkl'
    tweets_df.to_pickle(path_to_save)
    return path_to_save
    

#get_tweets('elonmusk', 100)