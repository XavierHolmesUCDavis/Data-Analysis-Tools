# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 23:58:12 2024

@author: Xavier Holmes

Script from the original Lebrilla Group N-Glycan Program 
Small edits to enable use with SnakeMake
"""

import sys
import csv
import os

input_folder_path = sys.argv[1]
output_folder_path = sys.argv[2]
## open each file in the input directory
for eachFile in os.listdir(input_folder_path):
    currentFile = csv.reader(open(input_folder_path+'/'+eachFile, "rb"))
    rawData = []
    glycanID = 0
    ## skip the header
    currentFile.next()
    currentFile.next()
    currentFile.next()
    ## read data from file
    for currentLine in currentFile:
        if len(currentLine)>1:
            ## parse and read composition
            Hex = int(currentLine[2].split('_')[0])
            HexNAc = int(currentLine[2].split('_')[1])
            Fuc = int(currentLine[2].split('_')[2])
            NeuAc = int(currentLine[2].split('_')[3])
            ## calculate unique glycan ID number
            glycanID = 2**Hex*3**HexNAc*5**Fuc*7**NeuAc
            ## add to rawData
            rawData.append([eachFile.split('.')[0],currentLine[4],currentLine[0],currentLine[3],Hex,HexNAc,Fuc,NeuAc,currentLine[5],glycanID])
    ## sort by glycan ID
    rawData.sort(key=lambda x: float(x[9]))
    k = 1
    m = 0
    compData = []
    ## add first glycan composition to list
    compData.append(rawData[0])
    while k < len(rawData):
        checker=rawData[k][9]-rawData[k-1][9]
        ## add new glycan composition to list
        if checker!=0:
            compData.append(rawData[k])
            m=m+1
        ## calculate compositional total abundance
        else:
            compData[m][1]=int(compData[m][1])+int(rawData[k][1])
        k=k+1
    ## sort by abundance
    compData.sort(key=lambda x: float(x[1]), reverse=True)
    ## calculate total glycan abundance
    glycanTIC = 0
    for currentLine in compData:
        glycanTIC = glycanTIC + int(currentLine[1])
    ## calculate relative abundance of each composition
    for currentLine in compData:
        currentLine.append(float(currentLine[1])/glycanTIC*100)
    ## make everything look pretty
    for currentLine in compData:
        currentLine=str(currentLine)
    ## designate output file
    y = output_folder_path + '/' + eachFile.split('.')[0] + '_compositional.csv'
    csvfile = open(y,'wb')
    ## write header
    csvfile.write('File,Abundance,Mass (exp.),Class,Hex,HexNAc,Fuc,NeuAc,RT,glycan ID,Rel Abund'+'\n')
    ## write data
    for list in compData:
        for currentLine in list:
            currentLine=str(currentLine)
            csvfile.write(currentLine)
            csvfile.write(',')
        csvfile.write('\n')
    csvfile.close()