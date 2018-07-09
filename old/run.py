#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:58:39 2018

@author: Evgeny Galimov
"""

# to escape error with "A value is trying to be set on a copy of a slice from a DataFrame"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None  # default='warn'


from create import *
from f import *
from mort import *
from state_ch import *



#######   list with worm names



# create initial worms
new_number=10
CreateWorm(new_number, wormlist)

x='worm_1'


# food conditions
food = 4
ts_d = 3
ts_l0 = 3
ts_a = 3


for time in range(1,10):
    mmm=0
    for x in wormlist:
        state =d[x].iloc[-1]['1_state']
        m_temp = mort(state)
        b = ['A1',0,0,0,0]
        d[x] = d[x].append(pd.Series(b, index=['1_state','2_progeny','3_hungry',
     '4_fruit_number', '5_time']), ignore_index=True)
        if m_temp == 0:
            d[x]['1_state'].iloc[-1] = 'A1'
        d[x].iloc[-1]['1_state']
        if m_temp == 1:
            d[x]['1_state'].iloc[-1] = 'DEAD'
            mmm=mmm+1
    print(mmm)
        
        
        
        

        



        
        
        
#### temp
for time in range(1,3):
    
    if d[x].iloc[-1]['1_state'] == 'L0':
        d[x].iloc[-1]['1_state'] = 'L1'