#based on this tutorial https://www.simonlindgren.com/notes/2017/11/7/scrape-tweets-without-using-the-api

import twint
import pandas as pd

def get_tweets(username):
    # Configure
    c = twint.Config()
    c.Limit = 1000
    c.Username = username
    c.Store_csv = True
    # Run
    twint.run.Search(c)

#get_tweets('elonmusk')

c = twint.Config()
c.Username = "realDonaldTrump"
c.Search = "great"
# Run
print(twint.run.Search(c))