import os
import sys
import tweepy
import requests
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from textblob import TextBlob


# Login into twitter using twitter API
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
user = tweepy.API(auth)

# Where the csv file will live
FILE_NAME = 'historical.csv'


def stock_sentiment(quote, num_tweets):
    
    # Check if the sentiment for the stock symbol input is positive or negative, 
    # Return True if majority of valid tweets have positive sentiment
    list_of_tweets = user.search(quote, count=num_tweets)
    positive, null = 0, 0

    for tweet in list_of_tweets:
        blob = TextBlob(tweet.text).sentiment
        if blob.subjectivity == 0:
            null += 1
            next
        if blob.polarity > 0:
            positive += 1

    if positive > ((num_tweets - null)/2):
        return True


def get_historical(quote):
    
    # Download the historical data(historical.csv) from google finance
    url = 'http://www.google.com/finance/historical?q=NASDAQ%3A'+quote+'&output=csv'
    r = requests.get(url, stream=True)

    if r.status_code != 400:
        with open(FILE_NAME, 'wb') as f:
            for chunk in r:
                f.write(chunk)

        return True

def stock_prediction():

    # Collect data points from the csv file
    dataset = []

    with open(FILE_NAME) as fr:
        for n, line in enumerate(fr):
            if n != 0:
                dataset.append(float(line.split(',')[1]))

    dataset = np.array(dataset)

    # Create dataset matrix (X=t and Y=t+1)
    def create_dataset(dataset):
        dataX = [dataset[n+1] for n in range(len(dataset)-2)]
        return np.array(dataX), dataset[2:]
        
    trainX, trainY = create_dataset(dataset)


# Ask user for a stock symbol
stock_quote = input("Enter a stock symbol from NASDAQ (e.j: AAPL, FB, GOOGL): ").upper()

# Check if the stock sentiment is positive
if not stock_sentiment(stock_quote, num_tweets=100):
    print ("This stock has bad sentiment, please re-run the script")
    sys.exit()

# Check if we have the historical data from Google finance
if not get_historical(stock_quote):
    print ("Google returned a 404, please re-run the script and")
    print ("enter a valid stock quote from NASDAQ")
    sys.exit()

# Run the neural net to get the prediction
stock_prediction()

# Delete the csv file after processing
os.remove(FILE_NAME)
