# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 14:36:22 2024

@author: Xavier Holmes
"""

import os
import sys

experiment_csv_folder_path = sys.argv[1]
output_file_path = sys.argv[2]
file_names = []

for filename in os.listdir(experiment_csv_folder_path):
    if filename.endswith('.csv'):
        file_names.append(filename)

with open(output_file_path, 'w') as file:
    file.write('File Names\n')
    for filename in file_names:
        file.write(filename + '\n')
