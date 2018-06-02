# -*- coding: utf-8 -*-
"""
Created on Sun May 27 22:00:15 2018

@author: DELL
"""
'''
Converts integers to Roman numerals
'''
def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]  
        str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]  
        res=''  
        for i in range(len(num_list)):  
             while num>=num_list[i]:  
                num-=num_list[i]  
                res+=str_list[i]  
        return res 

'''
Roman numerals converted to integers
'''
def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        convert={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1} 
        for i in range(len(s)-1):
            if convert[s[i]]<convert[s[i+1]]:
                sum=sum-convert[s[i]]
            else:
                sum=sum+convert[s[i]]
        return sum+convert[s[-1]]
