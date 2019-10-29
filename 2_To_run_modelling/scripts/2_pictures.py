#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 22:15:38 2018

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




# choose all files in the current dir starting with '3'
from os import listdir
from os.path import isfile, join

current_directory = os.getcwd()
wd = current_directory + name_f
by_condition = wd + '/' + 'by_condition'
tab_c = by_condition + '/' + 'tab_c'
final = by_condition + '/' + 'final'



iteration = ['0.80','0.85','0.90','0.95','0.99']


#############################
# Analyses of the tables
        

# L2S all
onlyfiles2 = [f for f in listdir(tab_c)] #if (isfile(join(tab_c, f)) and f[:4]=='0.80')]
onlyfiles2.sort() 
NUM_COLORS = 50
cm = plt.get_cmap('gist_rainbow')

#
#  L2S   all
names = []
for i in range(0,len(onlyfiles2)):
    name = 0     
    temp1 = pd.read_csv(tab_c+ '/' + onlyfiles2[i], sep=',', header=[0])
    if name == 0:
        name  = str(round(temp1.iloc[1,2],6)) + '_' + str(round(temp1.iloc[1,4],6))
    names.append(name)
    
    ax = plt.gca() 
    #ax.set_prop_cycle('color',plt.cm.Spectral(np.linspace(0,1,30)))
    ax.set_prop_cycle(color=[cm(1.*i/NUM_COLORS)])
    temp1.plot('time','L2S_n',kind='line',ax=ax)
    
    ax.legend(names, loc='upper left', prop={'size': 3})
    
plt.savefig(final+'/'+'L2S_all.png', dpi=300)
plt.close()    

#  L2S   sum   all
names = []
for i in range(0,len(onlyfiles2)):
    name = 0     
    temp1 = pd.read_csv(tab_c+ '/' + onlyfiles2[i], sep=',', header=[0])
    if name == 0:
        name  = str(round(temp1.iloc[1,2],6)) + '_' + str(round(temp1.iloc[1,4],6))
    names.append(name)
    
    ax = plt.gca() 
    ax.set_prop_cycle(color=[cm(1.*i/NUM_COLORS)])
    temp1.plot('time','L2Ssum_n',kind='line',ax=ax)
    
    ax.legend(names, loc='upper left', prop={'size': 4})
plt.savefig(final+'/'+'L2S_sum_all.png', dpi=300)
plt.close()    


#  L2S   max   all
names = []
for i in range(0,len(onlyfiles2)):
    name = 0     
    temp1 = pd.read_csv(tab_c+ '/' + onlyfiles2[i], sep=',', header=[0])
    if name == 0:
        name  = str(round(temp1.iloc[1,2],6)) + '_' + str(round(temp1.iloc[1,4],6))
    names.append(name)
    
    ax = plt.gca() 
    ax.set_prop_cycle(color=[cm(1.*i/NUM_COLORS)])
    temp1.plot('time','L2Smax_n',kind='line',ax=ax)
    
    ax.legend(names, loc='upper left', prop={'size': 4})
plt.savefig(final+'/'+'L2S__max_all.png', dpi=300)
plt.close()    



#  L2S   ad   all
names = []
for i in range(0,len(onlyfiles2)):
    name = 0     
    temp1 = pd.read_csv(tab_c+ '/' + onlyfiles2[i], sep=',', header=[0])
    if name == 0:
        name  = str(round(temp1.iloc[1,2],6)) + '_' + str(round(temp1.iloc[1,4],6))
    names.append(name)
    
    ax = plt.gca() 
    ax.set_prop_cycle(color=[cm(1.*i/NUM_COLORS)])
    temp1.plot('time','Ad_n',kind='line',ax=ax)
    
    ax.legend(names, loc='upper left', prop={'size': 4})
plt.savefig(final+'/'+'Ad_all.png', dpi=300)
plt.close()    



#  food_cons    all
names = []
for i in range(0,len(onlyfiles2)):
    name = 0     
    temp1 = pd.read_csv(tab_c+ '/' + onlyfiles2[i], sep=',', header=[0])
    if name == 0:
        name  = str(round(temp1.iloc[1,2],6)) + '_' + str(round(temp1.iloc[1,4],6))
    names.append(name)
    
    ax = plt.gca() 
    ax.set_prop_cycle(color=[cm(1.*i/NUM_COLORS)])
    temp1.plot('time','Food_cond_ad_n_cumul',kind='line',ax=ax)
    
    ax.legend(names, loc='upper left', prop={'size': 4})
plt.savefig(final+'/'+'Food_cond_all.png', dpi=300)
plt.close()    







########################
iteration = ['0.80','0.85','0.90','0.95','0.99']
NUM_COLORS = 12
cm = plt.get_cmap('gist_rainbow')
for z in range(0,len(iteration)):
    onlyfiles2 = [f for f in listdir(tab_c) if (isfile(join(tab_c, f)) and f[:4]==iteration[z])]
    onlyfiles2.sort() 
    
    #  L2S   all
    names = []
    for i in range(0,len(onlyfiles2)):
        name = 0     
        temp1 = pd.read_csv(tab_c+ '/' + onlyfiles2[i], sep=',', header=[0])
        if name == 0:
            name  = str(round(temp1.iloc[1,2],6)) + '_' + str(round(temp1.iloc[1,4],6))
        names.append(name)
        
        ax = plt.gca() 
        ax.set_prop_cycle(color=[cm(1.*i/NUM_COLORS)])
        temp1.plot('time','L2S_n',kind='line',ax=ax)
        
        ax.legend(names, loc='upper left', prop={'size': 4})
    plt.savefig(final+'/'+'L2S_'+ iteration[z] + '.png', dpi=300)
    plt.close()    
    
    #  L2S   sum   all
    names = []
    for i in range(0,len(onlyfiles2)):
        name = 0     
        temp1 = pd.read_csv(tab_c+ '/' + onlyfiles2[i], sep=',', header=[0])
        if name == 0:
            name  = str(round(temp1.iloc[1,2],6)) + '_' + str(round(temp1.iloc[1,4],6))
        names.append(name)
        
        ax = plt.gca() 
        ax.set_prop_cycle(color=[cm(1.*i/NUM_COLORS)])
        temp1.plot('time','L2Ssum_n',kind='line',ax=ax)
        
        ax.legend(names, loc='upper left', prop={'size': 4})
    plt.savefig(final+'/'+'L2S_sum_'+ iteration[z] +'.png', dpi=300)
    plt.close()    
    
    
    #  L2S   max   all
    names = []
    for i in range(0,len(onlyfiles2)):
        name = 0     
        temp1 = pd.read_csv(tab_c+ '/' + onlyfiles2[i], sep=',', header=[0])
        if name == 0:
            name  = str(round(temp1.iloc[1,2],6)) + '_' + str(round(temp1.iloc[1,4],6))
        names.append(name)
        
        ax = plt.gca() 
        ax.set_prop_cycle(color=[cm(1.*i/NUM_COLORS)])
        temp1.plot('time','L2Smax_n',kind='line',ax=ax)
        
        ax.legend(names, loc='upper left', prop={'size': 4})
    plt.savefig(final+'/'+'L2S__max_'+ iteration[z] +'.png', dpi=300)
    plt.close()    
    
    
    
    #  L2S   ad   all
    names = []
    for i in range(0,len(onlyfiles2)):
        name = 0     
        temp1 = pd.read_csv(tab_c+ '/' + onlyfiles2[i], sep=',', header=[0])
        if name == 0:
            name  = str(round(temp1.iloc[1,2],6)) + '_' + str(round(temp1.iloc[1,4],6))
        names.append(name)
        
        ax = plt.gca() 
        ax.set_prop_cycle(color=[cm(1.*i/NUM_COLORS)])
        temp1.plot('time','Ad_n',kind='line',ax=ax)
        
        ax.legend(names, loc='upper left', prop={'size': 4})
    plt.savefig(final+'/'+'Ad_'+ iteration[z] +'.png', dpi=300)
    plt.close()    
    
    
    #  Food cons   ad   all
    names = []
    for i in range(0,len(onlyfiles2)):
        name = 0     
        temp1 = pd.read_csv(tab_c+ '/' + onlyfiles2[i], sep=',', header=[0])
        if name == 0:
            name  = str(round(temp1.iloc[1,2],6)) + '_' + str(round(temp1.iloc[1,4],6))
        names.append(name)
        
        ax = plt.gca() 
        ax.set_prop_cycle(color=[cm(1.*i/NUM_COLORS)])
        temp1.plot('time','Food_cond_ad_n_cumul',kind='line',ax=ax)
        
        ax.legend(names, loc='upper left', prop={'size': 4})
    plt.savefig(final+'/'+'Food_cons_'+ iteration[z] +'.png', dpi=300)
    plt.close()    
        
    