# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:47:24 2024

@author: Xavier Holmes
"""
import pandas as pd
import csv
import os 
import sys

csv_file = sys.argv[1]

print("Preparing individual files from csv " + csv_file)

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

if not os.path.exists(sys.argv[2]):
    os.makedirs(sys.argv[2])
    
os.chdir(sys.argv[2])

for i in range(len(unique_files)):
    current_data = df_from_csv[df_from_csv['File'] == unique_files[i]]
    filename = unique_files[i].split('.')[0]
    filename = filename + '.csv'
    current_data.to_csv(filename, index=False)
    compound_list = [unique_files[i]] * len(current_data)
    compound_list_table = pd.DataFrame({'file': compound_list})
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('#CompoundList\n#\n' + content)
os.chdir('../../../')

print("Files are in folder: " + sys.argv[2])