#################################################

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def mainLoop(n_days, m0, m0_L2s, m1, m2, f1, f2, x_worm0, y_worm0, s_fed, s_hungry, L1S_s, L2S_s, food_consumotion_L, \
food_consumotion_A, sum_file_name, saving_time, fn_name1,fn_param1, fn_name2,fn_param2, food_source):

#####  SAVE TABLES
# PARAMETER TO CYCLE ACROSS  (and to put the the files' names)     
    cp_name1 = fn_name1
    cyc_param1 = fn_param1
    cp_name2 = fn_name2
    cyc_param2 = fn_param2


    add_f = 'result/' + saving_time
  
######################
### Set food grid    
    # make a food grid
    d = pd.read_csv(food_source, sep=',', index_col=0)

    startx_f2, starty_f2 = 80 , 80
######################    

    parameters = pd.DataFrame([food_source, m0, m0_L2s, m1, m2, f1, f2, x_worm0, y_worm0, s_fed, s_hungry, L1S_s, L2S_s, food_consumotion_L, food_consumotion_A], \
                              index=['food_source', 'm0','m0_L2s' , 'm1', 'm2','f1', 'f2', 'x_worm0', 'y_worm0', 's_fed', 's_hungry', 'L1S_s', 'L2S_s', 'food_consumotion_L', 'food_consumotion_A'])
    parameters.columns = ['parameters']
    
    
    #### data table for evol_result
    b2 = {'1_time': [0] ,'number_of_A':[0] ,'number_of_L':[0], 'starved_A':[0],'starved_L':[0], 'number_of_L2':[0], 'starved_L2':[0], 'Produced_L2S_cycle':[0], 'Adults_from_L2S_cycle':[0], 'Diff_L2S_cycle':[0], 'Total_L2S - L2Sconverted_to_adults':[0]}
    evol_res = pd.DataFrame(b2)

        
    from worms2 import Organism
    worm_0 = Organism(0, x_worm0,y_worm0)

    for time1 in range(100,100+n_days):
        
        # feed    
        pop_length = len(Organism.population)
        fc_A=0
        fc_L=0    
        for a in range(0,pop_length):
            if Organism.population[a].stage != 'dead':
                frx = Organism.population[a].xc
                fry = Organism.population[a].yc
                if Organism.population[a].stage == 'A':        
                    if d.iloc[fry, frx] > food_consumotion_A:
                        consumedA = food_consumotion_A
                        fc_A = fc_A + consumedA
                    else:
                        consumedA = d.iloc[fry, frx]
                        fc_A = fc_A + consumedA
                    d.iloc[fry, frx] = d.iloc[fry, frx] - food_consumotion_A
                    
                    if d.iloc[fry, frx] < 0: 
                        d.iloc[fry, frx] = 0
                        Organism.population[a].fed = 0
                    else:
                        Organism.population[a].fed = 1
                else:
                    if d.iloc[fry, frx] >= food_consumotion_L:
                        consumedL = food_consumotion_L
                        fc_L = fc_L + consumedL
                    else:
                        consumedL = d.iloc[fry, frx]
                        fc_L = fc_L + consumedL
                    
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
            Organism.population[a].survive(m0,m0_L2s,m1,m2,L1S_s,L2S_s)
            
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


        # Get the number of starved
        sA = 0
        sL = 0 
        sL2 = 0
        for a in range(0,pop_length):
            if Organism.population[a].stage != 'dead':
                if Organism.population[a].stage == 'A':        
                    if Organism.population[a].fed == 0:
                        sA +=1
                elif Organism.population[a].stage[0] == 'L':    
                    if Organism.population[a].fed == 0:
                        sL +=1
                    if Organism.population[a].stage[:2] == 'L2' and Organism.population[a].fed == 0:
                        sL2 +=1
                        
     
        # Calculate number of larvaes
        pop_length = len(Organism.population)
        L_count = 0
        L2_count = 0
        for a in range(0,pop_length):
            if Organism.population[a].stage[0] == 'L':
                L_count += 1
            if Organism.population[a].stage[:2] == 'L2':
                L2_count +=1    
        A_count = 0
        for a in range(0,pop_length):
            if Organism.population[a].stage[0] == 'A':
                A_count += 1        
        
        
        diff_L2S_produced_cycle = Organism.L2S_new_cycle - Organism.AdultsfFromL2S_cycle
        diff_L2S_sum = Organism.L2S_new - Organism.AdultsfFromL2S
        b2=list()
        b2.append(time1)
        b2.append(A_count)
        b2.append(L_count)
        b2.append(sA)
        b2.append(sL)
        b2.append(L2_count)
        b2.append(sL2)
        b2.append(Organism.L2S_new_cycle)
        b2.append(Organism.AdultsfFromL2S_cycle)
        b2.append(diff_L2S_produced_cycle)
        b2.append(diff_L2S_sum)
        evol_res = evol_res.append(pd.Series(b2, index=['1_time','number_of_A','number_of_L', 'starved_A','starved_L','number_of_L2', 'starved_L2', 'Produced_L2S_cycle', 'Adults_from_L2S_cycle', 'Diff_L2S_cycle', 'Total_L2S - L2Sconverted_to_adults']), ignore_index=True)        
        
          
    ##############################
    # Calculate food source amount
        sum_food_1 = 0
        sum_food_2 = 0
                
   
        lx2 = startx_f2 - 50
        if lx2 < 0:
            lx2 = 0
        rx2 = startx_f2 + 50
        if rx2 > 299:
            rx2 = 299
      
        ly2 = starty_f2 - 50
        if ly2 < 0:
           ly2 = 0
        ry2 = starty_f2 + 50
        if ry2 > 299:
           ry2 = 299
#
#  food count for the whole area
                    
        for n1 in range(0, d.shape[0]):
            for n2 in range(0, d.shape[1]):
                sum_food_1 = sum_food_1 + d.iloc[n2, n1]        

#  food count for 2    
        for n1 in range(lx2, rx2):
            for n2 in range(ly2, ry2):
                sum_food_2 = sum_food_2 + d.iloc[n2, n1]

        # Effectiveness dauers/per larvae produced
        eff = diff_L2S_sum/pop_length

        sum_line = cp_name1 +','+ str(cyc_param1)+ ',' + cp_name2 +','+ str(cyc_param2) + ',' + 'sum_food_1' + ',' + str(sum_food_1) + ',' + 'effectiveness_dauer_prod' + ',' + str(eff) +',' \
        + 'Adult_num' +','+str(A_count) +','+ 'L_num_last_timepoint' +','+str(L_count)+',' + 'L_num_max'+',' + str(max(evol_res['number_of_L']))+',' \
        + 'L_num_sum' +',' + str(sum(evol_res['number_of_L'])) +','\
        +'L2_num_last_timepoint' +','+str(L2_count)+',' + 'L2_num_max'+ ',' + str(max(evol_res['number_of_L2']))+',' + 'L2_num_sum' +',' + str(sum(evol_res['number_of_L2']))  + ',' \
        +'L2S_num_last_timepoint' +','+str(sL2)+',' + 'L2S_num_max' + ',' + str(max(evol_res['starved_L2']))+',' + 'L2S_num_sum' +',' \
        + str(diff_L2S_sum) + ',' +'Food_cons_Ad' + ','+ str(fc_A) + ',' + 'Food_cons_L' + ','+  str(fc_L) + ',' + 'Food_remained' + ',' + str(sum_food_1) + '\n'
        with open(sum_file_name + str(time1) + '.csv', 'a') as file:
                file.write(sum_line)

        # set cycle counters to 0        
        Organism.L2S_new_cycle = 0
        Organism.AdultsfFromL2S_cycle = 0


    parameters.to_csv(add_f + '/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + '__parameters' + '.csv', sep=',', encoding='utf-8')      

    evol_res.to_csv(add_f + '/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + '__evol' + '.csv', sep=',', encoding='utf-8') 


