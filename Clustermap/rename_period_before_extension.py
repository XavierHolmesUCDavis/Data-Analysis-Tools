# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:47:02 2024

@author: Xavier Holmes
"""

import os 

folder_path = "Z:/Xavier/Second Year/November_2022/Cyt_1_R2/Adjpoint2/After_GoodQC_11_28/Cytokine_Experiment_Proteins"
print("Renaming files with period before extension")
for filename in os.listdir(folder_path):
    name, ext = os.path.splitext(filename)
    if '.' in name:
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, name.replace('.', '_') + ext))
    else:
        continue