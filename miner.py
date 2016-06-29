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
            data_clone = json.loads(data)
            save_data = {
                "created_at":   data_clone["created_at"],
                "text":         data_clone["text"],
                "user":         data_clone["user"]["screen_name"],
                "followers":    data_clone["user"]["followers_count"],
                "score":        sentiment(data_dict["text"].encode('utf-8'))
            }
            print "Created at: %s by @%s\n%s\n" % (save_data["created_at"], save_data["user"], save_data["text"])
            for line in save_data["score"]:
                print line
                print data_dict["score"][line]
            print ""
        except Exception, e:
            print "Error: %s.\n" % e
        with open('data/' + sys.argv[1] + '.txt', 'a') as f:
            f.writelines(json.dumps(save_data))
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
