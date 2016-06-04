#!/usr/bin/python

import os
import sys

if __name__ == '__main__':

    os.system("clear")

    print "\nRunning main.py -- Tweet Miner\n\n"

    if len(sys.argv) < 2:
        while True:
            file_name = raw_input("Enter data file name: ")
            path = "data/" + file_name + '.txt'
            if not os.path.isfile(path):
                break
            else:
                print "Error: File already exists."
                flag = raw_input("Continue with this name? (y/n): ")
            if flag == 'y':
                break
        args = raw_input("Enter miner arguements separated by spaces: ").strip().split(' ')
    else:
        file_name = sys.argv[1]
        path = "data/" + file_name + '.txt'
        args = sys.argv[2:]
        while os.path.isfile(path):
            print "Error: File already exists."
            flag = raw_input("Continue with this name? (y/n): ")
            if flag == 'y':
                break
            else:
                file_name = raw_input("Enter data file name: ")
                path = "data/" + file_name + '.txt'

    params = file_name + " " + " ".join(args)
    status = "Filename: %s.txt\nSearch terms: %s" % (file_name, args)
    print "\n%s\n" % status

    while True:
        start = raw_input("Type data file name again to start mining: ")
        if start == file_name:
            break
        else:
            print "Error: Names did not match.\n"

    print "\n\nInitializing Mining. Press Ctrl+C to quit.\n\n"
    if not os.path.isfile(path):
        os.system("touch data/%s.txt" % file_name)
    os.system("python scripts/miner.py %s" % params)
