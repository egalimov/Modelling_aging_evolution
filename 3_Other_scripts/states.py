#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 14:02:36 2018

@author: Evgeny Galimov
"""

#states

# L0
# LS2 -> LS9  if no food
# L1
# D1 -> D90   if no food
# L2
# A3 - A##   until death
# B   - bagging   if no food for A3-A7
# DEAD

# list to create L0 stage of worm
state = "L1"
progeny = 0
hungry = 0
fruit_n = 1
time = 11

b=list()
b.append(state)
b.append.(progeny)
b.append(hungry)
b.append(fruit_n)
b.append.(time)
#
d['worm_1'] = d['worm_1'].append(pd.Series(a, index=['1_state','2_progeny','3_hungry',
 '4_fruit_number', '5_time']), ignore_index=True)

             

for time in range(1,3):
    for x in wormlist:
        aaa =d[x].iloc[-1]['1_state']
        print(aaa)
        
d[wormlist[0]]

aaa= d['worm_1']['1_state']
aaa

d['worm_1'].iloc[-1]['1_state']
