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


def mainLoop(n_days, m0, m1, m2, f1, f2, x_worm0, y_worm0, s_fed, s_hungry, L1S_s, L2S_s, food_consumotion_L, food_consumotion_A, sum_file_name, saving_time, fn_name1,fn_param1, fn_name2,fn_param2):
    
######################
### Set food grid    
    # make a food grid
    d = pd.read_csv('data/space.csv', sep=',', index_col=0)
    
    # set x and y coord the center of the food gradient 1
    startx_f1, starty_f1 = 80 , 80
    # set x and y coord the center of the food gradient 2
    startx_f2, starty_f2 = 220 , 220
######################    


    # Table for worm account
    b1 = {'1_time': [0],'2_id':[0],'3_parent':[0], '4_stage':['L0'], '5_adult_age':[0], '6_xc':[0], '7_yc':[0], '8_fed':[0], '9_progeny_n':[0]}
    worm_account = pd.DataFrame(b1)
    
    #### data table for parameters
    parameters = pd.DataFrame([m0, m1, m2, f1, f2, x_worm0, y_worm0, s_fed, s_hungry, L1S_s, L2S_s, food_consumotion_L, food_consumotion_A], index=['m0', 'm1', 'm2','f1', 'f2', 'x_worm0', 'y_worm0', 's_fed', 's_hungry', 'L1S_s', 'L2S_s', 'food_consumotion_L', 'food_consumotion_A'])
    parameters.columns = ['parameters']
    
    
    #### data table for evol_result
    b2 = {'1_time': [0] ,'number_of_A':[0] ,'number_of_L':[0]}
    evol_res = pd.DataFrame(b2)

    #### data table for food_result
    b3 = {'1_time': [0],'food1':[0], 'food2':[0]}
    food_res = pd.DataFrame(b3)    
        
    from worms2 import Organism
    #x_worm0 = 70
    #y_worm0 = 70
    
    worm_0 = Organism(0, x_worm0,y_worm0)
    
    for time1 in range(0,n_days):
    
        
        # feed    
        pop_length = len(Organism.population)
        for a in range(0,pop_length):
            if Organism.population[a].stage != 'dead':
                frx = Organism.population[a].xc
                fry = Organism.population[a].yc
                if Organism.population[a].stage == 'A':        
                    d.iloc[fry, frx] = d.iloc[fry, frx] - food_consumotion_A
                    if d.iloc[fry, frx] < 0: 
                        d.iloc[fry, frx] = 0
                        Organism.population[a].fed = 0
                    else:
                        Organism.population[a].fed = 1
                else:
                    d.iloc[fry, frx] = d.iloc[fry, frx] - food_consumotion_L
                    if d.iloc[fry, frx] < 0: 
                        d.iloc[fry, frx] = 0
                        Organism.population[a].fed = 0
                    else:
                        Organism.population[a].fed = 1
                    
           
        # time and staging
        for a in range(0,pop_length):
            Organism.population[a].time()
                
        # time and staging
        for a in range(0,pop_length):
            Organism.population[a].survive(m0,m1,m2,L1S_s,L2S_s)
        # number of progeny 
        pop_length = len(Organism.population)
        for a in range(0,pop_length):
            if Organism.population[a].stage == 'A':
                Organism.population[a].progeny_n(f1,f2)
            # else:
            #     Organism.population[a].progeny = 0
    
        # move 
        pop_length = len(Organism.population)
        for a in range(0,pop_length):
            if Organism.population[a].stage != 'dead':
                Organism.population[a].move(s_fed, s_hungry)
        
        # number of progeny 
        pop_length = len(Organism.population)
        for a in range(0,pop_length):
            if Organism.population[a].stage == 'A':
                Organism.population[a].progeny_n(f1,f2)
                if Organism.population[a].progeny > 0:
                    for a2 in range(0,Organism.population[a].progeny):
                        Organism.population[a].reproduce()
            else:
                Organism.population[a].progeny = 0
       
        
        # fill the worm account table
        pop_length = len(Organism.population)
        for a in range(0,pop_length):
            b=list()
            b.append(time1)
            b.append(Organism.population[a].id)
            b.append(Organism.population[a].parent)
            b.append(Organism.population[a].stage)
            b.append(Organism.population[a].adultAge)
            b.append(Organism.population[a].xc)
            b.append(Organism.population[a].yc)
            b.append(Organism.population[a].fed)
            b.append(Organism.population[a].progeny)
            worm_account = worm_account.append(pd.Series(b, index=['1_time','2_id','3_parent','4_stage','5_adult_age','6_xc', '7_yc', '8_fed', '9_progeny_n']), ignore_index=True)
    
        # Calculate number of larvaes
        pop_length = len(Organism.population)
        L_count = 0
        for a in range(0,pop_length):
            if Organism.population[a].stage[0] == 'L':
                L_count += 1
        A_count = 0
        for a in range(0,pop_length):
            if Organism.population[a].stage[0] == 'A':
                A_count += 1        
        b2=list()
        b2.append(time1)
        b2.append(A_count)
        b2.append(L_count)
        evol_res = evol_res.append(pd.Series(b2, index=['1_time','number_of_A','number_of_L']), ignore_index=True)        
          
    ##############################
    # Calculate food source amount
        sum_food_1 = 0
        sum_food_2 = 0
                
        lx1 = startx_f1 - 50
        if lx1 < 0:
            lx1 = 0
        rx1 = startx_f1 + 50
        if rx1 >299:
            rx1 = 299        
        lx2 = startx_f2 - 50
        if lx2 < 0:
            lx2 = 0
        rx2 = startx_f2 + 50
        if rx2 > 299:
            rx2 = 299
    
        ly1 = starty_f1 - 50
        if ly1 < 0:
            ly1 = 0
        ry1 = starty_f1 + 50
        if ry1 >299:
            ry1 = 299        
        ly2 = starty_f2 - 50
        if ly2 < 0:
            ly2 = 0
        ry2 = starty_f2 + 50
        if ry2 > 299:
            ry2 = 299
                    
        for n1 in range(lx1, rx1):
            for n2 in range(ly1, ry1):
                sum_food_1 = sum_food_1 + d.iloc[n2, n1]
    
        for n1 in range(lx2, rx2):
            for n2 in range(ly2, ry2):
                sum_food_2 = sum_food_2 + d.iloc[n2, n1]

        # Calculate number of food in food1 and food2
        bb2=list()
        bb2.append(time1)
        bb2.append(sum_food_1)
        bb2.append(sum_food_2)
        food_res = food_res.append(pd.Series(bb2, index=['1_time','food1','food2']), ignore_index=True)        

    
       # print('Food_source_1 = ',sum_food_1, '__food_source_2 = ', sum_food_2, '__worm_# = ',len(Organism.population))
    
       #print('FS1 = ',sum_food_1, '/ FS2= ', sum_food_2, '/ x=', Organism.population[0].xc, '/ y=', Organism.population[0].yc, '/ Fxy', d.iloc[fry, frx] )
       #dz = d



#####  SAVE TABLES
# PARAMETER TO CYCLE ACROSS  (and to put the the files' names)     
    cp_name1 = fn_name1
    cyc_param1 = fn_param1
    cp_name2 = fn_name2
    cyc_param2 = fn_param2
       
## save worm account table in the format: 'YYMMDD_HH-MM__worm_account.csv'
#    from time import gmtime, strftime
##    ct = strftime("%Y%m%d__%H-%M", gmtime())
#    ct = strftime("%Y%m%d", gmtime())
#  Create a new folder 'yyyymmdd__hh-mm' in the folder 'results'
    import os.path
    current_directory = os.getcwd()
    add_f = 'result/' + saving_time
    final_directory = os.path.join(current_directory, add_f)
    if not os.path.exists(final_directory):
       os.makedirs(final_directory)

#   save
    worm_account.to_csv(add_f + '/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + '__worm_account' + '.csv', sep=',', encoding='utf-8')        
    
    # save parameters table in the format: 'YYMMDD_HH-MM__parameters.csv'
#    from time import gmtime, strftime
#    ct = strftime("%Y%m%d__%H-%M", gmtime())
    parameters.to_csv(add_f + '/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + '__parameters' + '.csv', sep=',', encoding='utf-8')      
    
    # save parameters table in the format: 'YYMMDD_HH-MM__parameters.csv'
#    from time import gmtime, strftime
#    ct = strftime("%Y%m%d__%H-%M", gmtime())
    evol_res.to_csv(add_f + '/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + '__evol' + '.csv', sep=',', encoding='utf-8') 

#   # save food  
    food_res.to_csv(add_f + '/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + '__food_res' + '.csv', sep=',', encoding='utf-8')        



#   append L_count to the sum result file
    sum_line = cp_name1 +','+ str(cyc_param1) + ',' + cp_name2 +','+ str(cyc_param2) + ',' + 'sum_food_1' + ',' + str(sum_food_1) + ',' + 'sum_food_2' + ',' + str(sum_food_2) +','+ 'Adult_num' +','+str(A_count) +','+ 'L_num' +','+str(L_count) +'\n'
    with open(sum_file_name, 'a') as file:
            file.write(sum_line)

