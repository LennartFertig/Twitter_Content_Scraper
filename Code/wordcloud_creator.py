import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def create_wordCloud(path_to_df):
    df = pd.read_pickle(path_to_df)
    
    stringOfWords = df['text'].str.cat()    
    textTokens = word_tokenize(stringOfWords)
    tokens_without_sw = [word for word in textTokens if not word in stopwords.words()]
    
    word_cloud = WordCloud(collocations = True, background_color = 'white').generate((" ").join(tokens_without_sw))
    word_cloud.to_file("img/wordcloud.png")