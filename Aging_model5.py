#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 21:51:36 2018

@author: evgenigalimov
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



################################
################################
################################


###  fill the position
#d[2][2]=1

##########   Create a food gradient

#import scipy.stats as st
xcoord = []
l = []  
for i in range(-1500, 1500):
    i = i
    xcoord.append(i)
    l.append(round(st.norm.pdf(i,0,15)*1000))  #*1000))

# Create a dataframe with coord and int_for_food
d5 = {'coord':xcoord,'food':l}
food1 = pd.DataFrame(d5)

#import numpy as np
#import matplotlib.pyplot as plt

x = np.asarray(xcoord, dtype=None, order=None)
y = np.asarray(l, dtype=None, order=None)
#plt.plot(x, y)


######     put a 2D food gradient to a 2D space
# make a 2D space dataframe
#  2D space size for all food   (will be used in 1_Combine section)
linx = 300
liny = 300
d = pd.DataFrame(np.zeros((linx, liny)))


##### Food 1

d1 = pd.DataFrame(np.zeros((linx, liny)))

# set x and y coord the center of the food gradient
startx_f1, starty_f1 = 80 , 80

# fill the 2D space according to the gradient
for m in range(0, linx):
    for n in range(0, liny):
      
        z1 = food1.index[food1['coord'] == m-startx_f1].tolist()
        z1 = z1[0]
        z1 = food1.loc[z1]['food']
        
        z2 = food1.index[food1['coord'] == n-starty_f1].tolist()
        z2 = z2[0]
        z2 = food1.loc[z2]['food']
        z3 = z1*z2    
        
        d1[m][n] = z3


##### Food 2
        
d2 = pd.DataFrame(np.zeros((linx, liny)))
        
# set x and y coord the center of the food gradient
startx_f2, starty_f2 = 220 , 220

# fill the 2D space according to the gradient
for m in range(0, linx):
    for n in range(0, liny):
      
        z1 = food1.index[food1['coord'] == m-startx_f2].tolist()
        z1 = z1[0]
        z1 = food1.loc[z1]['food']
        
        z2 = food1.index[food1['coord'] == n-starty_f2].tolist()
        z2 = z2[0]
        z2 = food1.loc[z2]['food']
        z3 = z1*z2    
        
        d2[m][n] = z3

#######  1_Combine (add all linear spaces with food)

for m in range(0, linx):
    for n in range(0, liny):
        d[m][n] = d1[m][n] + d2[m][n] 



#####     Create 3 column dataframe to visualize the 2D space with the 2D food 
#grad 
#col_names =  ['A', 'B', 'C']
#d3  = pd.DataFrame(columns = col_names)
#for m in range(0, 15):
#    for n in range(0, 15):
#        mn = d[m][n]
#        d3.loc[len(d3)] = [m, n, mn]


#####   Plot the 3D dataframe
#from mpl_toolkits import mplot3d
#import numpy as np
#import matplotlib.pyplot as plt


dx = pd.DataFrame(np.zeros((linx, liny)))
for n1 in range(0, linx):
    for n2 in range(0, liny):
        dx[n1][n2] = n1

dy = pd.DataFrame(np.zeros((linx, liny)))
for m1 in range(0, linx):
    for m2 in range(0, liny):
        dy[m1][m2] = m2

dz = d

#from mpl_toolkits.mplot3d import axes3d
#import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot
ax.plot_wireframe(dx, dy, dz, rstride=10, cstride=10)

#plt.show()










################################
################################
################################


#  Class worms




# defining class worms    
class Organism(object):
    numOfInstances = 0
    worm_count = 0
    population = {}
    
    def __init__(self, parent, xc, yc):
            
        self.parent = parent
        self.id = Organism.worm_count
        #self.population.append(self)
        Organism.population[self.id] = self
        Organism.worm_count +=1
        
        # coord
        self.xc = xc
        self.yc = yc
        
        # food state
        self.fed = 1
        
               
    def reproduce(self):
       # global worm_count
       parent1 = self.id
       xc1 = self.xc
       yc1 = self.yc
       o = Organism(parent1, xc1, yc1)
       return o
    def move(self):
       if self.fed == 1:
           s = 1
       elif self.fed == 0:
           s = 16
       xadd = round(random.uniform(-s, s)*10)
       yadd = round(random.uniform(-s, s)*10)
       self.xc +=xadd
       self.yc +=yadd
       if self.xc < 0:
           self.xc = 0
       if self.xc >299:
           self.xc = 299
       if self.yc < 0:
           self.yc = 0     
       if self.yc >299:
           self.yc = 299     
#       print(xadd)
#       print(yadd)
#       print(self.xc)
#       print(self.yc)









################################
################################
################################


### Running experiment field

worm_0 = Organism(0, 0, 0)      

#xs.append(250)
#ys.append(150)
#zs.append(400)

for time1 in range(0,2):

    # run through all population 
    # reproduce
    pop_length = len(Organism.population)
    for a in range(0,pop_length):
        #print(Organism.population[a].id, "___", Organism.population[a].parent)
        Organism.population[a].reproduce()
    
    # feed
    pop_length = len(Organism.population)
    for a in range(0,pop_length):
        frx = Organism.population[a].xc
        fry = Organism.population[a].yc
        d[frx][fry] = d[frx][fry] - 1000000
        if d[frx][fry] < 0: 
            d[frx][fry] = 0
            worm_0.fed = 0
        
    # move 
    pop_length = len(Organism.population)
    for a in range(0,pop_length):
        Organism.population[a].move()

    # tables for visual
    pop_length = len(Organism.population)
    # set vectors for coordinates
    xs = []
    ys = []
    zs = []  
    for a in range(0,pop_length):
        xs.append(Organism.population[a].xc)
        ys.append(Organism.population[a].yc)
        zs.append(0)

    #  count number of worms in similar positions 
    q0=0
    while q0 < len(xs):
       # print(q0)
        
        yyy = 0
        q1 = q0+1
        deleten = 0
        deleteL = []
        while q1 < len(xs):
            #print(q0,'__',q1)
            if xs[q1] == xs[q0] and ys[q1] == ys[q0]:
              #  print('del', q1)
                yyy +=1
                deleteL.append(q1)
            q1 +=1
        for hhh in sorted(deleteL, reverse=True):
            del xs[hhh]
            del ys[hhh]
            del zs[hhh]
        zs[q0] = yyy + 1
        q0 +=1 
      #  print(q0, 'has', yyy, 'copies')
    
    




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
            sum_food_1 = sum_food_1 + d[n1][n2]

    for n1 in range(lx2, rx2):
        for n2 in range(ly2, ry2):
            sum_food_2 = sum_food_2 + d[n1][n2]

    print('Food_source_1___',sum_food_1, '____food_source_2__', sum_food_2)






    
################################
################################
################################









# Visualizing the process
        


    # Plot
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(dx, dy, dz, rstride=10, cstride=10)
    
    ax.scatter(xs, ys, zs, c='red', marker=3)
    
    plt.savefig('time_' + str(time1) + '.png', dpi=300)
#    plt.show()


# pop  = Organism.population
#pop1 = Organism.population




#  measure the time of the run
import time
start = time.time()
end = time.time()
print('time_of_run',end - start)





