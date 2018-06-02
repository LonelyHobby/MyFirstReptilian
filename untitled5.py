# -*- coding: utf-8 -*-
"""
Created on Tue May 22 19:08:36 2018

@author: DELL
"""
'''
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
plt.plot(x, y,'r--')
plt.title('The example')
plt.xlabel('Hello')
plt.ylabel('world')


import pylab as pl
import numpy as np
pl.figure(figsize=(8,6),dpi=100)
t=np.arange(0.,4.,0.1)
pl.plot(t,t,color='red',linestyle='-',linewidth=3,label='Line 1')
pl.plot(t,t+2,color='green',linestyle='',marker='*',linewidth=3,lable='Line 2')
pl.plot(t,t**2,color='blue',linestyle='',marker='+',linewidth=3,label='Line 3')
pl.legend(loc='upper left')

import pylab as pl 
import numpy as np 
pl.figure(figsize=(8,6),dpi=100) 
t=np.arange(0.,4.,0.1) 
pl.plot(t,t,color='red',linestyle='-',linewidth=3,label='Line 1') 
pl.plot(t,t+2,color='green',linestyle='',marker='*',linewidth=3,label='Line 2') 
pl.plot(t,t**2,color='blue',linestyle='',marker='+',linewidth=3,label='Line 3') 
pl.legend(loc='upper left')
'''

import requests
import re
import json
import pandas as pd
from datetime import date
import time
import matplotlib.pyplot as plt
 
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    r = requests.get(url)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)
    if m:
        quotes = json.loads(m[0])
        quotes = quotes[::-1]
    return  [item for item in quotes if not 'type' in item]
 
quotes = retrieve_quotes_historical('KO')
list1 = []
for i in range(len(quotes)):
    x = date.fromtimestamp(quotes[i]['date'])
    y = date.strftime(x,'%Y-%m-%d')
    list1.append(y)
quotesdf_ori = pd.DataFrame(quotes, index = list1)
# quotesdf_m = quotesdf_ori.drop(['unadjclose'], axis = 1)
quotesdf = quotesdf_ori.drop(['date'], axis = 1)
listtemp = []
for i in range(len(quotesdf)):
    temp = time.strptime(quotesdf.index[i],"%Y-%m-%d")
    listtemp.append(temp.tm_mon)
tempdf = quotesdf.copy()
tempdf['month'] = listtemp
pl.figure(figsize=(8,6),dpi=50) 
closeMeansKO = tempdf.groupby('month').close.mean()
x = closeMeansKO.index
y = closeMeansKO.values
plt.plot(x, y,'o')
plt.savefig('1.jpg')