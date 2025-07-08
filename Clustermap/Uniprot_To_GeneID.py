# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 20:29:39 2025

@author: Xavier Holmes

Gene symbol string to list
From https://www.syngoportal.org/convert conversion of uniprot IDs
"""

import pandas as pd

excel_path = "C:/Users/xavie/Downloads/UNICOnvert.xlsx"

df = pd.read_excel(excel_path, header=None)
gene_list = df.iloc[0, 0]

gene_list = gene_list.split(' ')

gene_df = pd.DataFrame(gene_list)
# Give header Gene_IDs
gene_df.columns = ['Gene_IDs']
gene_df.to_excel('gene_list.xlsx')