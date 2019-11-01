#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 18:04:00 2018

@author: evgenigalimov
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import shutil
import math


###### Parser
import argparse
# initialize parser
parser = argparse.ArgumentParser()
# add argument 1
parser.add_argument("param1", help="file name",
                    type=str)

parser.add_argument("param2", help="file name",
                    type=int)
# pass arguments to the list args
args = parser.parse_args()
name_f = args.param1   
name_f = name_f[:-4]





##### Setting other parameters
lastTimePoint = name_f[-3:]



# make a dir
import os.path
current_directory = os.getcwd()
cur_dir = current_directory + '/' + name_f
final_directory = cur_dir
if not os.path.exists(final_directory):
    os.makedirs(final_directory)

# make a dir for videos
cur_dir_adult = current_directory + '/' + 'adults'
cur_dir_L2S = current_directory + '/' + 'L2S'
cur_dir_L2Smax = current_directory + '/' + 'L2Smax'
cur_dir_L2Ssum = current_directory + '/' + 'L2Ssum'
if not os.path.exists(cur_dir_adult):
    os.makedirs(cur_dir_adult)
if not os.path.exists(cur_dir_L2S):
    os.makedirs(cur_dir_L2S)
if not os.path.exists(cur_dir_L2Smax):
    os.makedirs(cur_dir_L2Smax)
if not os.path.exists(cur_dir_L2Ssum):
    os.makedirs(cur_dir_L2Ssum)
cur_dir_t = current_directory + '/' + 'tables'
cur_dir_tno = current_directory + '/' + 'tables_no0'
if not os.path.exists(cur_dir_t):
    os.makedirs(cur_dir_t)
if not os.path.exists(cur_dir_tno):
    os.makedirs(cur_dir_tno)




analyses0 = pd.read_csv(name_f+'.csv', sep=',', header=None)
# sort the dataframe by the 4th column
analyses0 = analyses0.sort_values(by=[3,1], ascending = [True, False])

# remove duplicates by cell in a row
analyses0.columns = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w1','w2','w3','w4','z1','z2','z3','z4','z5','z6','z7','z8','z9']
analyses0 = analyses0.drop_duplicates(subset=['b','d'], keep="first")

# assign indices
analyses0.index = range(len(analyses0))

length_x  =  len(analyses0)

p1_list = ['0.99','0.95','0.90','0.85','0.8']
number_of_repeats = args.param2
p2_list = ['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9']

xlab = 'feds__0.1=High viscos., 0.9=low viscos.'
ylab = 'm2__0.8=ageing, 0.99=non-aging'


### Create table with averaged L and A number
b5 = {'a': [],'b':[], 'c':[],'d': [],'e':[], 'f':[],'g':[],'h':[], 'j':[],'k': [],'l':[], 'm':[], 'n':[], 'o':[], 'p':[], 'r':[], 's':[], 't':[], 'u':[]}
average_result = pd.DataFrame(b5)

for i in range(0,length_x,number_of_repeats):
    bb2=list()
    bb2.append(analyses0.iloc[i, 0])
    bb2.append(analyses0.iloc[i, 1])
    bb2.append(analyses0.iloc[i, 2])
    bb2.append(analyses0.iloc[i, 3])

    bb2.append(analyses0.iloc[i, 22])
    z1 = 0
    for j in range(0,number_of_repeats):
        z1 = z1 + int(analyses0.iloc[i+j, 23])
    z1 = z1/number_of_repeats
    bb2.append(z1)
    # adding SEM
    z4 = 0
    for j in range(0,number_of_repeats):
        z4 = z4 + (z1 - int(analyses0.iloc[i+j, 23]))**2
    z4 = math.sqrt(z4/(number_of_repeats-1))
    z4 = z4/math.sqrt(number_of_repeats)
    bb2.append(z4)
    
    
    bb2.append(analyses0.iloc[i, 26])
    z1 = 0
    for j in range(0,number_of_repeats):
        z1 = z1 + int(analyses0.iloc[i+j, 27])
    z1 = z1/number_of_repeats
    bb2.append(z1)
    # adding SEM
    z4 = 0
    for j in range(0,number_of_repeats):
        z4 = z4 + (z1 - int(analyses0.iloc[i+j, 27]))**2
    z4 = math.sqrt(z4/(number_of_repeats-1))
    z4 = z4/math.sqrt(number_of_repeats)
    bb2.append(z4)


    bb2.append(analyses0.iloc[i, 24])

    z1 = 0
    for j in range(0,number_of_repeats):
        z1 = z1 + int(analyses0.iloc[i+j, 25])
    z1 = z1/number_of_repeats
    bb2.append(z1)
    # adding SEM
    z4 = 0
    for j in range(0,number_of_repeats):
        z4 = z4 + (z1 - int(analyses0.iloc[i+j, 25]))**2
    z4 = math.sqrt(z4/(number_of_repeats-1))
    z4 = z4/math.sqrt(number_of_repeats)
    bb2.append(z4)


    
    bb2.append(analyses0.iloc[i, 8])
    z2 = 0
    for j in range(0,number_of_repeats):
        z2 = z2 + int(analyses0.iloc[i+j, 9])
    z2 = z2/number_of_repeats
    bb2.append(z2)
    # adding SEM
    z4 = 0
    for j in range(0,number_of_repeats):
        z4 = z4 + (z2 - int(analyses0.iloc[i+j, 9]))**2
    z4 = math.sqrt(z4/(number_of_repeats-1))
    z4 = z4/math.sqrt(number_of_repeats)
    bb2.append(z4)




    bb2.append(analyses0.iloc[i, 28])
    z1 = 0
    for j in range(0,number_of_repeats):
        z1 = z1 + int(analyses0.iloc[i+j, 29])
    z1 = z1/number_of_repeats
    z1 = z1/990025
    bb2.append(z1)
    # adding SEM
    z4 = 0
    for j in range(0,number_of_repeats):
        z4 = z4 + ((z1 - int(analyses0.iloc[i+j, 29]))/990025)**2
    z4 = math.sqrt(z4/(number_of_repeats-1))
    z4 = z4/math.sqrt(number_of_repeats)
    
    bb2.append(z4)


    
    average_result = average_result.append(pd.Series(bb2, index=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','r','s','t', 'u']), ignore_index=True)        


### Create table with averaged L and A number   BUT NOT accounting for zeros

b6 = {'a': [],'b':[], 'c':[],'d': [],'e':[], 'f':[],'g':[],'h':[], 'j':[],'k': [],'l':[], 'm':[], 'n':[], 'o':[], 'p':[], 'r':[], 's':[], 't':[], 'u':[]}
average_result_no0 = pd.DataFrame(b6)

for i in range(0,length_x,number_of_repeats):
    bb2=list()
    bb2.append(analyses0.iloc[i, 0])
    bb2.append(analyses0.iloc[i, 1])
    bb2.append(analyses0.iloc[i, 2])
    bb2.append(analyses0.iloc[i, 3])


    bb2.append(analyses0.iloc[i, 22])
    hhh = []
    for j in range(0,number_of_repeats):
        hhh.append(int(analyses0.iloc[i+j, 23]))
    hhh = list(filter((0).__ne__, hhh))
    if len(hhh)==0:
        hhh = [0]
    z1 = sum(hhh) / float(len(hhh))
    bb2.append(z1)
    # adding SEM
    z4 = 0
    count1 = 0
    for j in range(0,number_of_repeats):
        if analyses0.iloc[i+j, 23] != 0:
            z4 = z4 + (z1 - int(analyses0.iloc[i+j, 23]))**2
            count1 += 1
    if count1 ==0:
        z4 = 0
    elif count1 == 1:
        z4 = math.sqrt(z4)
    else:
        z4 = math.sqrt(z4/(count1-1))
        z4 = z4/math.sqrt(count1)
    bb2.append(z4)
    
    
    
    
    

    bb2.append(analyses0.iloc[i, 26])
    hhh = []
    for j in range(0,number_of_repeats):
        hhh.append(int(analyses0.iloc[i+j, 27]))
    hhh = list(filter((0).__ne__, hhh))
    if len(hhh)==0:
        hhh = [0]
    z1 = sum(hhh) / float(len(hhh))
    bb2.append(z1)
    # adding SEM
    z4 = 0
    count1 = 0
    for j in range(0,number_of_repeats):
        if analyses0.iloc[i+j, 27] != 0:
            z4 = z4 + (z1 - int(analyses0.iloc[i+j, 27]))**2
            count1 += 1
    if count1 ==0:
        z4 = 0
    elif count1 == 1:
        z4 = math.sqrt(z4)
    else:
        z4 = math.sqrt(z4/(count1-1))
        z4 = z4/math.sqrt(count1)
    bb2.append(z4)

    
    
    bb2.append(analyses0.iloc[i, 24])

    hhh = []
    for j in range(0,number_of_repeats):
        hhh.append(int(analyses0.iloc[i+j, 25]))
    hhh = list(filter((0).__ne__, hhh))
    if len(hhh)==0:
        hhh = [0]
    z1 = sum(hhh) / float(len(hhh))
    bb2.append(z1)
    # adding SE
    z4 = 0
    count1 = 0
    for j in range(0,number_of_repeats):
        if analyses0.iloc[i+j, 25] != 0:
            z4 = z4 + (z1 - int(analyses0.iloc[i+j, 25]))**2
            count1 += 1
    if count1 ==0:
        z4 = 0
    elif count1 == 1:
        z4 = math.sqrt(z4)
    else:
        z4 = math.sqrt(z4/(count1-1))
        z4 = z4/math.sqrt(count1)
    bb2.append(z4)
    
    
    
    
    
    bb2.append(analyses0.iloc[i, 8])
    hhh = []
    for j in range(0,number_of_repeats):
        hhh.append(int(analyses0.iloc[i+j, 9]))
    hhh = list(filter((0).__ne__, hhh))
    if len(hhh)==0:
        hhh = [0]
    z1 = sum(hhh) / float(len(hhh))
    bb2.append(z1)
    # adding SE
    z4 = 0
    count1 = 0
    for j in range(0,number_of_repeats):
        if analyses0.iloc[i+j, 9] != 0:
            z4 = z4 + (z1 - int(analyses0.iloc[i+j, 9]))**2
            count1 += 1
    if count1 ==0:
        z4 = 0
    elif count1 == 1:
        z4 = 0
    else:
        z4 = math.sqrt(z4/(count1-1))
        z4 = z4/math.sqrt(count1)
    bb2.append(z4)





    bb2.append(analyses0.iloc[i, 28])
    hhh = []
    for j in range(0,number_of_repeats):
        hhh.append(int(analyses0.iloc[i+j, 29]))
    hhh = list(filter((0).__ne__, hhh))
    if len(hhh)==0:
        hhh = [0]
    z1 = sum(hhh) / float(len(hhh))
    z1 = z1/990025
    bb2.append(z1)
    # adding SE
    z4 = 0
    count1 = 0
    for j in range(0,number_of_repeats):
        if analyses0.iloc[i+j, 29] != 0:
            z4 = z4 + ((z1 - int(analyses0.iloc[i+j, 29]))/990025)**2
            count1 += 1
    if count1 ==0:
        z4 = 0
    elif count1 == 1:
        z4 = 0
    else:
        z4 = math.sqrt(z4/(count1-1))
        z4 = z4/math.sqrt(count1)
    bb2.append(z4)
    



        
    average_result_no0 = average_result_no0.append(pd.Series(bb2, index=['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','r','s','t','u']), ignore_index=True)        







#############################
    # Creating tables and plots for Adults!!!!!!!!!
#########
#  Create square table for average_result_no0
    #  for param1 = 5, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 5
    #  for param1 = 2, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 2
        
par1 = len(p2_list)
par2 = len(p1_list)

sq_table_ad_no0 = pd.DataFrame(np.zeros((par1, par2)))
iii = 0
for xxx in range(0,par1):    
    for yyy in range(0,par2):
        #   iloc[row, col]
        sq_table_ad_no0.iloc[xxx, yyy] = average_result_no0.iloc[iii, 14]
        iii +=1 

# in case of #m2 = 5 
sq_table_ad_no0.columns = p1_list
# in case of #m2 = 2 
sq_table_ad_no0.index = p2_list

sq_table_ad_no0 = sq_table_ad_no0.T


# Create heat map for average_result_no0
import seaborn as sns
fig = sns.heatmap(sq_table_ad_no0, cmap='coolwarm', linewidths=0.25, linecolor='black')
fig.set_xlabel(xlab)
fig.set_ylabel(ylab)
plt.title('# of Adults' + lastTimePoint)
# saving plot and tables
plt.savefig(cur_dir + '/'+ name_f+'adult_no0'+'.jpg', dpi=300)
#plt.show()
plt.close()

#####
#  Create square table for average_result
    #  for param1 = 5, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 5
    #  for param1 = 2, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 2
        
par1 = len(p2_list)
par2 = len(p1_list)

sq_table_ad = pd.DataFrame(np.zeros((par1, par2)))
iii = 0
for xxx in range(0,par1):    
    for yyy in range(0,par2):
        sq_table_ad.iloc[xxx, yyy] = average_result.iloc[iii, 14]
        iii +=1 

# in case of #m2 = 5
sq_table_ad.columns = p1_list
# in case of #m2 = 2 
#sq_table.columns = ['0.99','0.8']
sq_table_ad.index = p2_list

sq_table_ad = sq_table_ad.T
    
# Create heat map for average_result
import seaborn as sns
fig = sns.heatmap(sq_table_ad, cmap='coolwarm', linewidths=0.25, linecolor='black')
fig.set_xlabel(xlab)
fig.set_ylabel(ylab)
plt.title('# of Adults' + lastTimePoint)
# saving plot and tables
plt.savefig(cur_dir + '/' +name_f+'adult_no0'+'.jpg', dpi=300)
#plt.show()
plt.close()


# saving plot and tables
average_result.to_csv(cur_dir + '/' +name_f+'_Av'+'.csv', sep=',', encoding='utf-8')
average_result_no0.to_csv(cur_dir + '/' +name_f+'_Av_no0'+'.csv', sep=',', encoding='utf-8')
sq_table_ad.to_csv(cur_dir + '/' +name_f+'_Square_adults'+'.csv', sep=',', encoding='utf-8')
sq_table_ad_no0.to_csv(cur_dir + '/' +name_f+'_Square_no0_adults'+'.csv', sep=',', encoding='utf-8')


shutil.copyfile(cur_dir + '/'+ name_f+'adult_no0'+'.jpg', cur_dir_adult + '/'+ name_f+'adult_no0'+'.jpg')
shutil.copyfile(cur_dir + '/' +name_f+'_Av'+'.csv', cur_dir_t + '/' +name_f+'_Av'+'.csv')
shutil.copyfile(cur_dir + '/' +name_f+'_Av_no0'+'.csv', cur_dir_tno + '/'+name_f+'_Av_no0'+'.csv')

#############################
    # Creating tables and plots for L2Smax!!!!!!!!!
#########
#  Create square table for average_result_no0
    #  for param1 = 5, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 5
    #  for param1 = 2, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 2
        
par1 = len(p2_list)
par2 = len(p1_list)

sq_table_no0_max = pd.DataFrame(np.zeros((par1, par2)))
iii = 0
for xxx in range(0,par1):    
    for yyy in range(0,par2):
        sq_table_no0_max.iloc[xxx, yyy] = average_result_no0.iloc[iii, 11]
        iii +=1 

# in case of #m2 = 5 
sq_table_no0_max.columns = p1_list
# in case of #m2 = 2 
#sq_table_no0.columns = ['0.99','0.8']
sq_table_no0_max.index = p2_list

sq_table_no0_max = sq_table_no0_max.T
# Create heat map for average_result_no0
import seaborn as sns
fig = sns.heatmap(sq_table_no0_max, cmap='coolwarm', linewidths=0.25, linecolor='black')
fig.set_xlabel(xlab)
fig.set_ylabel(ylab)
plt.title('L2S_num_max' + lastTimePoint)
# saving plot and tables
plt.savefig(cur_dir + '/' +name_f+'L2Smax_no0'+'.jpg', dpi=300)
#plt.show()
plt.close()

#####
#  Create square table for average_result
    #  for param1 = 5, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 5
    #  for param1 = 2, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 2
        
par1 = len(p2_list)
par2 = len(p1_list)

sq_table_max = pd.DataFrame(np.zeros((par1, par2)))
iii = 0
for xxx in range(0,par1):    
    for yyy in range(0,par2):
        sq_table_max.iloc[xxx, yyy] = average_result.iloc[iii, 11]
        iii +=1 

# in case of #m2 = 5
sq_table_max.columns = p1_list
# in case of #m2 = 2 
#sq_table.columns = ['0.99','0.8']
sq_table_max.index = p2_list

sq_table_max = sq_table_max.T
    
# Create heat map for average_result
import seaborn as sns
fig = sns.heatmap(sq_table_max, cmap='coolwarm', linewidths=0.25, linecolor='black')
fig.set_xlabel(xlab)
fig.set_ylabel(ylab)
plt.title('L2S_num_max' + lastTimePoint)
# saving plot and tables
plt.savefig(cur_dir + '/' +name_f+'L2Smax.jpg', dpi=300)
#plt.show()
plt.close()
# saving plot and tables
sq_table_max.to_csv(cur_dir + '/' +name_f+'_Square_L2Smax'+'.csv', sep=',', encoding='utf-8')
sq_table_no0_max.to_csv(cur_dir + '/' +name_f+'_Square_no0_L2Smax'+'.csv', sep=',', encoding='utf-8')


shutil.copyfile(cur_dir + '/' +name_f+'L2Smax_no0'+'.jpg', cur_dir_L2Smax + '/' +name_f+'L2Smax_no0'+'.jpg')


#############################
    # Creating tables and plots for L2Ssum!!!!!!!!!
#########
#  Create square table for average_result_no0
    #  for param1 = 5, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 5
    #  for param1 = 2, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 2
        
par1 = len(p2_list)
par2 = len(p1_list)

sq_table_no0_sum = pd.DataFrame(np.zeros((par1, par2)))
iii = 0
for xxx in range(0,par1):    
    for yyy in range(0,par2):
        sq_table_no0_sum.iloc[xxx, yyy] = average_result_no0.iloc[iii, 8]
        iii +=1 

# in case of #m2 = 5 
sq_table_no0_sum.columns = p1_list
# in case of #m2 = 2 
#sq_table_no0.columns = ['0.99','0.8']
sq_table_no0_sum.index = p2_list

sq_table_no0_sum = sq_table_no0_sum.T
# Create heat map for average_result_no0
import seaborn as sns
fig = sns.heatmap(sq_table_no0_sum, cmap='coolwarm', linewidths=0.25, linecolor='black')
fig.set_xlabel(xlab)
fig.set_ylabel(ylab)
plt.title('L2S_num_sum' + lastTimePoint)
# saving plot and tables
plt.savefig(cur_dir + '/' +name_f+'L2Ssum_no0'+'.jpg', dpi=300)
#plt.show()
plt.close()

#####
#  Create square table for average_result
    #  for param1 = 5, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 5
    #  for param1 = 2, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 2
        
par1 = len(p2_list)
par2 = len(p1_list)

sq_table_sum = pd.DataFrame(np.zeros((par1, par2)))
iii = 0
for xxx in range(0,par1):    
    for yyy in range(0,par2):
        sq_table_sum.iloc[xxx, yyy] = average_result.iloc[iii, 8]
        iii +=1 

# in case of #m2 = 5
sq_table_sum.columns = p1_list
# in case of #m2 = 2 
#sq_table.columns = ['0.99','0.8']
sq_table_sum.index = p2_list

sq_table_sum = sq_table_sum.T
    
# Create heat map for average_result
import seaborn as sns
fig = sns.heatmap(sq_table_sum, cmap='coolwarm', linewidths=0.25, linecolor='black')
fig.set_xlabel(xlab)
fig.set_ylabel(ylab)
plt.title('L2S_num_sum' + lastTimePoint)
# saving plot and tables
plt.savefig(cur_dir + '/' +name_f+'L2Ssum.jpg', dpi=300)
#plt.show()
plt.close()
# saving plot and tables
sq_table_sum.to_csv(cur_dir + '/' +name_f+'_Square_L2Ssum'+'.csv', sep=',', encoding='utf-8')
sq_table_no0_sum.to_csv(cur_dir + '/' +name_f+'_Square_no0_L2Ssum'+'.csv', sep=',', encoding='utf-8')


shutil.copyfile(cur_dir + '/' +name_f+'L2Ssum_no0'+'.jpg', cur_dir_L2Ssum + '/' +name_f+'L2Ssum_no0'+'.jpg')


#############################
    # Creating tables and plots for L2S_last_timepoint    !!!!!!!!!
#########
#  Create square table for average_result_no0
    #  for param1 = 5, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 5
    #  for param1 = 2, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 2
        
par1 = len(p2_list)
par2 = len(p1_list)

sq_table_no0_lt = pd.DataFrame(np.zeros((par1, par2)))
iii = 0
for xxx in range(0,par1):    
    for yyy in range(0,par2):
        sq_table_no0_lt.iloc[xxx, yyy] = average_result_no0.iloc[iii, 5]
        iii +=1 

# in case of #m2 = 5 
sq_table_no0_lt.columns = p1_list
# in case of #m2 = 2 
#sq_table_no0.columns = ['0.99','0.8']
sq_table_no0_lt.index = p2_list

sq_table_no0_lt = sq_table_no0_lt.T
# Create heat map for average_result_no0
import seaborn as sns
fig = sns.heatmap(sq_table_no0_lt, cmap='coolwarm', linewidths=0.25, linecolor='black')
fig.set_xlabel(xlab)
fig.set_ylabel(ylab)
plt.title('L2S_num_lt' + lastTimePoint)
# saving plot and tables
plt.savefig(cur_dir + '/' +name_f+'L2S_lt_no0'+'.jpg', dpi=300)
#plt.show()
plt.close()

#####
#  Create square table for average_result
    #  for param1 = 5, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 5
    #  for param1 = 2, param2 = 9 and 5 replicas -> use par1 = 9, par2 = 2
        
par1 = len(p2_list)
par2 = len(p1_list)

sq_table_lt = pd.DataFrame(np.zeros((par1, par2)))
iii = 0
for xxx in range(0,par1):    
    for yyy in range(0,par2):
        sq_table_lt.iloc[xxx, yyy] = average_result.iloc[iii, 5]
        iii +=1 

# in case of #m2 = 5
sq_table_lt.columns = p1_list
# in case of #m2 = 2 
#sq_table.columns = ['0.99','0.8']
sq_table_lt.index = p2_list

sq_table_lt = sq_table_lt.T
    
# Create heat map for average_result
import seaborn as sns
fig = sns.heatmap(sq_table_lt, cmap='coolwarm', linewidths=0.25, linecolor='black')
fig.set_xlabel(xlab)
fig.set_ylabel(ylab)
plt.title('L2S_num_lt' + lastTimePoint)
# saving plot and tables
plt.savefig(cur_dir + '/' +name_f+'L2S_lt.jpg', dpi=300)
#plt.show()
plt.close()
# saving plot and tables
sq_table_lt.to_csv(cur_dir + '/' +name_f+'_Square_lt'+'.csv', sep=',', encoding='utf-8')
sq_table_no0_lt.to_csv(cur_dir + '/' +name_f+'_Square_no0_lt'+'.csv', sep=',', encoding='utf-8')


shutil.copyfile(cur_dir + '/' +name_f+'L2S_lt_no0'+'.jpg', cur_dir_L2S + '/' +name_f+'L2S_lt_no0'+'.jpg')


#
#

#shutil.move(name_f+'.csv', cur_dir)


#####
### Create table with averaged Effectiveness   BUT NOT accounting for zeros

b10 = {'a': [],'b':[], 'c':[],'d': [],'e':[], 'f':[]}
eff_no0 = pd.DataFrame(b10)

for i in range(0,length_x,number_of_repeats):
    bb20=list()
    bb20.append(analyses0.iloc[i, 0])
    bb20.append(analyses0.iloc[i, 1])
    bb20.append(analyses0.iloc[i, 2])
    bb20.append(analyses0.iloc[i, 3])


    bb20.append(analyses0.iloc[i, 6])
    hhh = []
    for j in range(0,number_of_repeats):
        hhh.append((analyses0.iloc[i+j, 7]))

    hhh[:] = (value for value in hhh if value != 0)

#    hhh = list(filter((0.0).__ne__, hhh))
    if len(hhh)==0:
        hhh = [0]
    z9 = sum(hhh) / float(len(hhh))
    bb20.append(z9)
    eff_no0 = eff_no0.append(pd.Series(bb20, index=['a','b','c','d','e','f']), ignore_index=True)        

eff_no0.to_csv(cur_dir + '/' +name_f+'eff'+'.csv', sep=',', encoding='utf-8')






