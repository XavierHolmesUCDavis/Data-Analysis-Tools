# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 14:16:49 2023

@author: Xavier Holmes

Translated from script original in MATLAB

"""
import pandas as pd
import os

data = pd.read_csv('Cytokine_Assay_1.csv')
unique_files = data['File'].unique()

for i in range(len(unique_files)):
    current_data = data[data['File'] == unique_files[i]]
    filename = unique_files[i] + '.csv'
    current_data.to_csv(filename, index=False)
    compound_list = [unique_files[i]] * len(current_data)
    compound_list_table = pd.DataFrame({'file': compound_list})
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write('#CompoundList\n#\n' + content)
