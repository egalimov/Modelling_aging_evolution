#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:07:34 2018

@author: evgenigalimov
"""

import pandas as pd
import numpy as np
import os.path


#############################################################################
# Copying files to a new folder


current_directory = os.getcwd()

with open("run3_fast.py", "r") as f:
    searchlines = f.readlines()
for i, line in enumerate(searchlines):
    if "ct2=" in line: 
        z = line

z1 = z[5:-2]

csv_folder = current_directory + '/' + 'result/' + z1 + '_csv'
if not os.path.exists(csv_folder):
    os.makedirs(csv_folder)

wd  = current_directory + '/' + 'result/' + z1
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(wd) if (isfile(join(wd, f)) \
        and ((f[:5]==z1[:5])) and f.find('rep') != -1    )]

for i in range(0,len(onlyfiles)):
	print(onlyfiles[i])

import shutil
for i in range(0, len(onlyfiles)):
    shutil.copyfile(wd + '/' + onlyfiles[i], csv_folder+ '/' + onlyfiles[i])



############################################################################
#make a list fo files in new folder

par_save_name = 'list_files.csv'
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(csv_folder) if (isfile(join(csv_folder, f)) \
        and ((f[0]=='0') or (f[0]=='1') or (f[0]=='2') or (f[0]=='3') or (f[0]=='4') or \
             (f[0]=='5') or (f[0]=='6') or (f[0]=='7') or (f[0]=='8') or (f[0]=='9') )      )]


files1 = []
for i in range(0,len(onlyfiles)):
    files1.append(onlyfiles[i])        

df2 = pd.DataFrame({'col':files1})
df2.to_csv(csv_folder+ '/' +par_save_name, sep=',', encoding='utf-8',header=False, index=False)       



