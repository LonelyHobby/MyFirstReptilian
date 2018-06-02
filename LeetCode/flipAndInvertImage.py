# -*- coding: utf-8 -*-
"""
Created on Mon May 28 20:32:30 2018

@author: DELL
"""

def flipAndInvertImage(A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            A[i]=A[i].reverse()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if(A[i][j]==0):
                    A[i][j]=1
                else:
                    A[i][j]=0
        return A
A=[[1,1,0],[1,0,1],[0,0,0]]
flipAndInvertImage(A)
print(A)