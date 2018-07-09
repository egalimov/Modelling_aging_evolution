#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 13:58:39 2018

@author: Evgeny Galimov
"""
# L0
# LS2 -> LS9  if no food
# L1
# D1 -> D90   if no food
# L2
# A3 - A##   until death
# B   - bagging   if no food for A3-A7
# DEAD

# reproductive states of the worm

f_states_L=['L0','L1','L2']
f_states_SL=['SL2', 'SL3','SL4','SL5','SL6','SL7','SL8','SL9']
f_states_D=['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10',
            'D11','D12','D13','D14','D15','D16','D17','D18','D19','D20',
            'D21','D22','D23','D24','D25','D26','D27','D28', 'D29','D30',
            'D31','D32','D33','D34','D35','D36','D37','D38', 'D39','D40',
            'D41','D42','D43','D44','D45','D46','D47','D48', 'D49','D50',
            'D51','D52','D53','D54','D55','D56','D57','D58', 'D59','D60',
            'D61','D62','D63','D64','D65','D66','D67','D68', 'D69','D70',
            'D71','D72','D73','D74','D75','D76','D77','D78', 'D79','D80',
            'D81','D82','D83','D84','D85','D86','D87','D88', 'D89']
f_states_B=[
        ]
f_states_DEAD=['dead']
f_states_A = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
              'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18',
              'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
              'A28', 'A29', 'A29', 'A30', 'A1', 'A1', 'A1', 'A1', 'A1',]

#
#f0 = 50
#fd =1.7
######
# set rules for worm fertility 
def progeny_n(state):
    f=0
    if state[:1] == 'A' and food > ts_a:    #  Adults
        zz=int(state[1:])
        f = f0 - zz**fd
        f=round(f)
        if f < 0:
            f = 0
    elif state[:1] == 'A' and food <= ts_a and int(state[1:]) > 5:
        f = 0
    elif state[:1] == 'A' and food <= ts_a and (state == 'A1' or 'A2' or 'A3' or 'A4' or 'A5' ): 
        f = -1
    
    elif any(x == state for x in f_states_L):
        f=0
    elif any(x == state for x in f_states_SL):
        f=0
    elif any(x == state for x in f_states_D):
        f=0    
    elif any(x == state for x in f_states_DEAD):
        f=0 
    return f

#
##state = 'L1' 
#for state in x:    
#    zzz = progeny_n(state)
#    print(zzz)
#
##state=d['worm_1'].iloc[-1]['1_state']
##progeny_n(state)
#x = ['A1', 'A2','A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10',
#     'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18',
#     'A19', 'A20', 'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
#     'A28', 'A29', 'A29', 'A30',
#     'L0','L1','L2',
#     'SL2', 'SL3','SL4',
#     'D1','D2','D3','D4','D5',
#     'B',
#     'dead'
#     ]    
#
#food = 5
#ts_d = 3
#ts_l0 = 3
#ts_a = 3
#
#for state in x: 
#    zz=int(state[1:])
#    f = f0 - zz**fd
#    f=round(f)
#    if f < 0:
#        f = 0
#    print(f)
