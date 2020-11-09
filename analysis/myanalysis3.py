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
parser.add_argument("-i", "--in_file", help="input file")
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
count = [0,0,0,0] 
# counts per channel

def Count(countl,file):
    
    ifile = open(file)
    events = pickle.load(ifile)
    
    for event in events:
        for pulse in event.pulses:
            # only count rising edges
            if pulse.edge == 0:
                countl[pulse.chan] += 1
    return count1

def NumCounts(file):
    
    ifile = open(file)
    events = pickle.load(ifile)
    n_events = len(events)

    return n_events
    
def Eff(file):

    ifile = open(file)
    events = pickle.load(ifile)
    
    n_coinc1 = 0 # True no. of events  
    n_coinc2 = 0 # Total no. of triggered events

    for event in events:
	found0 = False
	found1 = False
	found2 = False
	for pulse in event.pulses:
	    # only count rising edges
	    if pulse.edge == 0 and pulse.chan == 1: # Ref channel 1
		found0 = True
	    if pulse.edge == 0 and pulse.chan == 3: # Channel finding efficiency of
		found1 = True
	    if pulse.edge == 0 and pulse.chan == 2: # Ref channel 2
		found2 = True
	if found0 and found1 and found2:
		n_coinc1 += 1
	if found0 and found2:
		n_coinc2 += 1

    n_coinc1 = np.float(n_coinc1)
    n_coinc2 = np.float(n_coinc2)

    efficiency = n_coinc1/n_coinc2
    
    uncertainty = np.sqrt(((np.sqrt(n_coinc1)/n_coinc2)**2)+((n_coinc1*np.sqrt(n_coinc2))/((n_coinc2)**2))**2)

    return efficiency,uncertainty,n_coinc1,n_coinc2  


def Decay(file):

    ifile = open(file)
    events = pickle.load(ifile)	

    decays = 0.
    t_decay = []

    t_decay0 = []
    t_decay1 = []
    t_decay2 = []
    t_decay3 = []

    for event in events:
	found0 = False
	found1 = False
	found2 = False
	found3 = False
	time0 = 0.
	time1 = 0.
	time2 = 0.
	time3 = 0.

	foundlate0 = False
	foundlate1 = False
	foundlate2 = False
	foundlate3 = False
	timelate0 = 0.
	timelate1 = 0.
	timelate2 = 0.
	timelate3 = 0.

	muon_stop = False
	
	for pulse in event.pulses:
	    if pulse.edge==0 and pulse.chan == 0 and pulse.time <= 40: # Can vary time cond.
		found0 = True
		time0 = pulse.time
	    if pulse.edge==0 and pulse.chan == 1 and pulse.time <= 40:
		found1 = True
		time1 = pulse.time
	    if pulse.edge==0 and pulse.chan == 2 and pulse.time <= 40:
		found2 = True
		time2 = pulse.time
	    if pulse.edge==0 and pulse.chan == 3 and pulse.time <= 40:
		found3 = True
		time3 = pulse.time		
       	if found0 and found1 and not found2 and not found3:
	    muon_stop = True
	    decays += 1.       #Adds 1 to no. decays if event has a stopping muon. Decays is no. events with a muon decay.

	if muon_stop:
	    for pulse in event.pulses:
		if pulse.edge==0 and pulse.chan == 0 and pulse.time > 40:
		    foundlate0 = True
		    timelate0 = pulse.time
		if pulse.edge==0 and pulse.chan == 1 and pulse.time > 40:
		    foundlate1 = True
		    timelate1 = pulse.time
		if pulse.edge==0 and pulse.chan == 2 and pulse.time > 40:
		    foundlate2 = True
		    timelate2 = pulse.time
		if pulse.edge==0 and pulse.chan == 3 and pulse.time > 40:
	  	    foundlate3 = True
		    timelate3 = pulse.time

	    if foundlate0 and not foundlate2 and not foundlate3:
		t_decay.append(timelate0)
		t_decay0.append(timelate0)
	    if foundlate1 and not foundlate2 and not foundlate3:
		t_decay.append(timelate1)
		t_decay1.append(timelate1)
	    if foundlate2 and not foundlate0 and not foundlate1:
		t_decay.append(timelate2)
		t_decay2.append(timelate2)
	    if foundlate3 and not foundlate0 and not foundlate1:
		t_decay.append(timelate3)
		t_decay3.append(timelate3)

    return decays, t_decay, t_decay0, t_decay1, t_decay2, t_decay3


#Count(count, args.in_file)

#print("Counts by channel")
#print("Channel 0 : {} ".format(count[0]))
#print("Channel 1 : {} ".format(count[1]))
#print("Channel 2 : {} ".format(count[2]))
#print("Channel 3 : {} ".format(count[3])) 

#print("Read {} events from file".format(NumCounts(args.in_file)))


#print("Number of decaying muons is {}".format(Decay(args.in_file)[0]))

print("General list of decay times")
print(Decay(args.in_file)[1])

print("List of decay times by channel")
print("Channel 0: {}".format(Decay(args.in_file)[2]))
print("Channel 1: {}".format(Decay(args.in_file)[3]))
print("Channel 2: {}".format(Decay(args.in_file)[4]))
print("Channel 3: {}".format(Decay(args.in_file)[5]))

