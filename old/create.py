#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:58:39 2018

@author: Evgeny Galimov
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy.random as np
import sys
import matplotlib



global wormlist
wormlist = list()
# dictionary for creating a dataframe for each worm
global d
d = {}
#######
# list to create L0 stage of worm
a_state = "L0"
a_progeny = 0
a_hungry = 0
a_fruit_n = 1
a_time = 0

a=list()
a.append(a_state)
a.append(a_progeny)
a.append(a_hungry)
a.append(a_fruit_n)
a.append(a_time)
a



######
#######   list with worm names
#wormlist = list()
## dictionary for creating a dataframe for each worm
#d = {}

# set number of newborn worm: i.e.  new_number=2

# creates new_number of new worms and adds to existing list wormlist
def CreateWorm(new_number, wormlist):
    for i1 in range(1, new_number+1):
        temp=len(wormlist)-1
        temp=temp+2
        temp= "worm_"+str(temp)
               
        wormlist.append(temp)
        # create empty df for a new worm
        d[temp] = pd.DataFrame()
        # appending newborn data to the new worm
        d[temp] = d[temp].append(pd.Series(a, index=['1_state','2_progeny','3_hungry','4_fruit_number', '5_time']), ignore_index=True)

#############
# list to create D1 stage of worm
a_state1 = "D1"
a_progeny1 = 0
a_hungry1 = 0
a_fruit_n1 = 1
a_time1 = 0

a1=list()
a1.append(a_state)
a1.append(a_progeny)
a1.append(a_hungry)
a1.append(a_fruit_n)
a1.append(a_time)
a1        

def CreateWorm_d(new_number, wormlist):
    for i1 in range(1, new_number+1):
        temp=len(wormlist)-1
        temp=temp+2
        temp= "worm_"+str(temp)
               
        wormlist.append(temp)
        # create empty df for a new worm
        d[temp] = pd.DataFrame()
        # appending newborn data to the new worm
        d[temp] = d[temp].append(pd.Series(a1, index=['1_state','2_progeny','3_hungry','4_fruit_number', '5_time']), ignore_index=True)
        


