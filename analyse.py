#!/usr/bin/python

import re
import sys
import json
import pandas
import urllib2
import matplotlib.pyplot as plotlib

TWEET_DATA_PATH = 'data/'
TWEET_DATA = []
TWEETS = pandas.DataFrame()
FOLLOWER_EXPONENT = 2

def match_words(word_list, text):
    text.lower()
    for word in word_list:
        word.lower()
        match = re.search(word, text)
        if match:
            return True
    return False



if __name__ == '__main__':

    # format:
    # python analyse.py [filename] [stockticker]

    # Creating intital path
    TWEET_DATA_PATH += sys.argv[1]

    # Reading data
    with open(TWEET_DATA_PATH + '.txt', 'r') as TWEET_FILE:
        for line in TWEET_FILE:
            try:
                tweet = json.loads(line)
                TWEET_DATA.append(tweet)
            except Exception, e:
                print "Error: %s.\n" % e
                continue

    # Moving data to Pandas for analysis
    # TWEETS["text"] = map(lambda tweet: tweet['text'], TWEET_DATA)
    # TWEETS["score"] = map(lambda tweet: tweet['score'], TWEET_DATA)
    # TWEETS["followers"] = map(lambda tweet: tweet['followers'], TWEET_DATA)

    # Data analysis
    mean_score = 0
    mean_score_normaliser = 0
    compound_score = 0
    compound_score_normaliser = 0
    
    for tweet in TWEET_DATA:

        weight = tweet["followers"]**FOLLOWER_EXPONENT
        tweet_score = tweet["score"]["compound"]

        mean_score += tweet_score
        mean_score_normaliser += 1

        compound_score += tweet_score*weight
        compound_score_normaliser += weight

    results = urllib2.urlopen('http://finance.yahoo.com/webservice/v1/symbols/' + sys.argv[2] + '/quote?format=json')
    stock_data = json.loads(results.read())

    RESULT_DATA = {
        'counted_tweets': mean_score_normaliser,
        'score': {
            'mean_score': mean_score/mean_score_normaliser,
            'compound_score': compound_score/compound_score_normaliser,
        },
        'stock': {
            'stock_name': sys.argv[2],
            'stock_price': stock_data["list"]["resources"][0]["resource"]["fields"]["price"]
        }   
    }

    with open(TWEET_DATA_PATH + '.json', 'w') as f:
        f.writelines(json.dumps(RESULT_DATA))
