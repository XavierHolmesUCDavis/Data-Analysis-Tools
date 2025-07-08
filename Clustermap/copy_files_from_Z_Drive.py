# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:50:16 2024

@author: Xavier Holmes
"""

import os
import shutil


byonic_file_directory = "Z:\Armin\#MilkDMI\BovineByonicOutputs"
new_directory = "C:\Python Scripts\Snake Make Workflows\Amino_Acid_Abundance\Byonic_Output"

for main_folder in os.listdir(byonic_file_directory):
    if main_folder.startswith("P"):
        for folder in os.listdir(byonic_file_directory + "\\" + main_folder):
            for file in os.listdir(byonic_file_directory + "\\" + main_folder + "\\" + folder):
                if file.endswith(".xlsx"):
                    shutil.copy(byonic_file_directory + "\\" + main_folder + "\\" + folder + "\\" + file, new_directory)
                