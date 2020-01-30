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




def mainLoop(n_days, m0, m0_L2s, m1, m2, f1, f2, x_worm0, y_worm0, s_fed, s_hungry, L1S_s, L2S_s, food_consumotion_L, \
food_consumotion_A, sum_file_name, saving_time, fn_name1,fn_param1, fn_name2,fn_param2, food_source):

#####  SAVE TABLES
# PARAMETER TO CYCLE ACROSS  (and to put the the files' names)     
    cp_name1 = fn_name1
    cyc_param1 = fn_param1
    cp_name2 = fn_name2
    cyc_param2 = fn_param2

    
    #from tables import SaveHeatMap
    #import seaborn as sns 
    
#  Create a new folder 'yyyymmdd__hh-mm' in the folder 'results'
#    import os.path
#    current_directory = os.getcwd()
    add_f = 'result/' + saving_time
#    final_directory = os.path.join(current_directory, add_f)
#    if not os.path.exists(final_directory):
#       os.makedirs(final_directory)    
######################
### Set food grid    
    # make a food grid
    d = pd.read_csv(food_source, sep=',', index_col=0)
    
    # set x and y coord the center of the food gradient 1
#    startx_f1, starty_f1 = 80 , 80
    # set x and y coord the center of the food gradient 2
    startx_f2, starty_f2 = 80 , 80
######################    


    # # Table for worm account
    # b1 = {'1_time': [0],'2_id':[0],'3_parent':[0], '4_stage':['L0'], '5_adult_age':[0], '6_xc':[0], '7_yc':[0], '8_fed':[0], '9_progeny_n':[0]}
    # worm_account = pd.DataFrame(b1)
    
    #### data table for parameters
    parameters = pd.DataFrame([food_source, m0, m0_L2s, m1, m2, f1, f2, x_worm0, y_worm0, s_fed, s_hungry, L1S_s, L2S_s, food_consumotion_L, food_consumotion_A], \
                              index=['food_source', 'm0','m0_L2s' , 'm1', 'm2','f1', 'f2', 'x_worm0', 'y_worm0', 's_fed', 's_hungry', 'L1S_s', 'L2S_s', 'food_consumotion_L', 'food_consumotion_A'])
    parameters.columns = ['parameters']
    
    
    #### data table for evol_result
    b2 = {'1_time': [0] ,'number_of_A':[0] ,'number_of_L':[0], 'starved_A':[0],'starved_L':[0], 'number_of_L2':[0], 'starved_L2':[0], 'Produced_L2S_cycle':[0], 'Adults_from_L2S_cycle':[0], 'Diff_L2S_cycle':[0], 'Total_L2S - L2Sconverted_to_adults':[0]}
    evol_res = pd.DataFrame(b2)
    # #### data table for food_result
    # b3 = {'1_time': [0],'food1':[0],'food2':[0], 'fc_A':[0],'fc_L':[0]}
    # food_res = pd.DataFrame(b3)    
        
    from worms2 import Organism
    worm_0 = Organism(0, x_worm0,y_worm0)
    worm_1 = Organism(0, 149,151)
    worm_2 = Organism(0, 151,149)
    worm_3 = Organism(0, 149,149)
    worm_4 = Organism(0, 151,151)
    worm_5 = Organism(0, 152,149)
    worm_6 = Organism(0, 149,152)


    #x_worm0 = 70
    #y_worm0 = 70
#    from tables import Table_collection
#    table = Table_collection()
    
    
    # use only for single worm tracking
    #current_view2 = pd.read_csv('data/zero.csv', sep=',', index_col=0)

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
       
        
        # # fill the worm account table
        # pop_length = len(Organism.population)
        # for a in range(0,pop_length):
        #     b=list()
        #     b.append(time1)
        #     b.append(Organism.population[a].id)
        #     b.append(Organism.population[a].parent)
        #     b.append(Organism.population[a].stage)
        #     b.append(Organism.population[a].adultAge)
        #     b.append(Organism.population[a].xc)
        #     b.append(Organism.population[a].yc)
        #     b.append(Organism.population[a].fed)
        #     b.append(Organism.population[a].progeny)
        #     worm_account = worm_account.append(pd.Series(b, index=['1_time','2_id','3_parent','4_stage','5_adult_age','6_xc', '7_yc', '8_fed', '9_progeny_n']), ignore_index=True)



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
        

        
# ##        ###########   Visualize the whole population
# ##        # tables for visual
#         current_view = pd.read_csv('data/zero.csv', sep=',', index_col=0)
#         pop_length = len(Organism.population)
#         # set vectors for coordinates
#         xs = []
#         ys = []
#         zs = []  
#         for a in range(0,pop_length):
#             xs.append(Organism.population[a].xc)
#             ys.append(Organism.population[a].yc)
#             zs.append(0)
#         #  count number of worms in similar positions 
#         q0=0
#         while q0 < len(xs):
#            # print(q0)
            
#             yyy = 0
#             q1 = q0+1
#             deleten = 0
#             deleteL = []
#             while q1 < len(xs):
#                 #print(q0,'__',q1)
#                 if xs[q1] == xs[q0] and ys[q1] == ys[q0]:
#                   #  print('del', q1)
#                     yyy +=1
#                     deleteL.append(q1)
#                 q1 +=1
#             for hhh in sorted(deleteL, reverse=True):
#                 del xs[hhh]
#                 del ys[hhh]
#                 del zs[hhh]
#             zs[q0] = yyy + 1
#             q0 +=1 
#           #  print(q0, 'has', yyy, 'copies')
#         for coor in range(0,len(xs)):
#             current_view.iloc[ys[coor], xs[coor]] = zs[coor]       

#         fig = sns.heatmap(current_view, cbar = False, cmap='binary', linewidths=0.0000001, linecolor='black')
#         plt.savefig(add_f+'/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2)+'pop_'+ str(time1)+ '.jpg', dpi=300)     
#         plt.close()        
#         #SaveHeatMap(current_view, add_f+'/'+'worm_pop'+ str(time1)+ '.jpg')

# #        
# #        # maps with food
#         fig = sns.heatmap(d, cbar = False, cmap='binary', linewidths=0.0000001, linecolor='black')
#         plt.savefig(add_f+'/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2)+'food_pop_'+ str(time1)+ '.jpg', dpi=300)     
#         plt.close()
#        SaveHeatMap(d, add_f+'/'+'food_pop'+ str(time1)+ '.jpg')



#        ###########
        # # Track one worm in the timeseriees
        # xs = []
        # ys = []
        # zs = []          
        # for a in range(0,pop_length):
        #     xs.append(Organism.population[a].xc)
        #     ys.append(Organism.population[a].yc)
        #     zs.append(1)
            
        # for coor in range(0,len(xs)):
        #     current_view2.iloc[ys[coor], xs[coor]] = zs[coor]

#        import seaborn as sns
#        fig = sns.heatmap(current_view2, cbar = False, cmap='binary', linewidths=0.0000001, linecolor='black')
#        fig.set_xlabel('x')
#        fig.set_ylabel('y')
#        plt.title('')
#        # saving plot and tables
#        plt.savefig(add_f+'/'+'single worm'+ str(time1)+ '.jpg', dpi=300)
#        #plt.show()                    
#        
        
        
        
        
          
    ##############################
    # Calculate food source amount
        sum_food_1 = 0
        sum_food_2 = 0
                
#        lx1 = startx_f1 - 50
#        if lx1 < 0:
#            lx1 = 0
#        rx1 = startx_f1 + 50
#        if rx1 >299:
#            rx1 = 299        
        lx2 = startx_f2 - 50
        if lx2 < 0:
            lx2 = 0
        rx2 = startx_f2 + 50
        if rx2 > 299:
            rx2 = 299
  
#        ly1 = starty_f1 - 50
#        if ly1 < 0:
#            ly1 = 0
#        ry1 = starty_f1 + 50
#        if ry1 >299:
#            ry1 = 299        
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
#  food count for 1 
        #for n1 in range(lx1, rx1):
        #    for n2 in range(ly1, ry1):
        #        sum_food_1 = sum_food_1 + d.iloc[n2, n1]

#  food count for 2    
        for n1 in range(lx2, rx2):
            for n2 in range(ly2, ry2):
                sum_food_2 = sum_food_2 + d.iloc[n2, n1]

        # # Calculate number of food in food1 and food2
        # bb2=list()
        # bb2.append(time1)
        # bb2.append(sum_food_1)
        # bb2.append(sum_food_2)
        # bb2.append(fc_A)
        # bb2.append(fc_L)

        # food_res = food_res.append(pd.Series(bb2, index=['1_time','food1','food2','fc_A','fc_L']), ignore_index=True)        
    
       # print('Food_source_1 = ',sum_food_1, '__food_source_2 = ', sum_food_2, '__worm_# = ',len(Organism.population))
    
       #print('FS1 = ',sum_food_1, '/ FS2= ', sum_food_2, '/ x=', Organism.population[0].xc, '/ y=', Organism.population[0].yc, '/ Fxy', d.iloc[fry, frx] )
       #dz = d
    #   append L_count to the sum result fill

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


#        import seaborn as sns
#        fig = sns.heatmap(current_view2, cbar = False, cmap='binary', linewidths=0.0000001, linecolor='black')
#        fig.set_xlabel('x')
#        fig.set_ylabel('y')
#        plt.title('')
#        # saving plot and tables
#        plt.savefig(add_f+'/'+'single worm'+ str(time1)+ '.jpg', dpi=300)
#        #plt.show()                    
#        
    

    # #  Save points where worms were
    # fig = sns.heatmap(current_view2, cbar = False, cmap='binary', linewidths=0.0000001, linecolor='black')
    # fig.set_xlabel('x')
    # fig.set_ylabel('y')
    # plt.title('')
    # # saving plot and tables
    # plt.savefig(add_f+'/'+ cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + 'all_worm_all_time'+ '.jpg', dpi=300)    
    # #SaveHeatMap(current_view2, add_f+'/'+'single worm'+ str(time1)+ '.jpg')


#    import seaborn as sns
#    fig = sns.heatmap(current_view2, cbar = False, cmap='binary', linewidths=0.0000001, linecolor='black')
#    fig.set_xlabel('x')
#    fig.set_ylabel('y')
#    plt.title('')
#    # saving plot and tables
#    plt.savefig(add_f+'/'+'single worm'+ str(time1)+ '.jpg', dpi=300)
#    #plt.show()                    
      
#####  SAVE TABLES
# save curves for larvse changes
#     list1 = []
#     list1.append(fn_param1)
#     list1.append(fn_param2)
#     for z in range(0, evol_res.shape[0]):
#         list1.append(evol_res.iloc[z,2])    
#     curves1 = pd.read_csv(add_f+'/'+ '0_curvesL.csv', sep=',', index_col=0) 
#     curves1[str(cyc_param1)+'_'+str(cyc_param2)] = list1
#     curves1.to_csv(add_f+'/'+ '0_curvesL.csv')

# # save curves for larvse2 changes
#     list1 = []
#     list1.append(fn_param1)
#     list1.append(fn_param2)
#     for z in range(0, evol_res.shape[0]):
#         list1.append(evol_res.iloc[z,3])    
#     curves1 = pd.read_csv(add_f+'/'+ '0_curvesL2.csv', sep=',', index_col=0) 
#     curves1[str(cyc_param1)+'_'+str(cyc_param2)] = list1
#     curves1.to_csv(add_f+'/'+ '0_curvesL2.csv')
    
# # save curves for larvse2S changes
#     list1 = []
#     list1.append(fn_param1)
#     list1.append(fn_param2)
#     for z in range(0, evol_res.shape[0]):
#         list1.append(evol_res.iloc[z,6])    
#     curves1 = pd.read_csv(add_f+'/'+ '0_curvesL2S.csv', sep=',', index_col=0) 
#     curves1[str(cyc_param1)+'_'+str(cyc_param2)] = list1
#     curves1.to_csv(add_f+'/'+ '0_curvesL2S.csv')    
    
# # save curves for adults changes
#     list1 = []
#     list1.append(fn_param1)
#     list1.append(fn_param2)
#     for z in range(0, evol_res.shape[0]):
#         list1.append(evol_res.iloc[z,1])    
#     curves2 = pd.read_csv(add_f+'/'+ '1_curvesA.csv', sep=',', index_col=0) 
#     curves2[str(cyc_param1)+'_'+str(cyc_param2)] = list1
#     curves2.to_csv(add_f+'/'+ '1_curvesA.csv')

# # save curves for food changes
#     list1 = []
#     list1.append(fn_param1)
#     list1.append(fn_param2)
#     for z in range(0, food_res.shape[0]):
#         list1.append(food_res.iloc[z,3])    
#     curves3 = pd.read_csv(add_f+'/'+ '2_curvesF.csv', sep=',', index_col=0) 
#     curves3[str(cyc_param1)+'_'+str(cyc_param2)] = list1
#     curves3.to_csv(add_f+'/'+ '2_curvesF.csv')    
                   
       
## save worm account table in the format: 'YYMMDD_HH-MM__worm_account.csv'
#    from time import gmtime, strftime
##    ct = strftime("%Y%m%d__%H-%M", gmtime())
#    ct = strftime("%Y%m%d", gmtime())


#   save
    #worm_account.to_csv(add_f + '/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + '__worm_account' + '.csv', sep=',', encoding='utf-8')        
    
    # save parameters table in the format: 'YYMMDD_HH-MM__parameters.csv'
#    from time import gmtime, strftime
#    ct = strftime("%Y%m%d__%H-%M", gmtime())
    parameters.to_csv(add_f + '/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + '__parameters' + '.csv', sep=',', encoding='utf-8')      
    
    # save parameters table in the format: 'YYMMDD_HH-MM__parameters.csv'
#    from time import gmtime, strftime
#    ct = strftime("%Y%m%d__%H-%M", gmtime())
    evol_res.to_csv(add_f + '/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + '__evol' + '.csv', sep=',', encoding='utf-8') 

#   # save food  
  #  food_res.to_csv(add_f + '/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + '__food_res' + '.csv', sep=',', encoding='utf-8')        

    # save food table 
    #d.to_csv(add_f + '/' + cp_name1 +'_'+ str(cyc_param1) + '-_-' + cp_name2 +'_'+ str(cyc_param2) + '__food_table' + '.csv', sep=',', encoding='utf-8') 


##   append L_count to the sum result file ONLY FOR THE LAST CYCLE
#    sum_line = cp_name1 +','+ str(cyc_param1) + ',' + cp_name2 +','+ str(cyc_param2) + ',' + 'sum_food_1' + ',' + str(sum_food_1) + ',' + 'sum_food_2' + ',' + str(sum_food_2) +',' \
#    + 'Adult_num' +','+str(A_count) +','+ 'L_num_last_timepoint' +','+str(L_count)+',' + 'L_num_max'+',' +  str(max(evol_res['number_of_L']))+',' + 'L_num_sum' +',' + str(sum(evol_res['number_of_L'])) +','  \
#    +'L2_num_last_timepoint' +','+str(L2_count)+',' + 'L2_num_max'+',' +  str(max(evol_res['number_of_L2']))+',' + 'L2_num_sum' +',' + str(sum(evol_res['number_of_L2'])) +'\n'
#    with open(sum_file_name + '.csv', 'a') as file:
#            file.write(sum_line)

