import os
import tweepy as tw
import pandas as pd
import json


#reads the credentials from the credentials json
credential_file = 'credentials/twitter_api_key_credentials.json'
cred = {}
with open(credential_file) as json_file:
    cred = json.load(json_file)    

# safes the credentials needed for the twitter API
consumer_key= cred['consumer_key']
consumer_secret= cred['consumer_secret']
access_token= cred['access_token']
access_token_secret= cred['access_token_secret']

# auth process for the twitter api
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#muss im nachinein geändert werden, hier soll dann eine Variable übergeben werden, evtl noch umschreiben zu einer Funktion
eingabe = 'elonmusk'
user = api.get_user(screen_name = eingabe)

user_id = user.id

tweets = api.user_timeline(screen_name=user_id, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

for info in tweets[:3]:
     print("ID: {}".format(info.id))
     print(info.created_at)
     print(info.full_text)
     print("\n")

all_tweets = []
all_tweets.extend(tweets)
oldest_id = tweets[-1].id
while True:
    tweets = api.user_timeline(screen_name=user_id, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           max_id = oldest_id - 1,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )
    if len(tweets) == 0:
        break
    oldest_id = tweets[-1].id
    all_tweets.extend(tweets)
    print('N of tweets downloaded till now {}'.format(len(all_tweets)))

tweets.full_text.encode("utf-8")
outtweets = [[tweet.id_str, 
              tweet.created_at, 
              tweet.favorite_count, 
              tweet.retweet_count, 
              tweet.full_text.encode("utf-8").decode("utf-8")] 
             for idx,tweet in enumerate(all_tweets)]
df = pd.DataFrame(outtweets,columns=["id","created_at","favorite_count","retweet_count", "text"])
df.to_csv('%s_tweets.csv' % user_id,index=False)
df.head(3)
