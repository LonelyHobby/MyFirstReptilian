# -*- coding: utf-8 -*-
"""
Created on Mon May 28 21:07:49 2018

@author: DELL
"""

def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        list=[0]*(right-left+1)
        rusult_list=[]
        for i in range(1,right-left+1):
            list[i]=i%10
            i=i/10
        for i in range(1,right-left+1):
            if (i%list[i]==0):
                result_list.append(i)
        return result_list
        
            