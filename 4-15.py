# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:32:31 2018

@author: DELL
"""

def fun(n):
    k=1
    list=[1]*100
    if(n<3):
        list[1]=0
        return
    if(n<5):
        list[k]=1;
        list[++k]=n-1
        return
    list[1]=2
    n-=2
    while(n>list[k]):
        k+=1
        list[k]=list[k-1]+1
        n-=list[k]
    if(n==list[k]):
        list[k]+=1
        n-=1
    for i in range (0,n):
        list[k-i]+=1
        
x=int(input("Please input the number: "))
result=fun(x)
print ("The result is {}".format(result))
    
