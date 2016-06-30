#!/usr/bin/python

import os
import sys
import time

if __name__ == '__main__':

    # format:
    # python main.py [stock_ticker] [param_list]

    # Need to be passed to analyse/miner
    stock_ticker = sys.argv[1]
    param_list = sys.argv[2:]
    file_name = "data_" + time.strftime("%d_%m_%Y")

    os.system("python miner.py " + file_name + " " + " ".join(param_list))
    os.system("python analyse.py " + file_name + " " + stock_ticker)
