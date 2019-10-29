#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:28:09 2018

@author: Evgeny Galimov
"""

import random


f_states_L=['L0','L1','L2']
f_states_LS=['SL2', 'SL3','SL4','SL5','SL6','SL7','SL8','SL9']
f_states_D=['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10',
            'D11','D12','D13','D14','D15','D16','D17','D18','D19',
            'D21','D22','D23','D24','D25','D26','D27','D28', 'D29',
            'D31','D32','D33','D34','D35','D36','D37','D38', 'D39',
            'D41','D42','D43','D44','D45','D46','D47','D48', 'D49',
            'D51','D52','D53','D54','D55','D56','D57','D58', 'D59',
            'D61','D62','D63','D64','D65','D66','D67','D68', 'D69',
            'D71','D72','D73','D74','D75','D76','D77','D78', 'D79',
            'D81','D82','D83','D84','D85','D86','D87','D88', 'D89']
f_states_B=['B']
f_states_DEAD=['dead']


######
# set rules for worm state change 
def mort(state):
    if state == 'A1':
        r = random.uniform(0, 1)
        if r > 0.8: 
            m = 1
        elif r <= 0.8:
            m=0
    if state == 'A2':
        r = random.uniform(0, 1)
        if r > 0.95: 
            m = 1
        elif r <= 0.95:
            m=0
    if state == 'A3':
        r = random.uniform(0, 1)
        if r > 0.95: 
            m = 1
        elif r <= 0.95:
            m=0
    if state == 'A4':
        r = random.uniform(0, 1)
        if r > 0.9: 
            m = 1
        elif r <= 0.9:
            m=0
    if state == 'A5':
        r = random.uniform(0, 1)
        if r > 0.8: 
            m = 1
        elif r <= 0.8:
            m=0
    if state == 'A6':
        r = random.uniform(0, 1)
        if r > 0.6: 
            m = 1
        elif r <= 0.6:
            m=0
    if state == 'A7':
        r = random.uniform(0, 1)
        if r > 0.4: 
            m = 1
        elif r <= 0.4:
            m=0
    if state == 'A8':
        r = random.uniform(0, 1)
        if r > 0.3: 
            m = 1
        elif r <= 0.3:
            m=0
    if state == 'A10':
        m=1
    if state == 'B':
        m = 1
    if any(x == state for x in f_states_L):
        m=0
    if any(x == state for x in f_states_LS):
        m=0
    if any(x == state for x in f_states_D):
        m=0    
    if any(x == state for x in f_states_DEAD):
        m=1
    return m



# state = d['worm_1'].iloc[-1]['1_state']

# z = list()
# for i in range(1,10000):
#     z.append(mort(state))


