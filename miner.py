#!/usr/bin/python

import os
import sys
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream
from vaderSentiment.vaderSentiment import sentiment

# Access Tokens
ACCESS_TOKEN = "3759161294-4BTsEaIZ5imG1zwuif6aTH4DRDdWwCiasN0J1ru"
ACCESS_TOKEN_SECRET = "RZxtnE4ClPUsRmkBb8JiUB9AaH9Co2oDPobpR9iJa3rah"
CONSUMER_KEY = "dTsJNrZbZdXvP1H1UuiVRzDLo"
CONSUMER_KEY_SECRET = "hRSWlmfFs1RmwSNfrRv7h1TRMsw8HdbcSf1FaToc6qeJoOuYYW"

# Stream Listener; saves streams to data/file_name.txt
class JSONListener(StreamListener):

    def on_data(self, data):
        try:
            data_dict = json.loads(data)
            data_tup = (data_dict["created_at"], data_dict["user"]["screen_name"], data_dict["text"])
            print "Created at: %s by @%s\n%s\n" % data_tup
            data_dict["score"] = sentiment(data_dict["text"].encode('utf-8'))
            for line in data_dict["score"]:
                print line
                print data_dict["score"][line]
            print ""
        except Exception, e:
            print "Error: %s.\n" % e
        with open('data/' + sys.argv[1] + '.txt', 'a') as f:
            f.writelines(json.dumps(data_dict))
        return True

    def on_error(self, status):
        print "\nError: %s\n" % (status)


if __name__ == '__main__':

    os.system("clear")

    print "\n\nMining Started"
    print "Filename: %s" % sys.argv[1]
    print "Parameters: %s\n\n" % sys.argv[2:]

    listener = JSONListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    input_stream = Stream(auth, listener)
    input_stream.filter(languages=["en"], track=sys.argv[2:])
