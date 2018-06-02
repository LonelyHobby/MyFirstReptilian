# -*- coding: utf-8 -*-
"""
Created on Tue May 22 20:33:11 2018

@author: DELL
"""
'''
import pandas as pd
stu_df = pd.DataFrame()
stu_df = pd.read_excel('1.xlsx', sheet_name = 'scores')
stu_df['sum'] = stu_df['Python'] + stu_df['Math']
stu_df.to_excel('1.xlsx', sheet_name = 'scores')
'''

import numpy as np 
import pylab as pl 
x = np.linspace(-np.pi, np.pi, 256) 
s = np.sin(x) 
c = np.cos(x) 
pl.title('Trigonometric Function') 
pl.xlabel('X') 
pl.ylabel('Y') 
pl.plot(x,s) 
pl.plot(x,c)
