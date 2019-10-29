#################################################

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import scipy.stats as st
#from scipy.stats import truncnorm
#from scipy.stats import multivariate_normal
#from mpl_toolkits.mplot3d import axes3d
#import matplotlib.pyplot as plt
#from mpl_toolkits import mplot3d
#import random
#import time
#import matplotlib

import numpy as np


########
###### Setting parameters
# this script waits for 2 arguments when run "python nest.py argument1 argumument2"  
#     arguments should be numbers

import argparse
## initialize parser
parser = argparse.ArgumentParser()
## add argument 1
parser.add_argument("param1", help="display a square of a given number",
                    type=float)
## add argument 2
parser.add_argument("param2", help="display a square of a given number",
                    type=float)
# pass arguments to the list args
args = parser.parse_args()




n_days = 80
food_source = 'data/space_central_gauss.csv'

#ct2 = strftime("%Y%m%d__%H-%M", gmtime())
#ct2 = 'L1_21_f2-0.05_cycle-m2-sfed_t16'
ct2='5000_NoReprAgeing_f1=30_m2-sfed_60day_100rep'

# mortality parameters  1-m2**(m1+adultAge) 
m0 = 0.05
m0_L2s = 0.05/10
m1 = 0.5
m2 = args.param1
# reproduction parameters    F = round(f1 - f2*self.adultAge**2.5)
f1 = 30
f2 = 0
# coord for the first worm
x_worm0 = 150
y_worm0 = 150

# movement speed based on food availability
s_fed = args.param2
s_hungry = 0.9

# Larvae survival wo food
L1S_s = 6
L2S_s = 30
# Food consumption
food_consumotion_L = 50
food_consumotion_A = 1000

#####
# set file name parameters
fn_name1 = 'm2'
fn_param1 = m2
fn_name2 = 's_fed'
fn_param2 = s_fed    


# create a sum_file   (an empty txt file)
#from time import gmtime, strftime




import os.path
current_directory = os.getcwd()
x = current_directory + '/result/' + ct2 + '/' + ct2 
final_directory = current_directory + '/result/' + ct2
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

saving_time = ct2
sum_file_name = x


for m in range(0,n_days):
    open(sum_file_name + str(n_days) + '.csv', 'a').close()


# saving time parameter





###
# Create a curve files
if not os.path.isfile(final_directory + '/' + '1_curvesA.csv') == True:
    curves = pd.DataFrame(np.zeros((n_days+3, 1)))
    curves.iloc[0,0] = 'p1'
    curves.iloc[1,0] = 'p2'
    for i in range(2,len(curves)):
        curves.iloc[i,0] = i-1 
    curves.to_csv(final_directory + '/' + '1_curvesA.csv')    

if not os.path.isfile(final_directory + '/' + '0_curvesL.csv') == True:
    curves = pd.DataFrame(np.zeros((n_days+3, 1)))
    curves.iloc[0,0] = 'p1'
    curves.iloc[1,0] = 'p2'
    for i in range(2,len(curves)):
        curves.iloc[i,0] = i-1 
    curves.to_csv(final_directory + '/' + '0_curvesL.csv')     

if not os.path.isfile(final_directory + '/' + '0_curvesL2.csv') == True:
    curves = pd.DataFrame(np.zeros((n_days+3, 1)))
    curves.iloc[0,0] = 'p1'
    curves.iloc[1,0] = 'p2'
    for i in range(2,len(curves)):
        curves.iloc[i,0] = i-1 
    curves.to_csv(final_directory + '/' + '0_curvesL2.csv') 
    
if not os.path.isfile(final_directory + '/' + '0_curvesL2S.csv') == True:
    curves = pd.DataFrame(np.zeros((n_days+3, 1)))
    curves.iloc[0,0] = 'p1'
    curves.iloc[1,0] = 'p2'
    for i in range(2,len(curves)):
        curves.iloc[i,0] = i-1 
    curves.to_csv(final_directory + '/' + '0_curvesL2S.csv')     

if not os.path.isfile(final_directory + '/' + '2_curvesF.csv') == True:
    curves = pd.DataFrame(np.zeros((n_days+3, 1)))
    curves.iloc[0,0] = 'p1'
    curves.iloc[1,0] = 'p2'
    for i in range(2,len(curves)):
        curves.iloc[i,0] = i-1 
    curves.to_csv(final_directory + '/' + '2_curvesF.csv')     





from mainloop_def_leg3_fast import mainLoop
from worms2 import Organism


mainLoop(n_days, m0, m0_L2s, m1, m2, f1, f2, x_worm0, y_worm0, s_fed, s_hungry, L1S_s, L2S_s, food_consumotion_L, \
food_consumotion_A, sum_file_name, saving_time, fn_name1,fn_param1, fn_name2,fn_param2, food_source)

