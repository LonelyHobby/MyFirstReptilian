# -*- coding: utf-8 -*-
"""
Created on Sun May 27 22:02:15 2018

@author: DELL
"""

def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        list=[0]*len(strs)
        rstr=" "
        for i in range(len(strs)):
            list[i]=len(strs[i])
        