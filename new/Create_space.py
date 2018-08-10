#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:24:53 2018

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



##########  SET THE PARAMETERS
# Parameters to shape the food gradients


# size of 2D space
linx = 300
liny = 300

# set x and y coord the center of the food gradient 1
startx_f1, starty_f1 = 80 , 80
# set x and y coord the center of the food gradient 2
startx_f2, starty_f2 = 220 , 220




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
plt.plot(x, y)


######     put a 2D food gradient to a 2D space
# make a 2D space dataframe
#  2D space size for all food   (will be used in 1_Combine section)
#
#linx = 300
#liny = 300
d = pd.DataFrame(np.zeros((linx, liny)))


##### Food 1

d1 = pd.DataFrame(np.zeros((linx, liny)))

# set x and y coord the center of the food gradient
#startx_f1, starty_f1 = 80 , 80

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
#startx_f2, starty_f2 = 220 , 220

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

plt.show()

# save the space.csv and lists for visualization.
d.to_csv('space.csv', sep=',', encoding='utf-8')
dx.to_csv('dx.csv', sep=',', encoding='utf-8')
dy.to_csv('dy.csv', sep=',', encoding='utf-8')
dz.to_csv('dz.csv', sep=',', encoding='utf-8')







