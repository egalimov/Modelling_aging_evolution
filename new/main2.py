#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 20:07:37 2018

@author: evgeniygalimov
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.stats import truncnorm
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import random
import time


#ddddd1 = pd.DataFrame(np.zeros((300, 300)))

d = pd.read_csv('data/space.csv', sep=',', index_col=0)

dx = pd.read_csv('data/dx.csv', sep=',', index_col=0)
dy = pd.read_csv('data/dy.csv', sep=',', index_col=0)
dz = pd.read_csv('data/dz.csv', sep=',', index_col=0)

########
###### Setting parameters
# this script waits for 2 arguments when run "python nest.py argument1 argumument2"  
#     arguments should be numbers

import argparse
# initialize parser
parser = argparse.ArgumentParser()
# add argument 1
parser.add_argument("param1", help="display a square of a given number",
                    type=float)
# add argument 2
parser.add_argument("param2", help="display a square of a given number",
                    type=float)
# pass arguments to the list args
args = parser.parse_args()
# print 
#print (args.param1) # print argument 1
#print (args.param2)    # print argument 1

n_days = 29
# mortality parameters  1-m2**(m1+adultAge) 
m0 = 0.05
m1 = 0.5
m2 = args.param1
# reproduction parameters    F = round(f1 - f2*self.adultAge**2.5)
f1 = 4
f2 = 0.2
# coord for the first worm
x_worm0 = 70
y_worm0 = 70

# movement speed based on food availability
s_fed = args.param2
s_hungry = 0.8

# Larvae survival wo food
L1S_s = 9
L2S_s = 9
# Food consumption
food_consumotion_L = 250
food_consumotion_A = 2500

#####
# set file name parameters
fn_name1 = 'm2'
fn_param1 = m2
fn_name2 = 's_fed'
fn_param2 = s_fed    






# create a sum_file   (an empty txt file)
from time import gmtime, strftime
#ct2 = strftime("%Y%m%d__%H-%M", gmtime())
ct2 = 'L1_17_cycle-m2-sfed_t3'
import os.path
current_directory = os.getcwd()
x = current_directory + '/result/' + ct2 + '/' + ct2 + '.csv'
final_directory = current_directory + '/result/' + ct2
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

open(x, 'a').close()
sum_file_name = x

# saving time parameter
saving_time = ct2

from mainloop_def import mainLoop
from worms2 import Organism
# Main function    
# we pass to the mainLoop function the following parameters:
# 1) parameters for the evolution model: 
#        n_days, m0, m1, m2, f1, f2, x_worm0, y_worm0, s_fed, s_hungry, L1S_s, L2S_s, food_consumotion_L, food_consumotion_A
# 2) name for a folder to save: sum_file_name
#   and time of saving: saving_time, 
# 3) parameters' names and values we cycle which will be written to the files' names:
#         fn_name1,fn_param1, fn_name2,fn_param2
mainLoop(n_days, m0, m1, m2, f1, f2, x_worm0, y_worm0, s_fed, s_hungry, L1S_s, L2S_s, food_consumotion_L, food_consumotion_A, sum_file_name, saving_time, fn_name1,fn_param1, fn_name2,fn_param2)
#    print(len(Organism.population))

        
