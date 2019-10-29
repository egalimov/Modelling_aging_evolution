#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 16:32:22 2018

@author: evgenigalimov
"""

################################
################################
################################

import random

#  function for probabilistic mortality   p = probability to die
def mort(p):
    return 1 if random.random() < p else 0

# Class Organism
class Organism(object):
    numOfInstances = 0
    worm_count = 0
    population = {}
    # number of L2S produced
    L2S_new = 0
    # number of L2S converted to adults
    AdultsfFromL2S = 0
    # number of L2S produced
    L2S_new_cycle = 0
    # number of L2S converted to adults
    AdultsfFromL2S_cycle = 0    

    def __init__(self, parent, xc, yc):
            
        self.parent = parent
        self.id = Organism.worm_count
        #self.population.append(self)
        Organism.population[self.id] = self
        Organism.worm_count +=1
        
        # Stage
        self.stage = 'L0'
        self.age = 0
        self.adultAge = 0
        
        self.L1_starved_count = 0
        self.L2_starved_count = 0
        
        # coord
        self.xc = xc
        self.yc = yc
        
        # food state
        self.fed = 1     # 1 means "fed"
        
        # progeny_n
        self.progeny = 0
        
        
    def time(self):
        # L0
        if self.stage == 'L0':
            self.stage = 'L1'
            # L1
        elif self.stage == 'L1' and self.fed == 1:
            self.stage = 'L2'
        elif self.stage == 'L1' and self.fed == 0:
            self.stage = 'L1S'
            self.L1_starved_count = 1
            # L1S            
        elif self.stage == 'L1S' and self.fed == 0:
            self.stage = 'L1S'
            self.L1_starved_count += 1
        elif self.stage == 'L1S' and self.fed == 1:
            self.stage = 'L2'
            # L2
        elif self.stage == 'L2' and self.fed == 1:
            self.stage = 'A'
            self.adultAge = 1
        elif self.stage == 'L2' and self.fed == 0:
            self.stage = 'L2S'
            self.L2_starved_count = 1
            Organism.L2S_new += 1
            Organism.L2S_new_cycle +=1
            # L2S            
        elif self.stage == 'L2S' and self.fed == 0:
            self.stage = 'L2S'
            self.L2_starved_count += 1
        elif self.stage == 'L2S' and self.fed == 1:
            self.stage = 'A'
            self.adultAge = 1
            Organism.AdultsfFromL2S +=1
            Organism.AdultsfFromL2S_cycle +=1
            # Dead
        elif self.stage == 'dead':
            self.stage = 'dead'
            # Adults        
        else:
            self.adultAge += 1
            self.stage = 'A'# + str(self.adultAge)

   
    def survive(self,m0,m0_L2s,m1,m2,L1S_s,L2S_s):
#        m0 = 0.05
#        m1 = 0.5
#        m2 = 0.5
# for L2S m = 0.005  
        livestate = 0
        if self.stage == 'L0':
            livestate = 0
        #    print(m0, 'dead? - ', livestate)
        elif self.stage == 'L1':
            livestate = mort(m0)
        #    print(m0, 'dead? - ', livestate)
        elif self.stage == 'L1S':
            livestate = mort(m0)
        #    print(m0, 'dead? - ', livestate)
        elif self.stage == 'L2':
            livestate = mort(m0)
        #    print(m0, 'dead? - ', livestate)
        elif self.stage == 'L2S':
            livestate = mort(m0_L2s)
        #    print(m0, 'dead? - ', livestate)
        elif self.stage == 'A':
            #print(1-m1-m2**self.adultAge)
            livestate = mort(1-m2**(m1+self.adultAge))
        #    print(1-m2**(m1+self.adultAge), 'dead? - ', livestate)
        
        if livestate == 1:
            self.stage = 'dead'
        elif livestate == 0 and self.stage == 'L1S' and self.L1_starved_count == L1S_s:
            self.stage = 'dead'
        elif livestate == 0 and self.stage == 'L2S' and self.L2_starved_count == L2S_s:
            self.stage = 'dead'
        else:
            self.stage = self.stage
            
       
        
               
    def reproduce(self):
       # global worm_count
       parent1 = self.id
       xc1 = self.xc
       yc1 = self.yc
       o = Organism(parent1, xc1, yc1)
       return o
   
    def progeny_n(self, f1, f2):  # f1 initial progeny number for d0, f2 - decline rate
        self.progeny = round(f1 - f2*self.adultAge**2.5)
        if self.progeny < 0:
            self.progeny = 0
            
    def move(self, s_fed, s_hungry):
       if self.fed == 1:
           s = s_fed
       elif self.fed == 0:
           s = s_hungry
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

