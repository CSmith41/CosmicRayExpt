# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:39:07 2020

@author: Cameron
"""

#!/usr/bin/env python

# data analysis example program
# Including some examples of how to use DataFrames from pandas
#
# Usage :
# python analysis.py -i test.dat

import pickle
import numpy as np
import matplotlib.pyplot as plt
import argparse

from event import Event, Pulse

parser = argparse.ArgumentParser(description='Analyse CSV file')
parser.add_argument("-i", "--in_file", help="input file 1")
#parser.add_argument("-i1", "--in_file1", help="input file 2") #Uncomment if making possible to add any filename instead of set ones
#parser.add_argument("-i1", "--in_file1", help="input file 2")
#parser.add_argument("-i2", "--in_file2", help="input file 3")
#parser.add_argument("-i3", "--in_file3", help="input file 4")
#parser.add_argument("-i4", "--in_file4", help="input file 5")
#parser.add_argument("-i5", "--in_file5", help="input file 6")
#parser.add_argument("-i6", "--in_file6", help="input file 7")
#parser.add_argument("-i7", "--in_file7", help="input file 8")
#parser.add_argument("-i8", "--in_file8", help="input file 9")
#parser.add_argument("-i9", "--in_file9", help="input file 10")
parser.add_argument("-o", "--out_file", help='output file')
parser.add_argument("-n", "--n_max", help='max number of lines to process')

args = parser.parse_args()

print("Starting analysis")

# event loop
count1000 = [0, 0, 0, 0] 
count900 = [0, 0, 0, 0]
count800 = [0, 0, 0, 0]
count700 = [0, 0, 0, 0]
count600 = [0, 0, 0, 0]
count500 = [0, 0, 0, 0] # counts per channel

def Count(countl,file):
    
    ifile = open(file)
    events= pickle.load(ifile)
    
    for event in events:
        for pulse in event.pulses:
            # only count rising edges
            if pulse.edge == 0:
                countl[pulse.chan] += 1
    return countl
    
Count(count1000, "0Chan1000test.dat") #Make sure file 1 has highest thresh, file 6 lowest etc
Count(count900, "0Chan900test.dat")  
Count(count800, "0Chan800test.dat")  #Change filename to "args.in_file1" to add any file
Count(count700, "0Chan700test.dat")
Count(count600, "0Chan600test.dat")
Count(count500, "0Chan500test.dat")
#IMPORTANT: Change filenames to whatever data to analyse

bins = [count1000[0], count900[0],count800[0],count700[0],count600[0],count500[0]]
rate = np.divide(bins, 30.)
thresh = [1000,900,800,700,600,500] #IMPORTANT: Change thresholds accordingly
error = np.divide([np.sqrt(x) for x in bins], 30.)

plt.errorbar(thresh, rate, yerr=error, fmt = '.k')
#IMPORTANT: Change number to however many seconds data ran for
plt.ylabel("Rate (Hz)")
plt.xlabel('Threshold (mV)')
plt.show()
