# -*- coding: utf-8 -*-
"""
Created on Wed May 23 14:32:31 2018

@author: DELL
"""

def fun(n):       
    k=1
    sum=1
    list=[0]*100000
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
    for j in range (1,k+1):
        print (list[j])   
        sum*=list[j]
    
    return sum
        
x=int(input("Please input the number: "))
if(x==1):
        print("result is 1 ")
else:
    result=fun(x)
    print ("result is {} ".format(result))