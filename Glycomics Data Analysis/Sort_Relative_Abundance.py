# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:16:49 2023
@author: Xavier Holmes
Translated from original in MATLAB
"""

import pandas as pd
import csv
import os

csv_file = 'Yasmine_Glioblastoma_Full_30_MSMS.csv'

print("Preparing individual files for input to N Glycan Program")
prompt = input('Have you named the correct csv file? (y/n) ')
if prompt == 'n':
    csv_file = input('What is the name of the csv file? ')

prompt = input('Have you moved the csv file to the Glycomics Data Analysis folder (Also need an individual results folder)? (y/n) ')
if prompt == 'n':
    print('Change the os.chdir() commands to the correct path and try again')
    exit()

os.chdir('C:/Python Scripts/Glycomics Data Analysis')

data = []

with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    next(csv_reader)
    header = next(csv_reader)[:13] 
    for line in csv_reader:
        data.append(line[:13]) 


df_list = []
for line in data:
    df_list.append(line)

df_from_csv = pd.DataFrame(df_list, columns=header)

unique_files = df_from_csv['File'].unique()
unique_files = [i for i in unique_files if i is not None]

os.chdir('C:/Python Scripts/Glycomics Data Analysis/Individual Result Files')

for i in range(len(unique_files)):
    current_data = df_from_csv[df_from_csv['File'] == unique_files[i]]
    filename = unique_files[i] + '.csv'
    current_data.to_csv(filename, index=False)
    compound_list = [unique_files[i]] * len(current_data)
    compound_list_table = pd.DataFrame({'file': compound_list})
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('#CompoundList\n#\n' + content)
os.chdir('C:/Python Scripts/Glycomics Data Analysis')

print("Files are in the individual results folder")

