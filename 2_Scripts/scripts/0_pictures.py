#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 21:12:11 2018

@author: evgenigalimov
"""

import pandas as pd
import numpy as np
import os.path
import matplotlib.pyplot as plt


###### Parser
import argparse
# initialize parser
parser = argparse.ArgumentParser()
# add argument 1
parser.add_argument("param1", help="file name",
                    type=str)
# pass arguments to the list args
args = parser.parse_args()
name_f = args.param1   





#name_f = '/tables_no0'
current_directory = os.getcwd()

wd = current_directory + name_f

# choose all files in the current dir starting with '3'
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(wd) if (isfile(join(wd, f)) \
        and ((f[0]=='0') or (f[0]=='1') or (f[0]=='2') or (f[0]=='3') or (f[0]=='4') or \
             (f[0]=='5') or (f[0]=='6') or (f[0]=='7') or (f[0]=='8') or (f[0]=='9') )      )]

onlyfiles.sort() 


by_condition = wd + '/' + 'by_condition'
if not os.path.exists(by_condition):
    os.makedirs(by_condition)

sum_max_c = by_condition + '/' + 'sum_max_c'
if not os.path.exists(sum_max_c):
    os.makedirs(sum_max_c)

L2S_ad_c = by_condition + '/' + 'L2S_ad_c'
if not os.path.exists(L2S_ad_c):
    os.makedirs(L2S_ad_c)
    
tab_c = by_condition + '/' + 'tab_c'
if not os.path.exists(tab_c):
    os.makedirs(tab_c)

final = by_condition + '/' + 'final'
if not os.path.exists(final):
    os.makedirs(final)

food_c_folder = by_condition + '/' + 'food_c_folder'
if not os.path.exists(food_c_folder):
    os.makedirs(food_c_folder)

temp = pd.read_csv(wd+ '/' + onlyfiles[0], sep=',', header=[0])
#temp = temp.sort_values(by=[3,1], ascending = [True, False])






for j in range(0, temp.shape[0]): 
    

    
    L2Slt = pd.DataFrame(np.zeros((len(onlyfiles), 20)))    
    name = 0
    for i in range(0,len(onlyfiles)):
        temp1 = pd.read_csv(wd+ '/' + onlyfiles[i], sep=',', header=[0])
        if name == 0:
            name  = str(round(temp1.iloc[j,2],6)) + '_' + str(round(temp1.iloc[j,4],6)) + '.csv'
        
        start_1 = int(onlyfiles[i].find("rep")) + 3
        stop_1 = start_1 + 3
        L2Slt.iloc[i,0] = int(onlyfiles[i][start_1:stop_1])
        L2Slt.iloc[i,1] = temp1.iloc[j,1]
        L2Slt.iloc[i,2] = temp1.iloc[j,2]
        L2Slt.iloc[i,3] = temp1.iloc[j,3]
        L2Slt.iloc[i,4] = temp1.iloc[j,4]
        L2Slt.iloc[i,5] = temp1.iloc[j,5]
        L2Slt.iloc[i,6] = temp1.iloc[j,6]
        L2Slt.iloc[i,7] = temp1.iloc[j,7]
            
        L2Slt.iloc[i,8] = temp1.iloc[j,8]
        L2Slt.iloc[i,9] = temp1.iloc[j,9]
        L2Slt.iloc[i,10] = temp1.iloc[j,10]        
            
        L2Slt.iloc[i,11] = temp1.iloc[j,11]
        L2Slt.iloc[i,12] = temp1.iloc[j,12]
        L2Slt.iloc[i,13] = temp1.iloc[j,13]    
        
        L2Slt.iloc[i,14] = temp1.iloc[j,14]
        L2Slt.iloc[i,15] = temp1.iloc[j,15]
        L2Slt.iloc[i,16] = temp1.iloc[j,16]
        L2Slt.iloc[i,17] = temp1.iloc[j,17] 
        L2Slt.iloc[i,18] = temp1.iloc[j,18] 
        L2Slt.iloc[i,19] = temp1.iloc[j,19] 
        
        
        
    L2Slt.columns = ['time','m2','m2_v','sfed','sfed_v','L2S','L2S_n','L2S_sem','L2Ssum','L2Ssum_n','L2Ssum_sem','L2Smax','L2Smax_n','L2Smax_sem','Ad','Ad_n','Ad_sem','Food_cond_ad','Food_cond_ad_n','Food_cond_ad_sem']
    L2Slt["Food_cond_ad_n_cumul"] = 0
    for i in range(0, L2Slt.shape[0]):
        sum_cons = 0
        for j in range(0, i+1):
            sum_cons = sum_cons + L2Slt.iloc[j,18]
        L2Slt.iloc[i,20] = sum_cons
    
    L2Slt = L2Slt.sort_values(by=['time'], ascending = [True])
    


    ax = plt.gca()
    sem_L2S = L2Slt['L2S_sem'].values.tolist()
    L2Slt.plot('time','L2S_n',kind='line',yerr = sem_L2S,ax=ax)
    sem_L2Sad = L2Slt['Ad_sem'].values.tolist()
    L2Slt.plot('time','Ad_n',kind='line',yerr = sem_L2Sad,ax=ax)
    plt.savefig(L2S_ad_c+'/'+name[:-4] +'L2S_ad.png', dpi=300)
    plt.close()
    
    ax = plt.gca()
    sem_L2Ssum = L2Slt['L2Ssum_sem'].values.tolist()
    L2Slt.plot('time','L2Ssum_n',kind='line',yerr = sem_L2Ssum,ax=ax)
    sem_L2Smax = L2Slt['L2Smax_sem'].values.tolist()
    L2Slt.plot('time','L2Smax_n',kind='line',yerr = sem_L2Smax,ax=ax)
    plt.savefig(sum_max_c+'/'+name[:-4] +'max_sum.png', dpi=300)
    plt.close()
    
    ax = plt.gca()
    sem_food = L2Slt['Food_cond_ad_sem'].values.tolist()
    L2Slt.plot('time','Food_cond_ad_n',kind='line',yerr = sem_food,ax=ax)
    L2Slt.plot('time','Food_cond_ad_n_cumul',kind='line',ax=ax)
    plt.savefig(food_c_folder+'/'+name[:-4] +'food_cons.png', dpi=300)
    plt.close()
    
    L2Slt.to_csv(tab_c+'/'+name, sep=',',index = False, encoding='utf-8')  