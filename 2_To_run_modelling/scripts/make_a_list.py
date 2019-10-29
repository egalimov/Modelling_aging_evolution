#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 17:35:19 2018

@author: evgenigalimov
"""




import pandas as pd

par_save_name = 'list_files.csv'

import os.path
current_directory = os.getcwd()


# choose all files in the current dir starting with '3'
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(current_directory) if (isfile(join(current_directory, f)) \
        and ((f[0]=='0') or (f[0]=='1') or (f[0]=='2') or (f[0]=='3') or (f[0]=='4') or \
             (f[0]=='5') or (f[0]=='6') or (f[0]=='7') or (f[0]=='8') or (f[0]=='9') )      )]


files1 = []
for i in range(0,len(onlyfiles)):
    files1.append(onlyfiles[i])        

df2 = pd.DataFrame({'col':files1})
df2.to_csv(par_save_name, sep=',', encoding='utf-8',header=False, index=False)       


# 






















