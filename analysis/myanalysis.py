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
count1000 = [0,0,0,0]
count900 = [0,0,0,0]
count800 = [0,0,0,0]
count700 = [0,0,0,0]
count600 = [0,0,0,0]
count500 = [0,0,0,0]
count400 = [0,0,0,0]
count300 = [0,0,0,0]
count200 = [0,0,0,0]
count100 = [0,0,0,0] 
# counts per channel

def Count(countl,file):
    
    ifile = open(file)
    events= pickle.load(ifile)
    
    for event in events:
        for pulse in event.pulses:
            # only count rising edges
            if pulse.edge == 0:
                countl[pulse.chan] += 1
    return countl
    
Count(count1000, "thresh1000.dat") #Make sure file 1 has highest thresh, file 6 lowest etc
Count(count900, "thresh900.dat")  
Count(count800, "thresh800.dat")  #Change filename to "args.in_file1" to add any file
Count(count700, "thresh700.dat")
Count(count600, "thresh600.dat")
Count(count500, "thresh500.dat")
Count(count400, "thresh400.dat")
Count(count300, "thresh300.dat")
Count(count200, "thresh200.dat")
Count(count100, "thresh100.dat")
#IMPORTANT: Change filenames to whatever data to analyse

counts_ch0 = [count1000[0],count900[0],count800[0],count700[0],count600[0],count500[0],count400[0],count300[0],count200[0],count100[0]]
counts_ch1 = [count1000[1],count900[1],count800[1],count700[1],count600[1],count500[1],count400[1],count300[1],count200[1],count100[1]]
counts_ch2 = [count1000[2],count900[2],count800[2],count700[2],count600[2],count500[2],count400[2],count300[2],count200[2],count100[2]]
counts_ch3 = [count1000[3],count900[3],count800[3],count700[3],count600[3],count500[3],count400[3],count300[3],count200[3],count100[3]]

thresh = [1000,900,800,700,600,500,400,300,200,100] #IMPORTANT: Change thresholds accordingly
time = 300   #IMPORTANT: Change time accordingly

error0 = [np.sqrt(x)/time for x in counts_ch0]
error1 = [np.sqrt(x)/time for x in counts_ch1]
error2 = [np.sqrt(x)/time for x in counts_ch2]
error3 = [np.sqrt(x)/time for x in counts_ch3]
rate0 = [x/time for x in counts_ch0]
rate1 = [x/time for x in counts_ch1]
rate2 = [x/time for x in counts_ch2]
rate3 = [x/time for x in counts_ch3]

plt.errorbar(thresh, rate0, yerr=error0, fmt = 'b', label = 'Channel 0')
plt.errorbar(thresh, rate1, yerr=error1, fmt = 'g', label = 'Channel 1')
plt.errorbar(thresh, rate2, yerr=error2, fmt = 'r', label = 'Channel 2')
plt.errorbar(thresh, rate3, yerr=error3, fmt = 'm', label = 'Channel 3')
plt.ylabel("Rate (Hz)")
plt.xlabel('Threshold (mV)')
plt.legend()
plt.show()
