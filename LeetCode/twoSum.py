# -*- coding: utf-8 -*-
"""
Created on Sun May 27 19:13:06 2018

@author: DELL
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list=[0]*2
        for i in range(len(nums)): 
            for j in range(len(nums)):
                if (nums[i]+nums[j]==target):
                    list[0]=i
                    list[1]=j
                    return list

