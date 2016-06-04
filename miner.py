#!/usr/bin/python

import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler, Stream

# Access Tokens
ACCESS_TOKEN = "3759161294-4BTsEaIZ5imG1zwuif6aTH4DRDdWwCiasN0J1ru"
ACCESS_TOKEN_SECRET = "RZxtnE4ClPUsRmkBb8JiUB9AaH9Co2oDPobpR9iJa3rah"
CONSUMER_KEY = "dTsJNrZbZdXvP1H1UuiVRzDLo"
CONSUMER_KEY_SECRET = "hRSWlmfFs1RmwSNfrRv7h1TRMsw8HdbcSf1FaToc6qeJoOuYYW"

# Stream Listener; saves streams to data/file_name.txt
class JSONListener(StreamListener):

    def on_data(self, data):
        with open('data/' + sys.argv[1] + '.txt', 'a') as f:
            f.writelines(data)
        return True

    def on_error(self, status):
        print "\nError: %s\n" % (status)


if __name__ == '__main__':

    print "\n\nMining Started"
    print "Filename: %s" % sys.argv[1]
    print "Parameters: %s\n\n" % sys.argv[2:]

    listener = JSONListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    input_stream = Stream(auth, listener)
    input_stream.filter(track=sys.argv[2:])
