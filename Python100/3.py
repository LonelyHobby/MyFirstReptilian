# -*- coding: utf-8 -*-
"""
Created on Sun May 27 18:51:35 2018

@author: DELL
"""

'''
输入某年某月某日，判断这一天是这一年的第几天？
'''
import datetime
 
y = int(input('Please input the year：'))  
m = int(input('Please input the month：'))  
d = int(input('Please input the day：'))  
 
targetDay = datetime.date(y, m, d)  
dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)  
print('%s是%s年的第%s天。'% (targetDay, y, dayCount.days))