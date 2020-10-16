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
<<<<<<< HEAD
#parser.add_argument("-i1", "--in_file1", help="input file 2") #Uncomment if making possible to add any filename instead of set ones
=======
#parser.add_argument("-i1", "--in_file1", help="input file 2")
>>>>>>> 7f215a7fdb7ef647f7948d6049a3ede2d3509e81
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
    
<<<<<<< HEAD
Count(count1000, "0Chan1000test.dat") #Make sure file 1 has highest thresh, file 6 lowest etc
Count(count900, "0Chan900test.dat")  
Count(count800, "0Chan800test.dat")  #Change filename to "args.in_file1" to add any file
Count(count700, "0Chan700test.dat")
Count(count600, "0Chan600test.dat")
Count(count500, "0Chan500test.dat")
#IMPORTANT: Change filenames to whatever data to analyse

bins = [count1000[0], count900[0],count800[0],count700[0],count600[0],count500[0]]
thresh = [1000,900,800,700,600,500] #IMPORTANT: Change thresholds accordingly
error = [np.sqrt(x) for x in bins]

plt.errorbar(thresh, np.divide(bins,30.), yerr=error, fmt = '.k') 
#IMPORTANT: Change number to however many seconds data ran for
plt.ylabel("Rate (Hz)")
=======
Count(count1000, "0Chan1000test.dat") #Make sure file 1 has highest thresh, last file is lowest etc
Count(count900, "0Chan900test.dat") 
Count(count800, "0Chan800test.dat") #Change filename to "args.in_file1" if want to try, making it possible to run it on whatever files I input
Count(count700, "0Chan700test.dat") #Instead of only being able to run on certain files.
Count(count600, "0Chan600test.dat")
Count(count500, "0Chan500test.dat")
# IMPORTANT: Change filenames to whatever data I desire to analyse

bins = [count1000[0], count900[0],count800[0],count700[0],count600[0],count500[0]]
thresh = [1000,900,800,700,600,500] #IMPORTANT: Change numbers for whatever the threshold is.
plt.plot(thresh, bins/30) #IMPORTANT: Change the number to however many seconds the data ran for. E.g. test data ran for 30 seconds, so divide bins by 30
plt.ylabel("Events/Second")
>>>>>>> 7f215a7fdb7ef647f7948d6049a3ede2d3509e81
plt.xlabel('Threshold (mV)')
plt.show()
