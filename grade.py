#!/usr/bin/python

import sys
from vaderSentiment.vaderSentiment import sentiment

print sys.argv[1],
print "\n\t%s" % sentiment(sys.argv[1])