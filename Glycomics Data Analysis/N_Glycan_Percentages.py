# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 17:10:49 2023

@author: Xavier Holmes

Translated from MATLAB 
"""

import pandas as pd
import os 

os.chdir('C:/Python Scripts/Glycomics Data Analysis')

original_sheet_name = 'Cytokine_Assay_Rel.csv'

data = pd.read_csv(original_sheet_name)

sample_names = data.columns[6:]
sample_names = [sample_name.split('_compositional')[0] for sample_name in sample_names]

percentages = []

for i in range(len(sample_names)):
    sample_data = data.iloc[:, 6+i]
    hm_count = 0
    undec_count = 0
    fuc_count = 0
    sia_count = 0
    sifuc_count = 0
    
    for j in range(len(sample_data)):
        class_str = data.loc[j, 'Class']
        
        if class_str == 'HM':
            hm_count += sample_data[j]
        elif 'F' not in class_str and 'S' not in class_str:
            undec_count += sample_data[j]
        elif 'F' in class_str and 'S' not in class_str:
            fuc_count += sample_data[j]
        elif 'S' in class_str and 'F' not in class_str:
            sia_count += sample_data[j]
        elif 'F' in class_str and 'S' in class_str:
            sifuc_count += sample_data[j]
        
    total = sum(sample_data)
    percentages.append([hm_count/total, undec_count/total, fuc_count/total, sia_count/total, sifuc_count/total])

percentages_df = pd.DataFrame(percentages, columns=['High_Mannose', 'Undecorated', 'Fucosylated', 'Sialylated', 'Sialofucosylated'])
percentages_df = percentages_df*100
percentages_df.insert(0, 'Sample', sample_names)
filename = original_sheet_name
name = filename.split('.')[0]

output_filename = name + '_percentages_GraphPad.csv'

percentages_df.to_csv(output_filename, index=False)

print('Percentages written to', output_filename)


