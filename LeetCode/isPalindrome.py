# -*- coding: utf-8 -*-
"""
Created on Sun May 27 21:32:33 2018

@author: DELL
"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
            n=str(x)
            m=n[::-1]
            return m==n