# -*- coding: utf-8 -*-
"""
Created on Tue May 29 19:48:08 2018

@author: DELL
"""

def uniqueMorseRepresentations(words):
        """
        :type words: List[str]
        :rtype: int
        """
        list0=[]  
        out = 0  
        listABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  
        listmorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]  
        for str1 in words:  
            str2 = ''  
            for i in range(0,len(str1)):  
                str2 = str2+listmorse[listABC.index(str1[i])]  
            if(str2 in list0):  
                continue  
            else:  
                list0.append(str2)  
                out +=1  
        return out  
words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words))
