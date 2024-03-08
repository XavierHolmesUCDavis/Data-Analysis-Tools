# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:21:24 2024

@author: Xavier Holmes
"""

import shutil
import sys 
import os 

csv_file = sys.argv[1]
output_folder_path = sys.argv[2]

shutil.copytree("File_Sorting/Individual_Files/"+csv_file, output_folder_path)

# for file in os.listdir(output_folder_path):
#     if not file.endswith(".csv"):
#         os.remove(file)