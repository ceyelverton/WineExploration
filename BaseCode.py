# -*- coding: utf-8 -*-
"""
Created on Thu May 31 14:31:44 2018

@author: Clyde
"""

import csv
import pandas as pd

RedWine = pd.read_csv('winequality-red.csv')
RedWine



with open('winequality-red.csv') as csvfile:
    RedWine = csv.reader(csvfile,delimiter=",")
    
    RedDict={}
    
    for row in RedWine:
        
        