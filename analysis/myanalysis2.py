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
count200 = [0,0,0,0]
count220 = [0,0,0,0]
count240 = [0,0,0,0]
count260 = [0,0,0,0]
count280 = [0,0,0,0]
count300 = [0,0,0,0]
count320 = [0,0,0,0]
count340 = [0,0,0,0]
count360 = [0,0,0,0]
count380 = [0,0,0,0]
count400 = [0,0,0,0]
count420 = [0,0,0,0]
count440 = [0,0,0,0]
count460 = [0,0,0,0]
count480 = [0,0,0,0]
count500 = [0,0,0,0]
count520 = [0,0,0,0]
count540 = [0,0,0,0]
count560 = [0,0,0,0]
count580 = [0,0,0,0]
count600 = [0,0,0,0] 
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
    
Count(count200, "2fthresh200.dat") #Make sure file 1 has highest thresh, file 6 lowest etc
Count(count220, "2fthresh220.dat")  
Count(count240, "2fthresh240.dat")  #Change filename to "args.in_file1" to add any file
Count(count260, "2fthresh260.dat")
Count(count280, "2fthresh280.dat")
Count(count300, "2fthresh300.dat")
Count(count320, "2fthresh320.dat")
Count(count340, "2fthresh340.dat")
Count(count360, "2fthresh360.dat")
Count(count380, "2fthresh380.dat")
Count(count400, "2fthresh400.dat")
Count(count420, "2fthresh420.dat")
Count(count440, "2fthresh440.dat")
Count(count460, "2fthresh460.dat")
Count(count480, "2fthresh480.dat")
Count(count500, "2fthresh500.dat")
Count(count520, "2fthresh520.dat")
Count(count540, "2fthresh540.dat")
Count(count560, "2fthresh560.dat")
Count(count580, "2fthresh580.dat")
Count(count600, "2fthresh600.dat")
#IMPORTANT: Change filenames to whatever data to analyse

counts_ch0 = [count200[0],count220[0],count240[0],count260[0],count280[0],count300[0],count320[0],count340[0],count360[0],count380[0],count400[0],count420[0],count440[0],count460[0],count480[0],count500[0],count520[0],count540[0],count560[0],count580[0],count600[0]]

counts_ch1 = [count200[1],count220[1],count240[1],count260[1],count280[1],count300[1],count320[1],count340[1],count360[1],count380[1],count400[1],count420[1],count440[1],count460[1],count480[1],count500[1],count520[1],count540[1],count560[1],count580[1],count600[1]]

counts_ch2 = [count200[2],count220[2],count240[2],count260[2],count280[2],count300[2],count320[2],count340[2],count360[2],count380[2],count400[2],count420[2],count440[2],count460[2],count480[2],count500[2],count520[2],count540[2],count560[2],count580[2],count600[2]]

counts_ch3 = [count200[3],count220[3],count240[3],count260[3],count280[3],count300[3],count320[3],count340[3],count360[3],count380[3],count400[3],count420[3],count440[3],count460[3],count480[3],count500[3],count520[3],count540[3],count560[3],count580[3],count600[3]]

thresh = [200,220,240,260,280,300,320,340,360,380,400,420,440,460,480,500,520,540,560,580,600] #IMPORTANT: Change thresholds accordingly
time = 300.   #IMPORTANT: Change time accordingly

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
plt.errorbar(thresh, rate3, yerr=error3, fmt = 'y', label = 'Channel 3')
plt.ylabel("Rate (Hz)")
plt.xlabel('Threshold (mV)')
plt.legend()
plt.show()
