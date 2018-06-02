# -*- coding: utf-8 -*-
"""
Created on Sun May 27 23:44:02 2018

@author: DELL
"""

def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        for i in range(1,n+1):
            if (i%3==0 and i%5==0):
                print("FizzBuzz")
            elif (i%3==0):
                print("Fizz")
            elif(i%5==0):
                print("Buzz")
            else:
                print(str(i))
fizzBuzz(15)