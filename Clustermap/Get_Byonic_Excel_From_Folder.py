# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:16:25 2024

@author: Xavier Holmes
"""

# Script to get the .xlsx files from a folder containing byonic output folders each of which has one .xlsx file in it 


import os
import shutil

# Add path to folder w/ byonic output folders

directory_path = 'Z:/Xavier/Second Year/November_2022/Cyt_1_R2/Adjpoint2/After_GoodQC_11_28'

folders = [f for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]
print(folders)

for folder in folders: 
    print('Working on folder: ', folder)
    files = os.listdir(directory_path + '/' + folder)
    for file in files:
        if file.endswith('.xlsx'):
            print(file)
            shutil.copy(directory_path + '/' + folder + '/' + file, directory_path + '/' + file)
            print('copied ' + file + ' to ' + directory_path + '/' + file)